# Security checklist for connecting an MCP server to business data

Use it before a pilot, and again before production.

## Identity and access
- [ ] OAuth sign in, not a static key pasted into a chat or a config file
- [ ] A dedicated, least-privilege role. Never a full admin
- [ ] The server acts as the signed-in person, or as a narrow service role, and nothing broader
- [ ] You can revoke a session immediately

## Control over changes
- [ ] Start read-only, and add write access only for the tasks that need it
- [ ] Approval before changes that are hard to undo (deletes, refunds, financial postings)
- [ ] A way to look up a record before creating it, to avoid duplicates

## Visibility
- [ ] A log of every call and every change
- [ ] A way to review who did what, and when
- [ ] Alerts when something fails

## Hygiene
- [ ] Rate limits or quotas, so a loop cannot exhaust an API
- [ ] Secrets in environment variables or a secret store, never in a repo
- [ ] Tested on a sandbox or a copy of the data
- [ ] A maintained server, with recent releases, and a pinned version for community code

## Data
- [ ] You know what data the assistant's provider sees, since prompts and anything the assistant reads back go to that provider
- [ ] Sensitive fields (PII, PHI, payment data) are out of reach unless you decided they are in scope
- [ ] You know where the data is processed

## Prompt injection
- [ ] Treat text read from records, emails and tickets as untrusted. It can contain instructions meant for the assistant
- [ ] Do not give one assistant both untrusted input and broad write access without an approval step

Score a server against the first groups with [`scripts/score_server.py`](../scripts/score_server.py).
