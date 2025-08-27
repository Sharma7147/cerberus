



# 🔐 CERBERUS – Advanced Password Profiler & Wordlist Generator

```
 ██████╗   ███████╗   ██████╗    ██████╗    ███████╗   ██████╗    ██╗   ██╗   ███████╗
██╔════╝   ██╔════╝   ██╔══██╗   ██╔══██╗   ██╔════╝   ██╔══██╗   ██║   ██║   ██╔════╝
██║        ███████╗   ██████╔╝   ██████╔╝   ███████╗   ██████╔╝   ██║   ██║   ███████╗
██║        ██╔══╝     ██╔══██╗   ██╔══██╗   ██╔══╝     ██╔══██╗   ██║   ██║   ╚════██║
╚██████╗   ███████╗   ██║  ██╗   ██████╔╝   ███████╗   ██║  ██╗   ╚██████╔╝   ███████║
 ╚═════╝   ╚══════╝   ╚═╝  ╚═╝   ╚═════╝    ╚══════╝   ╚═╝  ╚═╝    ╚═════╝    ╚══════╝
```

CERBERUS is an **advanced password profiler** for **pentesters, bug bounty hunters, and cybersecurity researchers**.
It generates **custom wordlists** from personal/user information (name, username, email, pets, DOB, etc.), with support for:

✔️ Leetspeak variants
✔️ Reversals
✔️ Breached/common password injection
✔️ Minimum/maximum length filters
✔️ Charset enforcement (require digits, symbols, uppercase, lowercase)


## 📦 Installation

### Clone the repository

```bash
git clone https://github.com/Sharma7147/cerberus.git
cd cerberus
```

### Install dependencies

#### 🔹 On **Kali Linux**

Kali blocks global `pip` installs by default. You have two options:

1. **Using a Virtual Environment (Recommended)**

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

2. **Using pipx (No venv needed)**

```bash
sudo apt install pipx -y
pipx install .
```

Then you can directly run:

```bash
cerberus -h
```

---

#### 🔹 On **Windows**

```powershell
pip install -r requirements.txt
```

---

## 🚀 Usage

You can run CERBERUS in two ways:

### 1. Directly via `run.py` (no installation required)

```bash
# Help
python run.py -h

# Interactive mode
python run.py -i
```

### 2. As a command (after installation with pip or pipx)

```bash
cerberus -h
cerberus -i
```

---

## ⚡ Features

* Generate password list from **names, usernames, emails, pets, DOB, keywords**
* Apply **leet (1337) speak** and reversals
* Enforce rules: require **digit / symbol / upper / lower**
* Control **min/max password length**
* Optionally include **top breached/common passwords**
* Save output automatically to a file

---

## 📄 License

This project is licensed under the **MIT License** – free for personal and commercial use.

---

## ⚠️ Disclaimer

This tool is built for **educational and security testing purposes only**.
The author is **not responsible** for misuse or illegal activity.



