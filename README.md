



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

---

## 📦 Installation & Setup

Run the following commands step by step:

```bash
# 1. Clone the repository
git clone https://github.com/Sharma7147/cerberus.git
cd cerberus

# 2. Install dependencies
pip install -r requirements.txt

```

---

## 🚀 Usage Examples

### **Help Menu**

```bash
python cerberus.py -h
```

### **Interactive Mode**

```bash
python cerberus.py -i
```



---

### **Direct CLI Example**

```bash
python cerberus.py \
  --first John \
  --last Ahmed \
  --usernames john123 \
  --emails john@example.com \
  --pets rex \
  --numbers 1234 \
  --dob 1999-05-10 \
  --limit 5000 \
  --min-len 6 \
  --max-len 20 \
  --breached \
  --output john_wordlist.txt
```

---

## ⚙️ CLI Options

| Option              | Description                            |
| ------------------- | -------------------------------------- |
| `--first`           | First name                             |
| `--last`            | Last name                              |
| `--usernames`       | List of usernames                      |
| `--emails`          | List of emails                         |
| `--pets`            | List of pet names                      |
| `--numbers`         | Numbers to include                     |
| `--dob`             | Date of Birth (YYYY-MM-DD)             |
| `--keywords`        | Extra keywords (company, domain, etc.) |
| `--limit`           | Max wordlist size (default 5000)       |
| `--min-len`         | Minimum password length                |
| `--max-len`         | Maximum password length                |
| `--breached`        | Include top breached/common passwords  |
| `--output`          | Output file name                       |
| `-i, --interactive` | Launch interactive mode                |

---

## 📂 Example Output

```
john123
Ahmed@1999
rex007
john!123
passwordJohn
...
```

---

## ⚖️ License

This project is licensed under the **MIT License** – free to use, modify, and distribute.

---

## 🔒 Privacy & Disclaimer

* This tool is built **for educational and research purposes only**.
* Do **not** use it against systems without **explicit permission**.
* The authors are **not responsible** for any misuse or damage caused.


