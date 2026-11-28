---
layout: resume
full_name: Adam Williams
title: Staff Software Engineer
location: Bozeman, Montana
intro: I’m a staff software engineer in Bozeman, Montana. At Arro Finance, I led engineering through a SOC 2 Type II audit and proposed a shared signup flow for web and mobile. At onX, I built permission checks that let anglers use one membership across three states.
highlights:
  - employer: Arro Finance
    target: arro-finance
    title: Securing employee access
    detail: I put internal tools behind one sign-in and audit trail. The independent auditor noted no exceptions.
  - employer: onX Backcountry
    target: onx-backcountry
    title: Snowpack history for skiers
    detail: I built the service that shows Backcountry skiers snowpack history at over 800 stations. Hunt and Offroad use its snow readings too.
  - employer: onX Identity
    target: onx-identity
    title: One membership across state lines
    detail: My permission checks let onX Fish subscribers open maps in Minnesota, Wisconsin and Michigan.
---

## Professional experience
{: #experience tabindex="-1"}

### <img class="employer-logo" alt="" src="{{ '/assets/employers/arro.png' | relative_url }}"> Arro Finance
{: #arro-finance tabindex="-1"}

#### Staff Software Engineer <span class="dates">Jan 2026 – present</span>

- Led engineering’s work with Compliance and Operations on the SOC 2 Type II audit. Required peer approval for infrastructure changes and tracked fixes in Vanta. The independent auditor issued an unqualified opinion and noted no exceptions.
- Designed employee access to internal tools using Google Workspace SSO and AWS Verified Access. Managed the gateways, shared access policy and audit logging in Terraform.
- Proposed reusing the [Credit Builder](https://www.arrofinance.com/creditbuilder) web signup in Arro’s mobile app. Built the handoff with Product and Engineering so applicants could skip steps they had already completed.
- Replaced Datadog with self-hosted Grafana and OpenTelemetry on AWS. Engineers could check payment-provider health and get alerts when workflows stalled or monitoring went silent.
- Built credit-line, statement and ledger services. Automated reconciliation to flag differences in balances across three systems.

### <img class="employer-logo" alt="" src="{{ '/assets/employers/onx.png' | relative_url }}"> onXmaps
{: #onxmaps}

#### Senior Software Engineer I, Core Services (Identity) <span class="dates">May 2023 – Dec 2025</span>
{: #onx-identity tabindex="-1"}

Built the Rust services that resolved permissions at token exchange, giving [onX Fish Midwest](https://www.onxmaps.com/blog/onx-officially-introduces-onx-fish) subscribers map access across three states.

- Added CockroachDB follower reads for permissions. Our team tuned data placement and consistency so the western region could serve fast reads locally.
- Updated the OAuth consent screen to show each client’s terms and privacy policy and let users submit their choice to allow or deny access.
- Indexed sessions by expiration and automated cleanup of old OAuth and session records to limit identity database growth.
- Wrote the local setup guide and on-call runbook for tracing permission checks and monitoring service health.
- Built authx so engineers could sign in and inspect permissions from a terminal. Dozens used it daily. Teammates added shell integration and npm distribution.

#### Senior Software Engineer I, Backcountry <span class="dates">Apr 2021 – Apr 2023</span>
{: #onx-backcountry tabindex="-1"}

- As Backcountry’s founding backend engineer, built the SNOTEL pipeline and API for Backcountry, Hunt and [Offroad](https://www.onxmaps.com/offroad/app/features/snow-mode). Skiers could tap a Backcountry map pin for [snowpack history](https://www.onxmaps.com/backcountry/app/features/snotel-map) at more than 800 mountain stations.
- Packaged the [avalanche terrain exposure model](https://www.onxmaps.com/blog/onx-backcountry-launches-avalanche-terrain-exposure-scale) in Docker, replacing its manual Anaconda setup. Aligned terrain grids and made inputs configurable so specialists could run the model for new areas.
- Worked with Geospatial Datastore and Routing & Navigation on [snap-to-trail routing](https://www.onxmaps.com/backcountry/app/features/hike-planner). Proposed a trail network for hikers, wrote its Offroute import query and expanded scheduled builds from Montana to all 50 states and DC.
- Set up a local map datastore so engineers could test data changes on their laptops.

### <img class="employer-logo" alt="" src="{{ '/assets/employers/foundant.webp' | relative_url }}"> [Foundant Technologies](https://www.foundant.com/)
{: #foundant-technologies tabindex="-1"}

#### Senior Software Engineer <span class="dates">Oct 2020 – Apr 2021</span>

- Gave shared Vue components their own release pipeline by extending a teammate’s Module Federation prototype with my [Vuetify Loader patch](https://github.com/vuetifyjs/vuetify-loader/pull/166). An Accounting engineer added a menu item once for both Accounting and Foundant User.
- Built one Webpack dependency that gave four Vue apps progressive web app support. [Vue CLI](https://github.com/vuejs/vue-cli/pull/6277) merged my Webpack 5 manifest fix.
- Built deposit posting across the accounting app and backend, reconciling deposits with their journal entries.

### <img class="employer-logo" alt="" src="{{ '/assets/employers/payouts.svg' | relative_url }}"> Payouts Network (formerly Wonder Technologies)
{: #payouts-network-formerly-wonder-technologies tabindex="-1"}

#### Solutions Architect <span class="dates">Sep 2020 – Oct 2020</span>
#### Senior Lead Software Engineer <span class="dates">Mar 2019 – Sep 2020</span>
#### Senior Software Engineer <span class="dates">Sep 2017 – Mar 2019</span>

I designed the AWS platform that credit unions used to issue card rebates and wrote the processor that submitted those credits to Mastercard.

- Moved scheduled clearing and rebate jobs for Mastercard and American Express to AWS Fargate. Continued developing the Mastercard processor after the migration, refactoring it and adding regression tests.
- Worked with a fellow engineer on the [FIS integration](https://payoutsnetwork.com/industries/banking), a priority for the business. Built configurable single sign-on for partners and implemented the United Airlines integration.
- Fixed a race condition in concurrent jobs by using database transactions.
- Moved production API traffic from EC2 to Kubernetes and worked with the chief security officer on cloud access and network controls for PCI DSS.
- During a CTO transition, helped hire and mentor engineers in Bozeman. Co-designed a hands-on DevOps interview that asked candidates to work with CloudFormation and Terraform.

### <img class="employer-logo" alt="" src="{{ '/assets/employers/composite.svg' | relative_url }}"> [Composite Apps](https://www.compositeapps.net/)
{: #composite-apps}

#### Software Developer <span class="dates">Feb 2016 – Sep 2017</span>

- Built [earthquake alerts](https://kinemetrics.com/news/kinemetrics-provides-business-continuity-solution-for-dubai-municipality/) and evacuation reporting for Kinemetrics. The company reported deploying the system in four Dubai buildings. Presented it to municipal leaders and trained police officers to use it.
- Rebuilt a separate evacuation app’s server and database. Server-sent events showed responders live check-ins as they scanned employee badges.
- Turned emailed studio reports into APIs for Warner Bros. A teammate extended them to Burbank and Leavesden.
- Standardized server setup and database migrations for studio reporting and two other client projects.

## Technical skills

**Languages** · Go, Rust, Python, TypeScript, JavaScript, Java and Elixir.\
**Applications and data** · React, Vue, PostgreSQL and Snowflake.\
**Infrastructure** · AWS, Google Cloud, Kubernetes, Terraform and OpenTofu.

## Open source

- **2026 · Developer tools.** Built [Savior](https://github.com/yourmoodai/savior) for local prompt processing and [agent-stream.nvim](https://github.com/awill1988/agent-stream.nvim) so developers can review a coding agent’s edits inside Neovim. Published Rust libraries for [optional values](https://github.com/awill1988/somelse) and [errors](https://github.com/awill1988/okerrr).
- **2021 · Developer tools.** Added local emulator support to [gcsfs](https://github.com/fsspec/gcsfs/pull/424) and fixed Webpack 5 manifest builds in [Vue CLI](https://github.com/vuejs/vue-cli/pull/6277).
- **2020 · Build tools.** At Foundant, fixed [xdomls](https://github.com/oeo/xdomls/pull/1) so Webpack warnings no longer triggered JSON parsing errors during development. Extended [GDAL](https://github.com/OSGeo/gdal/pull/2965) and [pg_tileserv](https://github.com/CrunchyData/pg_tileserv/pull/72) Docker builds to produce ARM and x86 images.

**Other merged contributions** · [Awesome AI Plugins directory](https://github.com/hashgraph-online/awesome-ai-plugins/pull/683) (2026), [Ory Hydra](https://github.com/ory/hydra/pull/3867) (2024) and [Wazuh](https://github.com/wazuh/wazuh/pull/3729) (2019).

**Proposed patches** · [Ory Pop](https://github.com/ory/pop/pull/7), [FlowPy](https://github.com/onXmaps/FlowPy/pull/1), [IElixir](https://github.com/pprzetacznik/IElixir/pull/60), [Vuetify Loader](https://github.com/vuetifyjs/vuetify-loader/pull/166), [redis-semaphore](https://github.com/swarthy/redis-semaphore/pull/16) and [k8s-auth-client](https://github.com/vimond/k8s-auth-client/pull/2). [Issue reports](https://github.com/search?q=is%3Apublic+is%3Aissue+author%3Aawill1988+-user%3Aawill1988&type=issues) include [Serverless Framework](https://github.com/serverless/serverless/issues/7578). [More projects](https://github.com/awill1988?tab=repositories).

## Education and volunteer service

**University of California, Irvine** · [BA in Drama](https://catalogue.uci.edu/clairetrevorschoolofthearts/departmentofdrama/drama_ba/), minor in Information & Computer Science, 2015.

**[Bozeman Symphonic Choir](https://www.bozemansymphony.org/choir)** · Volunteer member, 2022–present.\
**[Code2College](https://code2college.org/volunteers/)** · Volunteer tutoring instructor, 2022–2023.

## Acting credits <img class="emoji" alt="" src="{{ '/assets/emoji/theater.png' | relative_url }}">
{: #acting-credits}

{% include acting-credits.html %}
