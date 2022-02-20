from brownie import network, config, accounts 


def afunction():
    pass

def get_account_():
    if(network.show_active() == "development"): 
        return accounts[0]
    else: 
        return accounts.add(config['wallets']['from_key'])