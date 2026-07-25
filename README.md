# 🌐 DNETOOLS v2

> **Professional Network Intelligence Toolkit for Security Researchers, Ethical Hackers, Developers, and System Administrators.**

<div align="center">

# DNETOOLS v2

### Cross-Platform Network Intelligence Toolkit

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python)](https://www.python.org/)
[![License](https://img.shields.io/github/license/AnonymatLabs/dnetools)](https://github.com/AnonymatLabs/dnetools/blob/main/LICENSE)
[![Release](https://img.shields.io/github/v/release/AnonymatLabs/dnetools)](https://github.com/AnonymatLabs/dnetools/releases)
[![Stars](https://img.shields.io/github/stars/AnonymatLabs/dnetools?style=social)](https://github.com/AnonymatLabs/dnetools/stargazers)
[![Forks](https://img.shields.io/github/forks/AnonymatLabs/dnetools?style=social)](https://github.com/AnonymatLabs/dnetools/network/members)
[![Issues](https://img.shields.io/github/issues/AnonymatLabs/dnetools)](https://github.com/AnonymatLabs/dnetools/issues)
[![PyPI](https://img.shields.io/pypi/v/dnetools)](https://pypi.org/)
[![Downloads](https://img.shields.io/pypi/dm/dnetools)](https://pypi.org/)
[![Code Style](https://img.shields.io/badge/code%20style-PEP8-blue)](https://peps.python.org/pep-0008/)
[![Visitors](https://visitor-badge.laobi.icu/badge?page_id=AnonymatLabs.dnetools)](https://github.com/AnonymatLabs/dnetools)

</div>

---

# 🚀 About

**DNETOOLS v2** is a modern Python-based Network Intelligence Toolkit created for:

- Cybersecurity researchers
- Ethical hackers
- Developers
- System administrators
- Network engineers
- Students

The project provides multiple networking and OSINT utilities through a powerful command-line interface.

DNETOOLS is built with a modular architecture that allows easy expansion using providers and independent modules.

---

# ✨ Features

## 🌍 Network Intelligence

- IP Geolocation
- Public IP Detection
- DNS Lookup
- Reverse DNS Lookup
- WHOIS Lookup
- ASN Information

## 🛡 Security Intelligence

- Proxy Detection
- VPN Detection
- TOR Detection
- Hosting Detection
- Security Analysis

## 🧩 Developer Features

- Modular architecture
- Provider system
- Rich CLI interface
- Multiple API fallback
- Python 3 support
- Easy customization

---

# 💻 Supported Platforms

| Platform | Status |
|---|---|
| Android Termux | ✅ Tested |
| Ubuntu | ✅ Supported |
| Kali Linux | ✅ Supported |
| Fedora | ✅ Supported |
| Parrot OS | ✅ Supported |
| Debian | ✅ Supported |
| Arch Linux | ✅ Supported |
| Google Cloud Shell | ✅ Supported |
| macOS | ✅ Supported |
| Windows Python Environment | ✅ Supported |

---

# 📦 Installation

## Clone Repository

```bash
git clone https://github.com/AnonymatLabs/dnetools.git
```

## Enter Directory

```bash
cd dnetools
```

## Install Requirements

```bash
pip install -r requirements.txt
```

## Run

```bash
python dnetools.py --help
```

---

# 🚀 Usage Examples

## Show Help

```bash
python dnetools.py --help
```

## Get Public IP

```bash
python dnetools.py myip
```

Example:

```
✓ Your public IP: xxx.xxx.xxx.xxx
```

## IP Geolocation

```bash
python dnetools.py geo 8.8.8.8
```

## DNS Lookup

```bash
python dnetools.py dns google.com
```

## WHOIS Lookup

```bash
python dnetools.py whois google.com
```

## Reverse DNS

```bash
python dnetools.py reverse 8.8.8.8
```

## Security Check

```bash
python dnetools.py security 8.8.8.8
```

---

# 🏗 Architecture

```
dnetools/

├── core/
│   ├── config.py
│   ├── constants.py
│   ├── models.py
│   ├── output.py
│   └── utils.py
│
├── modules/
│   ├── geo.py
│   ├── dns.py
│   ├── whois.py
│   ├── reverse.py
│   ├── asn.py
│   ├── map.py
│   ├── phone.py
│   ├── wifi.py
│   └── security.py
│
├── providers/
│   ├── base_provider.py
│   ├── ipwhois_provider.py
│   ├── ipapi_provider.py
│   ├── ipinfo_provider.py
│   └── proxycheck_provider.py
│
├── reports/
├── assets/
├── dnetools.py
├── requirements.txt
├── setup.py
├── pyproject.toml
└── README.md
```

---

# 🔌 Providers

Supported providers:

- IPWho.is
- IPAPI
- IPinfo
- ProxyCheck

The toolkit can combine multiple providers to improve reliability.

---

## Trademark

DNETOOLS and Anonymat Labs are trademarks of Anonymat Labs.

Forks and modified versions must not use the official DNETOOLS name,
logo, or branding without permission.

# 🤝 Contributing

Contributions are welcome.

You can contribute by:

- ⭐ Star this repository
- 🍴 Fork this repository
- 🐞 Report bugs
- 💡 Suggest features
- 🔧 Submit pull requests
- 📚 Improve documentation
- ⚡ Optimize performance

---

# 🐞 Bug Reports

When reporting an issue include:

```
Operating System:
Python Version:
DNETOOLS Version:
Error Message:
Steps To Reproduce:
```

Please open an issue with complete information.

---

# 🗺 Roadmap

- ✅ CLI Framework
- ✅ Core Architecture
- ✅ Provider System
- ✅ Public IP Module

Coming soon:

- 🔄 Advanced Geo Engine
- 🔄 DNS Intelligence
- 🔄 WHOIS Engine
- 🔄 Phone Intelligence
- 🔄 WiFi Module
- 🔄 Security Scanner
- 🔄 Report Generator
- 🔄 Plugin System
- 🔄 Web Dashboard

---

# 👨‍💻 Author

## Mr Deh H4ck3r

Developer & Creator of DNETOOLS v2

GitHub:

https://github.com/AnonymatLabs

---

# 🏢 Brand

## Anonymat Labs

Website:

https://anonymatlab.blogspot.com

---

# ❤️ Support

If you like this project:

⭐ Star the repository

🍴 Fork it

🐞 Report issues

💡 Share ideas

🔧 Contribute code

Your support helps grow open-source cybersecurity tools.

---

# ⚠ Disclaimer

DNETOOLS is designed for:

- Educational purposes
- Authorized security testing
- Research
- Defensive cybersecurity

Do not use this software against systems without permission.

The author and contributors are not responsible for illegal use.

---

# 📜 License

MIT License

Copyright © 2026 Anonymat Labs

---

<div align="center">

## Built with ❤️ by Anonymat Labs

⭐ Star • 🍴 Fork • 🤝 Contribute

</div>
