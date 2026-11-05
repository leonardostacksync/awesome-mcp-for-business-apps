# Contributing

Add or correct an entry in `data/servers.json`, then run:

```bash
python scripts/build_readme.py
python -m unittest discover -s tests -v
```

Rules for an entry:

- Name the vendor and the server. **Do not add links** to other vendors' pages. Say how to find it ("search the vendor name plus the server name") if needed.
- Fill every field: category, vendor, name, kind, covers, auth, notes.
- Say what you could confirm and where sources disagree. Avoid dates, endpoints and prices, which change.
- Mark a community server as community.
- No rankings, benchmarks or superlatives.
- Update the `checked` date in the data file when you re-verify entries.
