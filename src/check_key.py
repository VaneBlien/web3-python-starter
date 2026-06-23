from dotenv import load_dotenv
from eth_account import Account
import os

def verify_wallet():

    load_dotenv()

    private_key = os.getenv("PRIVATE_KEY")

    account = Account.from_key(private_key)

    return account.address