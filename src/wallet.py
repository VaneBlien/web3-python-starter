from eth_account import Account
from pathlib import Path

def create_wallet():

    account = Account.create()

    return {
        "address": account.address,
        "private_key": account.key.hex()
    }


def save_wallet(wallet):

    env_content = f"""
PRIVATE_KEY={wallet['private_key']}
WALLET_ADDRESS={wallet['address']}
""".strip()

    Path(".env").write_text(env_content)