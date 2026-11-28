---
layout: resume
full_name: Adam Williams
title: Staff Software Engineer
location: Bozeman, Montana
intro: I’m a staff software engineer focused on security, compliance, and site reliability. At Arro Finance, I build banking services and operate the infrastructure behind them. At onX, I helped run the identity systems that gave subscribers access to the maps they paid for, across a platform used by millions of adventurers.
---

## Professional experience
{: #experience tabindex="-1"}

### <img class="employer-logo" alt="" src="{{ '/assets/employers/arro.png' | relative_url }}"> Arro Finance
{: #arro-finance}

#### Staff Software Engineer <span class="dates">Jan 2026 – present</span>

- Led engineering’s SOC 2 Type II audit work. Added peer approval for infrastructure changes, tracked fixes in Vanta and checked its AWS coverage. The independent auditor issued an unqualified opinion with no exceptions noted.
- Replaced Datadog with self-hosted Grafana and OpenTelemetry on AWS. Engineers could check payment-provider health and get alerts when workflows stalled or monitoring went silent.
- Secured internal tools with AWS Verified Access and mapped AWS permissions to Google Workspace groups. Coordinated penetration-test fixes with engineering and refined mobile protections with Customer Support. The independent tester verified that all high-severity findings had been resolved.
- Built credit-line, statement and ledger services. Automated balance checks across three systems. Implemented the engineering director’s design to deliver banking changes to Snowflake.
- Rebuilt Arro’s AI assistant in Rust on Amazon Bedrock. Engineers could release a prompt change without redeploying the service and inspect which tools the assistant used to answer a customer.
- Proposed reusing the [Arro Credit Builder](https://www.arrofinance.com/creditbuilder) web signup in the mobile app. Built the handoff with the team so one flow could skip steps an applicant had completed.

### <img class="employer-logo" alt="" src="{{ '/assets/employers/onx.png' | relative_url }}"> onXmaps
{: #onxmaps}

#### Senior Software Engineer I, Core Services (Identity) <span class="dates">May 2023 – Dec 2025</span>

Built the access controls that let onX Fish subscribers use [one Midwest membership](https://www.onxmaps.com/blog/onx-officially-introduces-onx-fish) across Minnesota, Wisconsin and Michigan.

- Worked with Growth on directing users to the appropriate sign-in provider. Automated permission changes when employee accounts were opened, suspended or restored.
- Built authx, an OAuth command-line tool that dozens of onX engineers used daily to sign in from their terminals.

#### Senior Software Engineer I, Backcountry <span class="dates">Apr 2021 – Apr 2023</span>
{: #onx-backcountry tabindex="-1"}

- As Backcountry’s founding backend engineer, built the SNOTEL pipeline and API that let skiers tap a map pin for [snowpack history](https://www.onxmaps.com/backcountry/app/features/snotel-map) at more than 800 mountain stations. The same service supplied snow observations to Hunt and [Offroad](https://www.onxmaps.com/offroad/app/features/snow-mode).
- Represented Backcountry on [snap-to-trail routing](https://www.onxmaps.com/backcountry/app/features/hike-planner) with the Geospatial Datastore and Routing & Navigation teams. Proposed a separate trail network for hikers, added its import query to Offroute and expanded the scheduled build from Montana to all 50 states and DC.
- Worked with geospatial specialists on a map layer showing [four levels of avalanche terrain exposure](https://www.onxmaps.com/blog/onx-backcountry-launches-avalanche-terrain-exposure-scale) for trip planning. Set up a local map datastore where engineers could test data changes on their laptops.

### <img class="employer-logo" alt="" src="{{ '/assets/employers/foundant.webp' | relative_url }}"> Foundant Technologies
{: #foundant-technologies tabindex="-1"}

#### Senior Software Engineer <span class="dates">Oct 2020 – Apr 2021</span>

- Built a common Webpack toolchain for four Vue applications. All four could adopt progressive web app support by updating one dependency.
- Extended a teammate’s Module Federation prototype to give shared components their own release pipeline. An Accounting engineer then added a menu destination in one place for both Accounting and Foundant User.
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

### <img class="employer-logo" alt="" src="{{ '/assets/employers/composite.svg' | relative_url }}"> Composite Apps
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
- **2021 · Local testing and web builds.** Added emulator support to [gcsfs](https://github.com/fsspec/gcsfs/pull/424) so developers could test against local storage. Fixed how [Vue CLI](https://github.com/vuejs/vue-cli/pull/6277) generates web app manifests under Webpack 5.
- **2020 · Geospatial tooling.** Extended [GDAL](https://github.com/OSGeo/gdal/pull/2965) and [pg_tileserv](https://github.com/CrunchyData/pg_tileserv/pull/72) Docker builds to produce ARM and x86 images.

**Other merged contributions** · [Awesome AI Plugins directory](https://github.com/hashgraph-online/awesome-ai-plugins/pull/683) (2026), [Ory Hydra](https://github.com/ory/hydra/pull/3867) (2024), [xdomls](https://github.com/oeo/xdomls/pull/1) (2020) and [Wazuh](https://github.com/wazuh/wazuh/pull/3729) (2019).

**Proposed patches** · [Ory Pop](https://github.com/ory/pop/pull/7), [FlowPy](https://github.com/onXmaps/FlowPy/pull/1), [IElixir](https://github.com/pprzetacznik/IElixir/pull/60), [Vuetify Loader](https://github.com/vuetifyjs/vuetify-loader/pull/166), [redis-semaphore](https://github.com/swarthy/redis-semaphore/pull/16) and [k8s-auth-client](https://github.com/vimond/k8s-auth-client/pull/2). [Issue reports](https://github.com/search?q=is%3Apublic+is%3Aissue+author%3Aawill1988+-user%3Aawill1988&type=issues) include [Serverless Framework](https://github.com/serverless/serverless/issues/7578). [More projects](https://github.com/awill1988?tab=repositories).

## Education and volunteer service

**University of California, Irvine** · BA in Drama, minor in Information & Computer Science, 2015.

**Bozeman Symphonic Choir** · Volunteer member, 2022–present.\
**Code2College** · Volunteer tutoring instructor, 2022–2023.

## Acting credits <img class="emoji" alt="" src="{{ '/assets/emoji/theater.png' | relative_url }}">
{: #acting-credits}

**Montana TheatreWorks** · *White Christmas* (ensemble, in rehearsal for December 2026), *The Music Man* (chorus, 2026) and *Cabaret* (Ernst Ludwig, 2025). **Shane Lalani Center for the Arts** · [*RENT* (Benny, 2026)](https://www.theshanecenter.org/latest-news/meetthecastandcrewofrent-f6t9h).
