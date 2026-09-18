T ENCODER 🔐

A powerful multi-encoding Python obfuscator by tepeed. Encode your Python scripts using 23 different encoding methods, generate ready-to-run decoders, obfuscate with PyArmor, and build standalone EXEs with PyInstaller.

---

✨ Features

· 🔢 23 Encoding Methods — Base16/32/64/85, ROT13, Zlib, Gzip, Bz2, Lzma, Marshal, Pickle, XOR, and many combinations
· 😀 Emoji Encoding — Python bytecode hidden as emoji (pyc_emoji)
· 🛡️ PyArmor Obfuscation — One-click obfuscation (recommended v9.1.8)
· 📦 PyInstaller Builds — Compile .py → standalone .exe
· ⚡ PyArmor + EXE — Obfuscate then package into EXE in a single step
· 🎨 Colorful UI — Gradient banner, live timezone, progress bars
· 📁 Auto Output — Encoded files and runners saved to encode/

---

📱 Installation on Termux

```bash
pkg update -y && pkg upgrade -y
pkg install git python python-pip -y
pip install --upgrade pip

git clone https://github.com/tepeed/multiple-encryptions-for-python-.git
cd multiple-encryptions-for-python-
pip install -r requirements.txt
python run.py
```

One-Line Install

```bash
pkg update -y && pkg upgrade -y && pkg install git python python-pip -y && pip install --upgrade pip && git clone https://github.com/tepeed/multiple-encryptions-for-python-.git && cd multiple-encryptions-for-python- && pip install -r requirements.txt && python run.py
```

---

💻 Installation on Linux / Windows / macOS

```bash
git clone https://github.com/tepeed/multiple-encryptions-for-python-.git
cd multiple-encryptions-for-python-
pip install -r requirements.txt
python run.py
```

Or inside the tool, choose Option 25 to auto-install all required packages.

---

🎮 Usage

Run the tool:

```bash
python run.py
```

You'll see a menu with options:

Option Description
01–23 Encoding methods (enter path to .py file)
24 PyArmor Obfuscate
25 Install all required packages
26 Helper / Usage info
27 Build EXE with PyInstaller
28 PyArmor + EXE (Obfuscate + Package)
00 Exit

Output location: encode/

Each encoding produces:

· encode/encoded-<method>.txt — the encoded payload
· encode/runner-<method>.py — a ready-to-execute decoder

---

🧩 Requirements

· Python 3.8+
· colorama, pyfiglet, tqdm, pytz, requests, aiofiles
· pyarmor==9.1.8 (for obfuscation)
· pyinstaller (for EXE builds)

Install all at once:

```bash
pip install -r requirements.txt
```

---

📂 Project Structure

```
multiple-encryptions-for-python-/
├── run.py              # Main tool
├── requirements.txt    # Python dependencies
├── encode/             # Output folder (auto-created)
│   ├── encoded-*.txt
│   └── runner-*.py
└── README.md
```

---

📞 Contact

· 👤 Developer: @tepeed
· 💬 Telegram: @wlzbi
· 🔗 GitHub: https://github.com/tepeed

---

⚠️ Disclaimer

This tool is intended for educational purposes only. Use it responsibly and only on code you own or have permission to modify. The author is not responsible for any misuse.

---

⭐ If you find this useful, give the repo a star!
