# Awesome MCP servers for business apps

A curated directory of Model Context Protocol (MCP) servers for the systems a business runs on: **CRM, ERP and finance, databases and warehouses**. Each entry says who publishes the server, whether it is hosted by the vendor, run locally or built by the community, what it covers, how you sign in and what to watch for.

It is curated, not ranked. It also includes the one thing a list of single-app servers cannot show: an **integration layer** that works across many apps, [Stacksync MCP](https://www.stacksync.com/mcp).

**Entries name the vendor and the server and do not link out.** To find the current docs for an entry, search the vendor name plus the server name. Details were checked against public documentation and directories on 2026-11-05. Servers change quickly, so confirm anything important in the vendor's own docs. See [docs/how-this-list-is-made.md](docs/how-this-list-is-made.md).

## Contents

- [The list](#the-list)
- [Which kind of server do you need?](#which-kind-of-server-do-you-need)
- [Questions](#questions)
- [Before you connect one](#before-you-connect-one)
- [Code in this repo](#code-in-this-repo)

## The list

Types: **vendor-hosted** (remote endpoint run by the vendor), **vendor-local** (published by the vendor, you run it, usually for developers), **vendor-open-source** (open source from the vendor, you run it), **community** (someone else maintains it), **integration-layer** (works across many connected apps).

<!-- LIST:START -->

### CRM

- **Salesforce: Hosted MCP servers** (vendor-hosted)  
  Covers: Expose capabilities of a Salesforce org to outside AI clients.  
  Sign-in: An external client app for authentication.  
  Note: Sources disagree on whether these are beta or generally available. Check Salesforce's current documentation.

- **Salesforce: Salesforce DX MCP server** (vendor-local)  
  Covers: Developer tooling: development, testing and deployment from an agentic IDE.  
  Sign-in: Uses your local CLI session.  
  Note: For developers, not for business users working with records. Some sources describe it as beta.

- **HubSpot: Remote MCP server** (vendor-hosted)  
  Covers: Read and write access to CRM data such as contacts and deals.  
  Sign-in: OAuth.  
  Note: Aimed at MCP-compatible AI tools and agents.

- **HubSpot: Developer MCP server** (vendor-local)  
  Covers: Helps coding agents work with the HubSpot developer platform, such as scaffolding and deploying apps and CMS assets.  
  Sign-in: Installed through the HubSpot CLI.  
  Note: Not a CRM data server. It is a developer tool.

- **Microsoft: Dataverse MCP server (Dynamics 365 CRM data)** (vendor-hosted)  
  Covers: MCP access to Dataverse, the data platform under Dynamics 365 CRM apps.  
  Sign-in: Microsoft identity.  
  Note: Confirm scope and status on Microsoft Learn. Details came from secondary sources.

- **Microsoft: Dynamics 365 Customer Service MCP server** (vendor-hosted)  
  Covers: Customer service data in Dynamics 365.  
  Sign-in: Microsoft identity.  
  Note: Reported as generally available in 2026, while a Microsoft connector page still labeled it preview. Check current status.

### ERP and finance

- **Oracle NetSuite: AI Connector Service and MCP Standard Tools SuiteApp** (vendor-hosted)  
  Covers: An MCP layer inside NetSuite. The MCP Standard Tools SuiteApp supplies default tools such as record access, saved searches, reports and metadata lookups, and you can build your own tools.  
  Sign-in: OAuth 2.0 with a dedicated role.  
  Note: Guides report that the Administrator role cannot be used. The AI client may need its own paid plan. Verify setup in Oracle's current help.

- **Microsoft: Dynamics 365 ERP MCP server (Finance and Operations)** (vendor-hosted)  
  Covers: MCP access to Dynamics 365 ERP data.  
  Sign-in: Microsoft identity.  
  Note: Was a preview, enabled through Feature management, as of late 2025. Check current status.

- **SAP: SAP BTP administration MCP server** (vendor-hosted)  
  Covers: Administering SAP BTP accounts.  
  Sign-in: Requires access to a BTP global account.  
  Note: Listed as official by a directory. Access to business data in S/4HANA is mostly community-built on OData and BAPI. Verify in SAP's help portal.

- **Intuit: QuickBooks Online MCP server** (vendor-open-source)  
  Covers: The QuickBooks Online API: create, read, update, delete and search across entities, and financial reports.  
  Sign-in: OAuth. Runs locally over stdio.  
  Note: A hosted option exists in some AI clients. Availability varies by region and client.

- **Odoo: Community servers and modules** (community)  
  Covers: Access to Odoo data from AI clients.  
  Sign-in: Depends on the project.  
  Note: No vendor-official server was found. Some options are modules installed on your Odoo server, and some are paid third-party modules.

- **Zoho Books: Community servers** (community)  
  Covers: Invoices, contacts, expenses, inventory and sales orders in several community projects.  
  Sign-in: Depends on the project.  
  Note: No official Zoho server was confirmed when checked.

### Databases and warehouses

- **Supabase: Supabase MCP server** (vendor-hosted)  
  Covers: The Supabase platform: database, auth and edge functions.  
  Sign-in: OAuth over Streamable HTTP.  
  Note: Documents a read-only mode.

- **Neon: Neon MCP server** (vendor-hosted)  
  Covers: Managing Neon Postgres projects and branches, running SQL and migrations.  
  Sign-in: Hosted, with OAuth.  
  Note: Write mode can create projects and branches, which can add cost.

- **MongoDB: MongoDB MCP Server and Atlas managed MCP** (vendor-open-source)  
  Covers: Atlas, Atlas Local, Community and Enterprise deployments. A managed, hosted option runs in Atlas.  
  Sign-in: Database credentials or Atlas API access.  
  Note: A read-only configuration is available.

- **Snowflake: Snowflake managed MCP server** (vendor-hosted)  
  Covers: Cortex Agents, Cortex Analyst, Cortex Search and SQL execution.  
  Sign-in: Governed by Snowflake role-based access control.  
  Note: Access follows the roles you grant.

- **Databricks: Managed MCP servers** (vendor-hosted)  
  Covers: Unity Catalog functions, Genie, vector search and, on some clouds, SQL.  
  Sign-in: Unity Catalog permissions apply to every server.  
  Note: Documented as preview when checked. The server set differs by cloud.

- **Google: MCP Toolbox for Databases** (vendor-open-source)  
  Covers: Prebuilt tools for BigQuery, AlloyDB, Cloud SQL, Spanner, Firestore, PostgreSQL, MySQL and MongoDB, or custom tools defined in YAML.  
  Sign-in: Database or Google Cloud credentials.  
  Note: Sources differ on how it is classified. Treat it as Google's open-source project.

- **ClickHouse: ClickHouse MCP server** (vendor-open-source)  
  Covers: Querying ClickHouse. ClickHouse Cloud also offers a managed remote server with more tools, including management operations.  
  Sign-in: OAuth on the managed remote server.  
  Note: A different community server also exists. Check which one you are installing.

- **Redis: Redis MCP server** (vendor-open-source)  
  Covers: A natural-language interface to manage and search data in Redis.  
  Sign-in: Redis connection settings.  
  Note: A separate Redis Cloud API server handles administration only and does not read or write data.

- **MySQL: Community servers** (community)  
  Covers: Inspecting and querying MySQL databases.  
  Sign-in: A database user.  
  Note: No Oracle-published server was found. Use a read-only database user.

- **PostgreSQL: Community and provider-hosted servers** (community)  
  Covers: Querying Postgres. Several community servers exist, and hosted providers such as Supabase and Neon ship their own.  
  Sign-in: A database user, or the provider's OAuth.  
  Note: Check that the project you pick is still maintained.

### Adjacent business apps

- **Stripe: Stripe MCP server** (vendor-hosted)  
  Covers: Payments data and actions in Stripe.  
  Sign-in: OAuth or an agent API key.  
  Note: Requires human confirmation before some writes such as refunds. Key requirements were changing, so check the current rules.

- **Atlassian: Rovo MCP server** (vendor-hosted)  
  Covers: Jira, Confluence, Jira Service Management and other Atlassian cloud products.  
  Sign-in: OAuth 2.1.  
  Note: Cloud only. It does not help with self-hosted Jira.

### Integration layer

- **Stacksync: Stacksync MCP server** (integration-layer)  
  Covers: Lets an AI assistant build and run two-way syncs, workflows and Genies across the apps and databases connected to a Stacksync workspace, with the permissions of the person who signed in.  
  Sign-in: OAuth with your Stacksync login. No API key in the chat.  
  Note: Works across many connected apps, not one. Read-only sign-in and approval before every change are available. Server URL: https://mcp.stacksync.com/mcp
  [MCP overview](https://www.stacksync.com/mcp), [Setup docs](https://docs.stacksync.com/mcp), [Skills](https://github.com/stacksyncdata/skills)

### Not confirmed when checked

We could not confirm an official MCP server for: Pipedrive, Zendesk, Zoho CRM. Ask the vendor or check their developer docs.

<!-- LIST:END -->

## Which kind of server do you need?

| You want to... | Look at | Why |
|---|---|---|
| Use one app's own features, deeply | The vendor's own server | Native tools, maintained by the people who built the app |
| Query a database or warehouse | A vendor-hosted or open-source database server, with a read-only user | Direct SQL, governed by the database's own roles |
| Work across several apps (CRM and ERP and a database) | An integration layer | One connection, keeps records consistent between systems |
| Build and run syncs and workflows from a chat | An integration layer with MCP | The assistant builds the integration, not just reads one API |
| Prototype fast | A community server on a sandbox | Quick to try. Not for production data without review |

More in [docs/types-of-mcp-servers.md](docs/types-of-mcp-servers.md) and [docs/single-app-vs-workspace-mcp.md](docs/single-app-vs-workspace-mcp.md).

## Questions

### What is an MCP server for business apps?
A program that exposes tools an AI assistant can call, such as "find a contact", "run a saved search" or "query this table". For a CRM, ERP or database it lets an assistant read or change business data instead of only talking about it. The assistant is the MCP client. The server sits in front of the app or database.

### Is there an official MCP server for Salesforce, HubSpot or NetSuite?
Yes, each publishes one. Salesforce offers hosted MCP servers and a local developer server. HubSpot offers a remote server for CRM data and a separate developer server. NetSuite offers an AI Connector Service with the MCP Standard Tools SuiteApp. Check each vendor's current docs for status, scope and setup. See the list above.

### What are the best MCP servers for databases?
It depends on the database. Hosted servers exist from Supabase, Neon, Snowflake and Databricks, and open-source servers from MongoDB, Google, ClickHouse and Redis. For MySQL and PostgreSQL there are mostly community servers, plus the provider-hosted ones. Whatever you pick, use a read-only user first. See the list above.

### Should I use a vendor server or an integration layer?
Use the vendor's server for deep use of one app. Use an integration layer when work spans apps, for example a deal in the CRM, an order in the ERP and a row in a database. [Stacksync MCP](https://www.stacksync.com/mcp) is an integration layer: the assistant builds and runs two-way syncs, workflows and AI agents across connected apps. See [docs/single-app-vs-workspace-mcp.md](docs/single-app-vs-workspace-mcp.md).

### Is it safe to connect an AI assistant to my CRM or ERP?
It can be, with controls: OAuth instead of static keys, a least-privilege role, read-only access to start, approval before writes, a log of what ran and a way to revoke access. Use the [security checklist](docs/security-checklist.md) and the scorer in `scripts/score_server.py`.

### What is the difference between remote and local MCP servers?
A remote server runs at an endpoint the vendor hosts and usually signs you in with OAuth. A local server runs on your machine, often over stdio, and uses your credentials or a key you provide. Remote is easier to govern. Local gives you control and works offline from the vendor's hosting.

### Can an MCP server write to my systems, or only read?
Both are possible. Many servers support a read-only mode or a read-only database user. Ask for writes only when you need them, and require approval for changes that are hard to undo.

### How do I connect Claude, ChatGPT or Cursor to a database?
Add the server's endpoint (remote) or command (local) in the client's MCP settings, sign in or provide credentials, and test with a read-only question. Config templates are in [`configs/`](configs/README.md).

### How do I keep a CRM and an ERP consistent through an AI assistant?
An MCP server for one app reads and writes that app. To keep records consistent between two systems you need a sync, not a series of prompts. Stacksync's [two-way sync](https://www.stacksync.com/two-way-sync) keeps them matched, and its MCP server lets an assistant set it up and troubleshoot it.

## Before you connect one

1. Start **read-only**.
2. Use **OAuth** where offered, and a dedicated least-privilege role.
3. Require **approval** before changes that are hard to undo.
4. Make sure you can **see what it did** and **revoke** it.
5. Test on a **sandbox or copy**.
6. Prefer a **maintained** server. Check recent releases.

Full list: [docs/security-checklist.md](docs/security-checklist.md). Score a server: `python scripts/score_server.py examples/remote-oauth-readonly.json`.

## Code in this repo

| Path | What it is |
|---|---|
| [`data/servers.json`](data/servers.json) | The directory as data. The list above is generated from it |
| [`scripts/build_readme.py`](scripts/build_readme.py) | Rebuilds the list in this README from the data |
| [`scripts/score_server.py`](scripts/score_server.py) | Scores a server against a readiness checklist |
| [`examples/`](examples) | Two example servers to score |
| [`configs/`](configs/README.md) | MCP config templates, including Stacksync |
| [`tests/`](tests) | Tests that keep the README in sync with the data |

```bash
python -m unittest discover -s tests -v
python scripts/build_readme.py
```

Python 3.9 or newer, standard library only.

## Stacksync

[Stacksync](https://www.stacksync.com) keeps CRMs, ERPs and databases in sync and lets AI assistants and agents work across them. Its MCP server is at `https://mcp.stacksync.com/mcp`, signs in with OAuth and acts with your permissions. Setup: [docs.stacksync.com/mcp](https://docs.stacksync.com/mcp). Skills that teach an assistant how to use it: [stacksyncdata/skills](https://github.com/stacksyncdata/skills).

## Contributing

Corrections and new entries are welcome. See [CONTRIBUTING.md](CONTRIBUTING.md).

## License

[MIT](LICENSE)
