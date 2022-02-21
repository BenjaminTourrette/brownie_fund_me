from brownie import network, config, accounts , MockV3Aggregator
from web3 import Web3
import json, requests

FORKED_LOCAL_ENVIRONMENT=['mainnet-fork']
LOCAL_BLOCKCHAIN_ENVIRONMENT=['development', 'ganache-local']
DECIMALS = 8
STARTING_PRICE = 200000000000

# Api url 
url = "https://strapi.benjamintourrette.com/smart-contracts"
def afunction():
    pass

def get_account_():
    if network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENT or network.show_active() in FORKED_LOCAL_ENVIRONMENT: 
        return accounts[0]
    else: 
        return accounts.add(config['wallets']['from_key'])
    
    
def deploy_mocks():
    print(f"The active network is {network.show_active()}")
    print(f'Deploying Mocks ...') 
    
    if len(MockV3Aggregator) <= 0:
        mock_aggregator = MockV3Aggregator.deploy(DECIMALS, STARTING_PRICE, {'from' : get_account_()})
    print("Deployed")
    
    
    
def pushContractAddressToApi(contract): 
    # data to be sent to api    
    data = {"contractAddress" : contract.address, 'abi': json.dumps(contract.abi)}
    header = {'Content-Type': 'application/json'}
    
    response = requests.post(url,
        data=json.dumps(
            data
        ),
        headers={
            'Content-Type': 'application/json'
        })
    
    # extracting response text 
    
    print("Response : ", response.text)
