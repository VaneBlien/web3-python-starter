# Web3 Python Starter

[简体中文](README.zh-CN.md)

![Python](https://img.shields.io/badge/Python-3.11+-blue)
![License](https://img.shields.io/badge/License-MIT-green)
![Web3](https://img.shields.io/badge/Web3.py-Latest-orange)

A production-ready Python Web3 starter template.

## Wallet Tutorial

Create your first blockchain wallet using Python and learn how to manage private keys securely.

---

## Project Structure

```text
wallet_tutorial/
├── scripts/
│   └── activate.ps1
├── src/
│   ├── main.py
│   ├── wallet.py
│   └── check_key.py
├── tests/
├── logs/
├── .venv/
├── .env
├── .gitignore
├── requirements.txt
└── README.md
```

---

## Features

- Generate a wallet
- Create a wallet address
- Store private keys in `.env`
- Recover wallet from private key
- Verify wallet address
- Automatic virtual environment management

---

## Requirements

- Python 3.11+
- Windows PowerShell

Check your Python version:

```powershell
python --version
```

---

## Project Initialization

Create a virtual environment:

```powershell
python -m venv .venv
```

Activate the environment:

```powershell
.\scripts\activate.ps1
```

If `.venv` does not exist, the script will create it automatically.

---

## Install Dependencies

```powershell
pip install web3
pip install eth-account
pip install python-dotenv
```

Or install all dependencies:

```powershell
pip install -r requirements.txt
```

---

## Run the Project

```powershell
python src/main.py
```

Example output:

```text
Wallet Address: 0x1234...
Recovered Address: 0x1234...
Wallet verification success
```

---

## Generated .env File

The application automatically creates:

```env
PRIVATE_KEY=xxxxxxxxxxxxxxxx
WALLET_ADDRESS=0x1234567890
```

---

## Security Notes

Never:

- Upload your `.env`
- Commit `.env` to GitHub
- Share your private key with anyone

Recommended `.gitignore`:

```text
.env
.venv/
__pycache__/
logs/
```

---

## Modules

### wallet.py

Responsible for:

- Wallet generation
- Wallet persistence

### check_key.py

Responsible for:

- Loading private keys
- Recovering wallets
- Verifying addresses

### main.py

Application entry point:

```text
Create Wallet
    ↓
Save Private Key
    ↓
Recover Wallet
    ↓
Verify Wallet
```

---

## Roadmap

### Next Lesson

Connect to an RPC node and query wallet balances.

Topics include:

- Web3 initialization
- RPC configuration
- Query ETH balance
- Query latest block number
- Verify blockchain connectivity
