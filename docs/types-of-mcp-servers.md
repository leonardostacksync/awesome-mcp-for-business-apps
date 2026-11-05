# Types of MCP servers

| Type | Where it runs | Sign-in | Who maintains it | Good for | Watch out for |
|---|---|---|---|---|---|
| **Vendor-hosted** | The vendor's cloud, at a remote endpoint | Usually OAuth | The vendor | Business users, governed access | Scope is limited to what the vendor exposes. Status can be beta |
| **Vendor-local** | Your machine | Your local session or key | The vendor | Developers working on the app | Often a developer tool, not a data server |
| **Vendor open source** | Your machine or your infrastructure | Credentials you provide | The vendor, in the open | Databases and self-hosted setups | You run and secure it |
| **Community** | Your machine or a host you pick | Whatever the author built | Someone else | Prototyping, niches with no official server | Maintenance, security review, abandoned projects |
| **Integration layer** | The provider's cloud | OAuth | The provider | Work across several apps | Depends on the connectors it supports |

## Transport in one line

A remote server speaks over HTTP (often called streamable HTTP). A local server usually speaks over stdio, started by your client as a subprocess.

## Which to trust with what

- **Sandbox or read-only data:** anything, after a quick review.
- **Real business data:** vendor-hosted or an integration layer with OAuth, a least-privilege role, approvals and logs.
- **Community servers on real data:** only after you read the code, pin a version and run it with a read-only identity.
