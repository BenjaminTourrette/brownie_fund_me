from brownie import FundMe, MockV3Aggregator, network, config
#from scripts.helpful_scripts import get_account
from scripts.helpful_scripts import deploy_mocks, get_account_, deploy_mocks

DECIMALS = 18
STARTING_PRICE = 2000

def deploy_fund_me():
    account = get_account_()
    
    
    # if we are on persistant network use associated address 
    # if not deploy mocks
    if network.show_active() != "development":
        price_feed_address = config['networks'][network.show_active()]['eth_usd_price_feed']
    else: 
        deploy_mocks()
        price_feed_address = MockV3Aggregator[-1].address
        print("Deployed")
        
    
    
    fund_me = FundMe.deploy("0x8A753747A1Fa494EC906cE90E9f37563A8AF630e", 
                            {"from" : account}, publish_source=config['networks'][network.show_active()].get("verify"))
    print(f"Contract deployed to {fund_me.address}")
    
    
def store_value(value):
    #FundMe[-1].fund(15, {"from": get_account_()})
    print(FundMe[-1].fund({'value': value, 'from':get_account_()}))

def main():
    deploy_fund_me()
    #store_value(15)