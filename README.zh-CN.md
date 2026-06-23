# Web3 Python Starter

[English](README.md)

![Python](https://img.shields.io/badge/Python-3.11+-blue)
![License](https://img.shields.io/badge/License-MIT-green)
![Web3](https://img.shields.io/badge/Web3.py-Latest-orange)

一个面向生产环境的 Python Web3 Starter Template。

## Wallet Tutorial

使用 Python 创建第一个链上钱包，并学习如何安全管理私钥。

---

## 项目结构

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

## 功能

- 创建钱包
- 生成钱包地址
- 保存私钥到 `.env`
- 从私钥恢复钱包
- 验证钱包地址
- 自动管理虚拟环境

---

## 环境要求

- Python 3.11+
- Windows PowerShell

检查版本：

```powershell
python --version
```

---

## 初始化项目

创建虚拟环境：

```powershell
python -m venv .venv
```

激活环境：

```powershell
.\scripts\activate.ps1
```

如果 `.venv` 不存在，脚本会自动创建。

---

## 安装依赖

```powershell
pip install web3
pip install eth-account
pip install python-dotenv
```

或者：

```powershell
pip install -r requirements.txt
```

---

## 运行项目

```powershell
python src/main.py
```

示例输出：

```text
Wallet Address: 0x1234...
Recovered Address: 0x1234...
Wallet verification success
```

---

## 自动生成的 .env

程序首次运行后会自动生成：

```env
PRIVATE_KEY=xxxxxxxxxxxxxxxx
WALLET_ADDRESS=0x1234567890
```

---

## 安全提示

请勿：

- 上传 `.env`
- 提交 `.env` 到 GitHub
- 向任何人泄露私钥

推荐 `.gitignore`：

```text
.env
.venv/
__pycache__/
logs/
```

---

## 模块说明

### wallet.py

负责：

- 创建钱包
- 保存钱包

### check_key.py

负责：

- 读取私钥
- 恢复钱包
- 验证地址

### main.py

程序入口：

```text
创建钱包
    ↓
保存私钥
    ↓
恢复钱包
    ↓
验证钱包
```

---

## Roadmap

### 下一课

连接 RPC 节点并查询钱包余额。

内容包括：

- Web3 初始化
- RPC 配置
- 查询 ETH 余额
- 查询最新区块高度
- 验证链连接状态
