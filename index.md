---
layout: resume
full_name: Adam Williams
title: Staff Software Engineer
location: Bozeman, Montana
intro: Full-stack engineer with more than ten years in financial and geospatial software. Built the SNOTEL service that brought mountain snowpack histories to onX Hunt, Backcountry and Offroad. Financial work spans credit-union payments, core banking and an AI assistant at Arro Finance.
---

## Professional experience
{: #experience tabindex="-1"}

### Arro Finance

#### Staff Software Engineer <span class="dates">Jan 2026 – present</span>

- Built services for credit lines, statements and ledger posting. Automated account balance checks so the banking team could investigate discrepancies.
- Rebuilt Arro’s AI assistant in Rust on Amazon Bedrock. Engineers could release new prompts independently of the service and inspect the tool calls and evaluation scores behind a response.
- Proposed sharing Credit Builder’s web signup with the mobile app. The team could update one form for both platforms, and customers could skip steps they had already completed.
- Built and operated Arro’s Grafana monitoring stack. Implemented the engineering director’s design for capturing banking data changes in AWS and delivering them to Snowflake.
- Added banking rules and test cases to Arro’s AI code-review tools so engineers could check proposed changes against how the ledger records transactions.
- Led engineering’s SOC 2 Type II audit work with Compliance and Operations. The independent auditor issued an unqualified opinion with no exceptions noted.

### onXmaps

#### Senior Software Engineer I, Core Services <span class="dates">Apr 2023 – Dec 2025</span>

Maintained the shared services that handle sign-in and product access across onX’s outdoor apps.

- Built regional access for onX Fish so a single Midwest subscription could unlock maps across Minnesota, Wisconsin and Michigan.
- Worked with Growth on directing users to the appropriate sign-in provider. Automated permission changes when employee accounts were opened, suspended or restored.

#### Backend Software Development Engineer, Backcountry <span class="dates">Apr 2021 – Mar 2023</span>
{: #onx-backcountry tabindex="-1"}

Founding backend engineer for onX Backcountry.

- Designed and built the pipeline and API that turned raw SNOTEL observations into snowpack histories for onX Hunt, Backcountry and Offroad. In Backcountry, skiers could tap a map pin to see how conditions had changed at one of more than 800 mountain stations.
- Built Backcountry’s hiking route pipeline on the engine shared with Offroad. Proposed separate routing data for hikers and expanded the scheduled build from Montana to all 50 states and DC.
- Worked with geospatial specialists on the avalanche terrain exposure layer. Set up a local map datastore where engineers could test data changes on their laptops.

### Foundant Technologies
{: #foundant-technologies tabindex="-1"}

#### Senior Software Engineer <span class="dates">Oct 2020 – Apr 2021</span>

- Built a common Webpack toolchain for four Vue applications. Added progressive web app support to one package and rolled it out to all four through a dependency update.
- Used Webpack 5 Module Federation to give shared components their own release pipeline. An Accounting engineer could add a menu destination in one place for both Accounting and Foundant User.
- Developed the deposit-posting workflow across the accounting interface and backend services, including the logic that reconciled deposits with their journal entries.

### Payouts Network (formerly Wonder Technologies)
{: #payouts-network-formerly-wonder-technologies tabindex="-1"}

#### Solutions Architect <span class="dates">Sep 2020 – Oct 2020</span>
#### Senior Software Engineer / Senior Lead Software Engineer <span class="dates">Sep 2017 – Sep 2020</span>

Worked with Product and IT to plan card-linked rebate programs and design the systems needed to run them.

- Designed and deployed the AWS platform that enabled credit unions to offer rebates on card purchases. Worked with the chief security officer on cloud access and network controls for PCI DSS.
- Took responsibility for the React application customers used to claim a payout. Unified how card entry and confirmation handled a payment, and extended sign-in and shared components across the customer and administrative applications.
- Co-designed the DevOps interview with the director of engineering as the team adopted containers and infrastructure as code. Helped hire and mentor engineers in Bozeman as an individual contributor, including during a CTO transition.

### Composite Apps

#### Full Stack Engineer <span class="dates">Feb 2016 – Sep 2017</span>

- Built earthquake alerts and evacuation reporting for Kinemetrics. Presented the system to municipal leaders in Dubai and trained police officers to use it.
- Rebuilt the server and database for an employee evacuation app. Responders could scan badges on company-issued phones during drills and emergencies. Server-sent events showed them who had been accounted for in real time.
- Built APIs from emailed reports for Warner Bros. Studio Tours. A teammate extended coverage to Burbank and Leavesden.
- Standardized server setup and database migrations for studio reporting and two other client projects.

## Technical skills

**Languages** · Go, Rust, Python, TypeScript, JavaScript, Java and Elixir.\
**Applications and data** · React, Vue, PostgreSQL and Snowflake.\
**Infrastructure** · AWS, Google Cloud, Kubernetes, Terraform and OpenTofu.

## Education and teaching

**University of California, Irvine** · BA in Drama, minor in Information & Computer Science, 2015.

**Code2College** · Volunteer tutoring instructor, 2022–2023.
