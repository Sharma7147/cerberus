---

# 🔐 CERBERUS – Advanced Password Profiler & Wordlist Generator

```
 ██████╗   ███████╗   ██████╗    ██████╗    ███████╗   ██████╗    ██╗   ██╗   ███████╗
██╔════╝   ██╔════╝   ██╔══██╗   ██╔══██╗   ██╔════╝   ██╔══██╗   ██║   ██║   ██╔════╝
██║        ███████╗   ██████╔╝   ██████╔╝   ███████╗   ██████╔╝   ██║   ██║   ███████╗
██║        ██╔══╝     ██╔══██╗   ██╔══██╗   ██╔══╝     ██╔══██╗   ██║   ██║   ╚════██║
╚██████╗   ███████╗   ██║  ██╗   ██████╔╝   ███████╗   ██║  ██╗   ╚██████╔╝   ███████║
 ╚═════╝   ╚══════╝   ╚═╝  ╚═╝   ╚═════╝    ╚══════╝   ╚═╝  ╚═╝    ╚═════╝    ╚══════╝
```

CERBERUS is an **advanced password profiling tool** for
🔹 **Penetration Testers**
🔹 **Bug Bounty Hunters**
🔹 **Cybersecurity Researchers**

It generates **custom password wordlists** from personal/user information like names, usernames, emails, pets, DOBs, and more – ideal for **targeted dictionary attacks** in real-world scenarios.

---

## ✨ Why use CERBERUS?

Unlike generic wordlists (e.g., *rockyou.txt*), CERBERUS builds **personalized, context-aware wordlists** that:
✔️ Increase cracking success rate
✔️ Include **leet-speak** variants & reversals
✔️ Add **breached/common passwords** for realism
✔️ Apply filters (min/max length, required digits/symbols/uppercase)
✔️ Work across **Linux, Windows, and macOS**

---

## 📦 Installation

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/Sharma7147/cerberus.git
cd cerberus
```

---

### 2️⃣ Install Dependencies

#### 🔹 On **Debian/Ubuntu/Kali Linux**

Modern Debian/Kali **block global pip installs** (PEP 668).
You have two safe options:

**(a) Virtual Environment (Recommended)**

```bash
sudo apt update
sudo apt install python3 python3-pip python3-venv -y

python3 -m venv venv
source venv/bin/activate

pip install --upgrade pip
pip install -r requirements.txt
pip install -e .
```

**(b) pipx (No venv needed)**

```bash
sudo apt install pipx -y
pipx install .
```

---

#### 🔹 On **Windows (PowerShell)**

Make sure **Python 3.9+** is installed and added to PATH.

```powershell

# Install dependencies
pip install --upgrade pip
pip install -r requirements.txt
pip install -e .
```

---

## 🚀 Usage

### Option 1: Run directly (no installation required)

```bash
python run.py -h
python run.py -i
```

---

---


---

## ⚡ Features

* 🔑 Generate wordlists from **names, usernames, emails, pets, DOBs**
* 🔄 Apply **leet-speak** (1337) and **reverse strings**
* 🔒 Enforce password policies (**digits, symbols, upper/lower**)
* 📏 Control **min/max length**
* 📂 Save results to a file automatically
* 🔥 Inject **top breached/common passwords**

---

## 📜 License

This project is licensed under the **MIT License**.
You are free to use, modify, and distribute it with attribution.

---

## ⚠️ Disclaimer

CERBERUS is intended **for educational and authorized security testing only**.
The author assumes **no liability for misuse**.
Using this tool without consent on real systems is **illegal**.

---

## 👨‍💻 Author

**Yashraj Sharma**
GitHub: [Sharma7147](https://github.com/Sharma7147)

---
