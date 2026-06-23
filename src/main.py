from wallet import create_wallet
from wallet import save_wallet

from check_key import verify_wallet


def main():

    wallet = create_wallet()

    save_wallet(wallet)

    print(f"Wallet Address: {wallet['address']}")

    recovered_address = verify_wallet()

    print(f"Recovered Address: {recovered_address}")

    if wallet["address"] == recovered_address:
        print("Wallet verification success")
    else:
        print("Wallet verification failed")


if __name__ == "__main__":
    main()