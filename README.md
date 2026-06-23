# Wallet Tutorial

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
- 生成地址
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

## 生成的 .env

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
- 分享私钥给任何人

`.gitignore`

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

## 下一课

连接 RPC 节点并查询钱包余额。

内容包括：

- Web3 初始化
- RPC 配置
- 查询 ETH 余额
- 查询区块高度
- 验证链连接状态