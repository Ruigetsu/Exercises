from web3 import  Web3
import json
import requests
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects

ERC20_ABI = json.loads('''[{"inputs":[{"internalType":"string","name":"_name","type":"string"},{"internalType":"string","name":"_symbol","type":"string"},{"internalType":"uint256","name":"_initialSupply","type":"uint256"}],"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"owner","type":"address"},{"indexed":true,"internalType":"address","name":"spender","type":"address"},{"indexed":false,"internalType":"uint256","name":"value","type":"uint256"}],"name":"Approval","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"from","type":"address"},{"indexed":true,"internalType":"address","name":"to","type":"address"},{"indexed":false,"internalType":"uint256","name":"value","type":"uint256"}],"name":"Transfer","type":"event"},{"inputs":[{"internalType":"address","name":"owner","type":"address"},{"internalType":"address","name":"spender","type":"address"}],"name":"allowance","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"approve","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"account","type":"address"}],"name":"balanceOf","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"decimals","outputs":[{"internalType":"uint8","name":"","type":"uint8"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"subtractedValue","type":"uint256"}],"name":"decreaseAllowance","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"addedValue","type":"uint256"}],"name":"increaseAllowance","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"name","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint8","name":"decimals_","type":"uint8"}],"name":"setupDecimals","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"symbol","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"totalSupply","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"recipient","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"transfer","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"sender","type":"address"},{"internalType":"address","name":"recipient","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"transferFrom","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"}]''')

url = 'https://pro-api.coinmarketcap.com/v2/tools/price-conversion'
COINMARKETCAP_API = "105dbb7e-bc1c-43f7-8bd8-c617faf01bea"
INFURA_API = "0d12ed4428834836abad0bdb71f85446"
INFURA_URL = "https://mainnet.infura.io/v3/" + INFURA_API
#wallet_address = "0xA9D1e08C7793af67e9d92fe308d5697FB81d3E43"
#token_address = "0x2260FAC5E5542a773Aa44fBCfeDf7C193bc2C599"

web3 = Web3(Web3.HTTPProvider(INFURA_URL))

def get_info(wallet_address, token_address, convert_into):
    contract = web3.eth.contract(token_address, abi = ERC20_ABI)
    token_symbol =  contract.functions.symbol().call()
    token_demicals = contract.functions.decimals().call()
    token_balance = contract.functions.balanceOf(wallet_address).call()
    total_amount = token_balance / 10**token_demicals

    parameters = {

        'amount' : total_amount,
        'symbol': token_symbol,
        'convert' : convert_into
        }

    headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': COINMARKETCAP_API,
    }

    session = Session()
    session.headers.update(headers)

    try:

        response = session.get(url, params=parameters)
        print(response)
        data = response.json().get("data")
        info = data[0]
        info_1 = info['quote']
        info_2 = info_1[convert_into]
        info_3 = info_2['price']
        print(f"name: {info['name']}, amount: {info['amount']:,}, convert into: {convert_into}, price: {info_3:,}")

    except (ConnectionError, Timeout, TooManyRedirects) as e:
        
        print(e)

print(get_info("0xA9D1e08C7793af67e9d92fe308d5697FB81d3E43","0x1f9840a85d5aF5bf1D1762F925BDADdC4201F984", "USDT"))