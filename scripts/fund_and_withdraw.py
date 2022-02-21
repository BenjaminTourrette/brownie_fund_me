from brownie import FundMe
from scripts.helpful_scripts import get_account_

def fund():
    fund_me = FundMe[-1]
    account = get_account_()
    entrance_fee = fund_me.getEntranceFee()
    
    print(fund_me.owner())
    print('Current entrance fee : ', entrance_fee)
    
    print('Funding contract')
    fund_me.fund({"from" : account, "value" : entrance_fee})
    
def withdraw():
    fund_me = FundMe[-1]
    account = get_account_()
    
    print('Withdraw')
    fund_me.withdraw({"from": account})

def main():
    fund()
    withdraw()