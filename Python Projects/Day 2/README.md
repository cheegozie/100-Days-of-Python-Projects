## 🔐 File Hasher CLI Tool

This is a command-line Python tool that securely hashes any file using MD5, SHA1, or SHA256.

It allows users to verify file integrity, check for tampering, or simply understand how cryptographic hashes work.

This project was created as part of my **100 Days of Python – Cybersecurity Edition** learning journey. It's a hands-on way for me to master the fundamentals of file handling, hashing, and CLI tool creation in Python.


## 🚀 Features

- Hash any file using:
  - `MD5`
  - `SHA1`
  - `SHA256`
- Choose algorithm with `--algo`
- Optional `--show-bytes` flag to display file contents before hashing


## 🧠 What I’m Learning

- How to build secure tools using Python
- What hashes are and why they matter in cybersecurity
- How to handle binary files safely
- The power of `argparse` for command-line apps
- How file integrity checks work using real cryptographic methods


## 📦 Installation

Make sure you have Python installed.

Clone this repository:

```bash
git clone https://github.com/cheegozie/file-hasher
cd file-hasher
```

---

## 🛠️ Usage

This tool works from the command line. Run it like this:

```bash
python reader.py testfile.txt --algo sha256
```

### Optional Flags

- `--algo`: Choose between `md5`, `sha1`, `sha256` (default is sha256)
- `--show-bytes`: Show the file’s byte content before hashing

---

## 📸 Example

```bash
python reader.py testfile.txt --algo sha1 --show-bytes
```

```
Raw file bytes:
 b'Welcome to my code'

SHA1 hash of testfile.txt:
9e15764fa902bd02a3e...
```

---

## ✅ Sample Output

```
SHA256 hash of testfile.txt:
f2c74f9b4b45d7f24e3c6c5f...
```

---

## 🧪 Files in this Project

- `reader.py` – The main Python file hasher script
- `testfile.txt` – A sample file used for testing the hashes
- `README.md` – You're reading it

---

## 📚 License

MIT — free to use and modify.

---

Built as part of my #100DaysOfPython journey — documenting everything I learn publicly.

Created by [@cheeegozie](https://x.com/cheeegozie)
