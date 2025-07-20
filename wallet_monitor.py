import requests

WALLET_ADDRESS = "0x72083bEDe1224e2a2a073c1dc8080e714f737b1B"

def run():
    url = f"https://api.etherscan.io/api?module=account&action=balance&address={WALLET_ADDRESS}&tag=latest&apikey=CXTB4IUT31N836G93ZI3YQBEWBQEGGH5QS"
    data = requests.get(url).json()
    eth_balance = int(data['result']) / 10**18
    print(f"[Wallet Monitor] ETH Balance: {eth_balance} ETH")
