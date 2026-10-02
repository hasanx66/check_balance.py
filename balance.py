from web3 import Web3

# Base Mainnet
RPC_URL = "https://mainnet.base.org"

# SimpleToken deployed on Base
CONTRACT_ADDRESS = "0xa4f77f0367260122148210883cb4459441032467"

ABI = [
    {
        "inputs": [{"name": "", "type": "address"}],
        "name": "balanceOf",
        "outputs": [{"name": "", "type": "uint256"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "decimals",
        "outputs": [{"name": "", "type": "uint8"}],
        "stateMutability": "view",
        "type": "function",
    },
]

web3 = Web3(Web3.HTTPProvider(RPC_URL))

if not web3.is_connected():
    raise ConnectionError("Could not connect to Base")

contract_address = Web3.to_checksum_address(CONTRACT_ADDRESS)
contract = web3.eth.contract(address=contract_address, abi=ABI)

wallet = input("Enter wallet address: ")
wallet = Web3.to_checksum_address(wallet)

balance = contract.functions.balanceOf(wallet).call()
decimals = contract.functions.decimals().call()

token_balance = balance / (10 ** decimals)

print(f"Network: Base")
print(f"Wallet: {wallet}")
print(f"MTK Balance: {token_balance:,.4f}")
