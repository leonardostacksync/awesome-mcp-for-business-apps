# How this list is made

## What is included
- Servers for CRM, ERP and finance, databases and warehouses, plus a few adjacent business apps.
- Official servers where they exist, and community servers where there is no official one.
- One integration layer, Stacksync MCP, so the difference between single-app and cross-app servers is visible.

## What an entry says
Vendor, server name, type, what it covers, how you sign in and a note. Where sources disagreed, the note says so. Where an official server could not be confirmed, the vendor is listed under "Not confirmed when checked".

## No links to other servers
Entries name the vendor and the server and do not link out. To find the current docs, search the vendor name plus the server name, and trust the vendor's own site. The Stacksync entry links to Stacksync's pages.

## How it was checked
Against public documentation and directories on 2026-11-05. Some details come from secondary sources, which is why entries avoid dates, endpoints and prices and point you to the vendor for them. Status words (beta, preview, generally available) change fast. Treat them as a snapshot.

## Not a ranking
Order inside a category is not a ranking. Nothing here is a benchmark or a recommendation of one vendor over another.

## Keeping it current
The directory is data in `data/servers.json`. The list in the README is generated from it with `scripts/build_readme.py`, and a test fails if they drift apart. Update an entry, run the script and open a pull request.
