from brownie import FundMe, MockV3Aggregator, network, config
#from scripts.helpful_scripts import get_account
from scripts.helpful_scripts import deploy_mocks, get_account_, deploy_mocks, LOCAL_BLOCKCHAIN_ENVIRONMENT, FORKED_LOCAL_ENVIRONMENT, pushContractAddressToApi



def deploy_fund_me():
    account = get_account_()
    # if we are on persistant network use associated address 
    # if not deploy mocks
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENT:
        print('active network : ', config['networks'][network.show_active()])
        price_feed_address = config['networks'][network.show_active()]['eth_usd_price_feed']
    else: 
        deploy_mocks()
        price_feed_address = MockV3Aggregator[-1].address
        #print("Deployed")
    
    fund_me = FundMe.deploy(price_feed_address, 
                            {"from" : account}, publish_source=config['networks'][network.show_active()].get("verify"))
    print(f"Contract deployed to {fund_me.address}")
    
    if network.show_active() != 'ganache-local' and network.show_active() not in FORKED_LOCAL_ENVIRONMENT :
        print("Pushing to API ...")
        pushContractAddressToApi(FundMe[-1])
    return fund_me
    
    
def store_value(value):
    #FundMe[-1].fund(15, {"from": get_account_()})
    print(FundMe[-1].fund({'value': value, 'from':get_account_()}))

def main():
    deploy_fund_me()
    #store_value(15)