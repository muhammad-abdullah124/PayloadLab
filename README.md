# PayloadLab 🛠️

**PayloadLab** is a modular payload generator designed to assist penetration testers and security researchers in generating customized web exploitation payloads for various attack vectors including:

- Command Injection (CMDi)
- SQL Injection (SQLi)
- Cross-Site Scripting (XSS)

---

## 🔧 Features

- Pre-built payloads for XSS, SQLi, and CMDi attacks.
- Burp Suite integration module.
- Payload mutation and encoding modules.
- CLI interface for ease of use.
- Easily extensible and customizable.

---

## 📁 Project Structure

```
PayloadLab/
├── cli.py                # CLI entry point
├── main.py               # Core logic and runner
├── modules/              # Exploit logic by attack type
│   ├── burp.py
│   ├── cmdi.py
│   ├── encoder.py
│   ├── mutator.py
│   ├── sqli.py
│   └── xss.py
├── payloads/             # JSON payload templates
│   ├── cmdi_payloads.json
│   ├── sqli_payloads.json
│   └── xss_payloads.json
└── README.md             # Documentation
```

---

## ⚙️ Installation

```bash
git clone https://github.com/muhammad-abdullah124/PayloadLab.git
cd PayloadLab
python3 -m venv venv
source venv/bin/activate            # For Linux/macOS
.\\venv\\Scripts\\Activate.ps1      # For Windows (PowerShell)
pip install -r requirements.txt
```

> ⚠️ Ensure you have Python 3.8+ installed.

## 🚀 Usage

To launch PayloadLab via CLI:

```bash
python cli.py --type xss --encode base64
```

---

### Available Options:

| Argument      | Description                           |
|---------------|---------------------------------------|
| `--type`      | Type of payload: `xss`, `sqli`, `cmdi`|
| `--mutate`    | Apply mutation techniques             |
| `--encode`    | Encode the payload (e.g., `base64`)   |
| `--output`    | Save output to a file                 |

### Example:

```bash
python cli.py --type sqli --mutate --encode url
```

---

## 📄 License

[MIT License](LICENSE)
