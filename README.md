# Script Collection

> A curated collection of utility scripts for security testing, system administration, and everyday automation tasks.

[![Shell](https://img.shields.io/badge/Shell-19-blue?style=flat-square&logo=gnu-bash&logoColor=white)](#shell)
[![Python](https://img.shields.io/badge/Python-9-green?style=flat-square&logo=python&logoColor=white)](#python)
[![PowerShell](https://img.shields.io/badge/PowerShell-1-purple?style=flat-square&logo=powershell&logoColor=white)](#powershell)

[![GitHub Sponsors](https://img.shields.io/badge/Sponsor-❤-ea4aaa?style=flat-square&logo=github-sponsors&logoColor=white)](https://github.com/sponsors/anantshri)
[![Buy Me A Coffee](https://img.shields.io/badge/Buy%20Me%20A%20Coffee-☕-ffdd00?style=flat-square&logo=buy-me-a-coffee&logoColor=black)](https://buymeacoffee.com/anantshri)

---

## Table of Contents

- [Shell](#shell) — Bash/Shell scripts
- [Python](#python) — Python utilities
- [PowerShell](#powershell) — PowerShell experiments
- [macOS](#macos) — macOS-specific tools
- [Misc](#misc) — One-off utilities
- [Found Online](#found-online) — Curated external scripts
- [Polyglot](#polyglot) — Cross-environment scripts

---

## Shell

Bash and shell scripts for various automation tasks.

| Script | Description |
|:-------|:------------|
| `check_bulk_response.sh` | Checks response for a specific URL against a list of domains |
| `claude-local` | Launch Claude Code with Ollama backend (auto-discovers local network → Tailscale → localhost) |
| `claude-x` | Launch Claude Code with external API providers (Z.ai, OpenAI, DeepSeek, Groq, etc.) |
| `dec2hex` / `hex2dec` | Converts between hexadecimal and decimal |
| `doh_query.sh` | DNS-over-HTTPS query validator (CloudFlare, Google, DNS0.eu, Quad9) |
| `dvcsfinder.sh` | Detects exposed version control files (.git, .svn, etc.) |
| `genymotion.sh` | Start/stop Genymotion VMs via command line |
| `gitrebase` | Sync fork with upstream without creating merge commits |
| `http` | Portable HTTP server with multi-language fallback |
| `ip` | Cross-platform IP address display (IPv4/IPv6) with interface names |
| `isolated_window` | Launch URL in Chrome/Chromium as isolated app window |
| `loop.sh` | Execute command for each line in a file with prefix/suffix |
| `ollama` | Drop-in Ollama wrapper with automatic instance selection |
| `pdfencrypt` | Encrypt PDF files with user/owner passwords (Ghostscript) |
| `pdflinkchecker.sh` | Extract URLs from PDF and verify HTTP status codes |
| `publicip.sh` | Display public IP address |
| `vagrant_supercharged` | Enhanced Vagrant wrapper script |
| `websites.sh` | Launch websites as Chrome app containers |
| `wp-user-enum.sh` | WordPress username enumeration |
| `zipclean` | Remove `.DS_Store` and `__MACOSX` from zip archives |

---

## Python

Python utilities for encoding, security research, and data processing.

| Script | Description |
|:-------|:------------|
| `char_to_num.py` | Convert string to single digit via character-to-number reduction |
| `custom_enc_decoder.py` | Custom encoder/decoder with configurable word swaps |
| `hash_generator.py` | Generate hashes in multiple formats |
| `ip_dword.py` | Convert IP addresses to DWORD and various encoded formats |
| `palindrome_in_year.py` | Find all palindrome dates in a given year |
| `rotme.py` | Apply ROT1-26 cipher variations to a string |
| `shodan_hostenum.py` | Shodan hostname enumeration *(requires API key)* |
| `wadl_statistics_reporter.py` | Count resources, methods, and parameters in WADL files |
| `wordpress_attachment.py` | WordPress attachment ID bruteforce |

---

## PowerShell

PowerShell scripts and experiments.

| Script | Description |
|:-------|:------------|
| `http.ps1` | Simple HTTP file server on `localhost:8000` |

---

## macOS

Scripts specifically for macOS.

| Script | Description |
|:-------|:------------|
| `codesign_remover.sh` | Remove code signing from applications in `~/Applications` |

---

## Misc

Miscellaneous utilities and one-off scripts.

| Script | Description |
|:-------|:------------|
| `ip.bat` | Windows batch script for displaying IP addresses |
| `php_func_enumerator.php` | Enumerate disabled PHP functions for code execution |
| `resource_abusive_bot_blocking.htaccess` | Block abusive bots via htaccess rules |
| `script_kiddie_blocker.htaccess` | Block common script kiddie attacks via htaccess |

---

## Found Online

Useful scripts collected from various online sources.

| Script | Description | Source |
|:-------|:------------|:-------|
| `duckduckbot-fetch` | Fetch URLs with DuckDuckGo bot user-agent | — |
| `extract` | Universal archive extraction (zip, rar, tar, gz, 7z, etc.) | [DigitalOcean](https://www.digitalocean.com/community/tutorials/an-introduction-to-useful-bash-aliases-and-functions) |
| `gc` | Git clone with automatic directory structure | [git-dolly](https://github.com/op/git-dolly) |
| `googlebot-fetch` | Fetch URLs with Googlebot user-agent | — |

---

## Polyglot

Scripts that work across multiple environments.

| Script | Description |
|:-------|:------------|
| `http.ps1` | HTTP server (PowerShell) |

---

## Claude Scripts Setup

### claude-local

Launches Claude Code with the best available Ollama backend. Automatically discovers and connects to your AI server.

**Discovery priority:**
1. AI Server via local network (by hostname)
2. AI Server via Tailscale (MagicDNS, then IP lookup)
3. Local Ollama (localhost)

**Setup:**

```bash
# Add to ~/.bashrc or ~/.zshrc
export AISERVER_HOSTNAME="aiserver.local"      # Local network hostname
export AISERVER_LOCAL_IP="192.168.1.100"       # Fallback if .local doesn't resolve
export AISERVER_TAILSCALE_NAME="aiserver"      # Tailscale machine name
```

**Usage:**

```bash
claude-local                    # Auto-discover and launch
claude-local -s                 # Show discovery status
claude-local -a                 # Force AI Server
claude-local -m qwen3:32b       # Use specific model
```

### claude-x

Launches Claude Code with external API providers (Z.ai GLM, OpenAI, DeepSeek, Groq, etc.).

**Setup:**

```bash
# Run once to create config file
claude-x -l

# Edit config to add your API keys
# Config location: ~/.config/claude-x/config
```

Or copy the example config:

```bash
mkdir -p ~/.config/claude-x
cp Shell/claude-x.config.example ~/.config/claude-x/config
chmod 600 ~/.config/claude-x/config
# Edit and add your API keys
```

**Built-in providers:** `zai`, `openai`, `deepseek`, `groq`, `together`, `mistral`, `anthropic`

**Usage:**

```bash
claude-x -l                     # List providers and status
claude-x -p zai                 # Use Z.ai with default model
claude-x -p openai -m gpt-4     # Use OpenAI with specific model
```

---

## Support

If you find these scripts useful, consider supporting the project:

[![GitHub Sponsors](https://img.shields.io/badge/Sponsor_on_GitHub-❤-ea4aaa?style=for-the-badge&logo=github-sponsors&logoColor=white)](https://github.com/sponsors/anantshri)
[![Buy Me A Coffee](https://img.shields.io/badge/Buy_Me_A_Coffee-☕-ffdd00?style=for-the-badge&logo=buy-me-a-coffee&logoColor=black)](https://buymeacoffee.com/anantshri)

---

## License

These scripts are provided as-is for educational and utility purposes.

## Author

**Anant Shrivastava** — [https://anantshri.info](https://anantshri.info)
