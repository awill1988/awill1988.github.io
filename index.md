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
- Proposed sharing the web signup for [Arro Credit Builder](https://www.arrofinance.com/creditbuilder) with the mobile app. The team could update one form for both platforms, and customers could skip steps they had already completed.
- Built and operated Arro’s Grafana monitoring stack. Implemented the engineering director’s design for capturing banking data changes in AWS and delivering them to Snowflake.
- Added banking rules and test cases to Arro’s AI code-review tools so engineers could check proposed changes against how the ledger records transactions.
- Led engineering’s SOC 2 Type II audit work with Compliance and Operations. The independent auditor issued an unqualified opinion with no exceptions noted.

### onXmaps

#### Senior Software Engineer I, Core Services <span class="dates">Apr 2023 – Dec 2025</span>

Maintained the shared services that handle sign-in and product access across onX’s outdoor apps.

- Built onX Fish access controls so [one Midwest subscription](https://www.onxmaps.com/blog/onx-officially-introduces-onx-fish) covered Minnesota, Wisconsin and Michigan.
- Worked with Growth on directing users to the appropriate sign-in provider. Automated permission changes when employee accounts were opened, suspended or restored.

#### Backend Software Development Engineer, Backcountry <span class="dates">Apr 2021 – Mar 2023</span>
{: #onx-backcountry tabindex="-1"}

Founding backend engineer for onX Backcountry.

- Designed and built the SNOTEL pipeline and API for onX Hunt, Backcountry and [Offroad](https://www.onxmaps.com/offroad/app/features/snow-mode). In Backcountry, skiers could tap any of more than 800 mountain stations to see its [snowpack history](https://www.onxmaps.com/backcountry/app/features/snotel-map).
- Built Backcountry’s hiking route pipeline on the engine shared with Offroad. Proposed hiker-specific routing data and expanded the build from Montana to all 50 states and DC. Hikers could [snap a route to hiking trails](https://www.onxmaps.com/backcountry/app/features/hike-planner) and see its distance and elevation change as they planned.
- Worked with geospatial specialists on a map layer showing [four levels of avalanche terrain exposure](https://www.onxmaps.com/blog/onx-backcountry-launches-avalanche-terrain-exposure-scale) for trip planning. Set up a local map datastore where engineers could test data changes on their laptops.

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
- Took responsibility for the React application customers used to [claim an Instant Payout](https://payoutsnetwork.com/terms-and-conditions). Unified how card entry and confirmation handled a payment, and extended sign-in and shared components across the customer and administrative applications.
- Co-designed the DevOps interview with the director of engineering as the team adopted containers and infrastructure as code. Helped hire and mentor engineers in Bozeman as an individual contributor, including during a CTO transition.

### Composite Apps

#### Full Stack Engineer <span class="dates">Feb 2016 – Sep 2017</span>

- Built [earthquake alerts](https://kinemetrics.com/news/kinemetrics-provides-business-continuity-solution-for-dubai-municipality/) and evacuation reporting for Kinemetrics. The company reported deploying the system in four Dubai buildings. Presented it to municipal leaders and trained police officers to use it.
- Rebuilt the server and database for an employee evacuation app. Responders could scan badges on company-issued phones during drills and emergencies. Server-sent events showed them who had been accounted for in real time.
- Built APIs from emailed reports for Warner Bros. Studio Tours. A teammate extended coverage to Burbank and Leavesden.
- Standardized server setup and database migrations for studio reporting and two other client projects.

## Technical skills

**Languages** · Go, Rust, Python, TypeScript, JavaScript, Java and Elixir.\
**Applications and data** · React, Vue, PostgreSQL and Snowflake.\
**Infrastructure** · AWS, Google Cloud, Kubernetes, Terraform and OpenTofu.

## Open source

Added local storage-emulator support to [gcsfs](https://github.com/fsspec/gcsfs/pull/424) and fixed how [Vue CLI](https://github.com/vuejs/vue-cli/pull/6277) generates web app manifests under Webpack 5. Other merged work spans [GDAL](https://github.com/OSGeo/gdal/pull/2965), [pg_tileserv](https://github.com/CrunchyData/pg_tileserv/pull/72), [Ory Hydra](https://github.com/ory/hydra/pull/3867), [onX Hydrax](https://github.com/onXmaps/hydrax/pull/7), [Wazuh](https://github.com/wazuh/wazuh/pull/3729), [xdomls](https://github.com/oeo/xdomls/pull/1) and the [Awesome AI Plugins directory](https://github.com/hashgraph-online/awesome-ai-plugins/pull/683).

Proposed patches for [Vuetify Loader](https://github.com/vuetifyjs/vuetify-loader/pull/166), [IElixir](https://github.com/pprzetacznik/IElixir/pull/60), [FlowPy](https://github.com/onXmaps/FlowPy/pull/1), [Ory Pop](https://github.com/ory/pop/pull/7), [redis-semaphore](https://github.com/swarthy/redis-semaphore/pull/16) and [k8s-auth-client](https://github.com/vimond/k8s-auth-client/pull/2). [Public bug reports and feature proposals](https://github.com/search?q=is%3Apublic+is%3Aissue+author%3Aawill1988+-user%3Aawill1988&type=issues) include [Serverless Framework](https://github.com/serverless/serverless/issues/7578).

Built [Savior](https://github.com/yourmoodai/savior) for local prompt processing, [agent-stream.nvim](https://github.com/awill1988/agent-stream.nvim) for working with coding agents in Neovim, and Rust libraries for handling [optional values](https://github.com/awill1988/somelse) and [errors](https://github.com/awill1988/okerrr). [More projects](https://github.com/awill1988?tab=repositories).

## Education and volunteer service

**University of California, Irvine** · BA in Drama, minor in Information & Computer Science, 2015.

**Bozeman Symphonic Choir** · Volunteer member, 2022–present.\
**Code2College** · Volunteer tutoring instructor, 2022–2023.

## Acting credits

**Montana TheatreWorks** · *White Christmas* (ensemble, in rehearsal for December 2026), *The Music Man* (chorus, 2026) and *Cabaret* (Ernst Ludwig, 2025). **Shane Lalani Center for the Arts** · [*RENT* (Benny, 2026)](https://www.theshanecenter.org/latest-news/meetthecastandcrewofrent-f6t9h).
