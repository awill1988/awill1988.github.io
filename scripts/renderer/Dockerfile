FROM mcr.microsoft.com/playwright/python:v1.65.2-noble@sha256:ef91d1740c114a119450f11e8edb1af4f6d49e641c04207985f0c65a4aaa34a0
RUN python -m pip install --target=/opt/resume --no-cache-dir --only-binary=:all: \
    playwright==1.65.2 PyMuPDF==1.26.7 pillow==12.2.0 \
    greenlet==3.3.2 pyee==13.0.1 typing-extensions==4.15.0
ENV PYTHONPATH=/opt/resume
USER pwuser
ENTRYPOINT ["python", "/work/scripts/render.py"]
