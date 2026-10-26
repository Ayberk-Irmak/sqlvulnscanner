# sqlvulnscanner

A small, educational dork-based SQL-injection *reconnaissance* helper. It collects
candidate URLs from a search engine for a given dork and flags pages that leak a SQL
syntax error, as a first-pass indicator worth manual review.

> ⚠️ **Authorized use only**
>
> This tool can reach third-party websites. Testing systems you do not own or are not
> explicitly authorized to assess is **illegal** in most jurisdictions. The scanner will
> not run until you confirm authorization (interactive prompt, or the `--authorized`
> flag). You are solely responsible for how you use it.

## Scope & limitations

- This is a lightweight learning project — a single error-string heuristic, not a real
  SQLi engine. Expect false positives and false negatives.
- Google is currently unsupported (bot protection); Bing is used instead.
- No exploitation is performed — it only flags candidate URLs for manual review.

## For real engagements, use reconowl

For authorized penetration testing I maintain a far more capable, properly scoped tool:

### 👉 [**reconowl**](https://github.com/Ayberk-Irmak/reconowl)
A recon → scan → report CLI orchestrator (native checks + nmap/nuclei/httpx/sqlmap)
with evidence-based confirmation, CVSS/SARIF reporting and an "authorized use only"
model. Prefer it over this script for anything beyond learning.

## Usage

```bash
git clone https://github.com/Ayberk-Irmak/sqlvulnscanner.git
cd sqlvulnscanner
pip install -r requirements.txt

# You will be asked to confirm authorization before scanning:
python sqlvulnscan.py -d "inurl:php?id=" -e bing -p 2 -t 4

# Non-interactive (CI / scripted) — only if you are authorized:
python sqlvulnscan.py -d "inurl:php?id=" -e bing -p 2 -t 4 --authorized
```

| Flag | Meaning |
|------|---------|
| `-d`, `--dork` | Dork query |
| `-e`, `--engine` | `bing` (google falls back to bing) |
| `-p`, `--pages` | Pages of results to fetch |
| `-t`, `--threads` | Worker threads |
| `--authorized` | Skip the interactive authorization prompt |

## License

MIT

## Author

**Ayberk Irmak** — [@Ayberk-Irmak](https://github.com/Ayberk-Irmak) · ayberk.sec@proton.me
