"""Build the Jekyll site and render its downloads with the CI browser."""

import argparse
import os
from pathlib import Path
import subprocess

ROOT = Path(__file__).resolve().parents[1]
PLATFORM = "linux/arm64"


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--check", action="store_true", help="compare the selected design with visual-baselines/")
    mode.add_argument("--update-baselines", action="store_true", help="replace baselines with this render")
    parser.add_argument("--proofs", action="store_true", help="include the local typography comparison")
    args = parser.parse_args()
    subprocess.run(["bundle", "exec", "jekyll", "build"], cwd=ROOT, check=True)
    subprocess.run(["docker", "build", "--platform", PLATFORM, "-t", "resume-renderer",
                    "scripts/renderer"], cwd=ROOT, check=True)
    flags = [flag for flag, enabled in (
        ("--check", args.check), ("--update-baselines", args.update_baselines), ("--proofs", args.proofs)
    ) if enabled]
    subprocess.run([
        "docker", "run", "--rm", "--platform", PLATFORM, "--network", "none",
        "--shm-size", "256m", "--user", f"{os.getuid()}:{os.getgid()}",
        "-e", "HOME=/tmp", "-v", f"{ROOT}:/work", "-w", "/work", "resume-renderer", *flags
    ], check=True)


if __name__ == "__main__":
    main()
