import json
from pathlib import Path

import sandbox
from web3 import Web3
from eth_abi import encode

def set_balance(web3: Web3, account_address: str, amount: int):
    res = web3.provider.make_request(
        "anvil_setBalance",
        [account_address, amount]
    )
    print(res)


def deploy(web3: Web3, deployer_address: str, deployer_privateKey: str, player_address: str) -> str:
    contract_info = json.loads(Path("compiled/Setup.sol/Setup.json").read_text())
    abi = contract_info["abi"]
    bytecode = contract_info["bytecode"]["object"]

    contract = web3.eth.contract(abi=abi, bytecode=bytecode)

    # TheGenesisCrypt Setup requires playerAddress and 10 ETH
    construct_txn = contract.constructor(player_address).build_transaction(
        {
            "from": deployer_address,
            "nonce": web3.eth.get_transaction_count(deployer_address),
            "value": Web3.to_wei(10, 'ether'),
        }
    )

    tx_create = web3.eth.account.sign_transaction(construct_txn, deployer_privateKey)
    tx_hash = web3.eth.send_raw_transaction(tx_create.raw_transaction)

    rcpt = web3.eth.wait_for_transaction_receipt(tx_hash)
    setup_address = rcpt.contractAddress

    # Get the GenesisCrypt (TARGET) address from the Setup contract
    setup_contract = web3.eth.contract(address=setup_address, abi=abi)
    target_address = setup_contract.functions.TARGET().call()

    # Call proposeState twice on the GenesisCrypt contract using deployer's key
    # These calls set up the challenge state
    propose_state_selector = Web3.keccak(text="proposeState(string)")[:4]
    
    # First call: proposeState("Constructors_must_now_be_defined")
    first_proposal = "Constructors_must_now_be_defined"
    encoded_data_1 = propose_state_selector + encode(['string'], [first_proposal])
    
    tx1 = {
        "from": deployer_address,
        "to": target_address,
        "nonce": web3.eth.get_transaction_count(deployer_address),
        "gas": 100000,
        "gasPrice": web3.eth.gas_price,
        "data": encoded_data_1,
    }
    signed_tx1 = web3.eth.account.sign_transaction(tx1, deployer_privateKey)
    tx_hash1 = web3.eth.send_raw_transaction(signed_tx1.raw_transaction)
    web3.eth.wait_for_transaction_receipt(tx_hash1)
    print(f"First proposeState call completed: {tx_hash1.hex()}")

    # Second call: proposeState("_using_the_constructor_keyword")
    second_proposal = "_using_the_constructor_keyword"
    encoded_data_2 = propose_state_selector + encode(['string'], [second_proposal])
    
    tx2 = {
        "from": deployer_address,
        "to": target_address,
        "nonce": web3.eth.get_transaction_count(deployer_address),
        "gas": 100000,
        "gasPrice": web3.eth.gas_price,
        "data": encoded_data_2,
    }
    signed_tx2 = web3.eth.account.sign_transaction(tx2, deployer_privateKey)
    tx_hash2 = web3.eth.send_raw_transaction(signed_tx2.raw_transaction)
    web3.eth.wait_for_transaction_receipt(tx_hash2)
    print(f"Second proposeState call completed: {tx_hash2.hex()}")

    # Player starts with 1 ETH
    set_balance(web3, player_address, Web3.to_wei(1, 'ether'))

    return setup_address

def pre_tx_hook(data, node_info):
    return 200, ""

def post_tx_hook(data, response, node_info):
    return 200, ""

app = sandbox.run_launcher(
    deploy,
    pre_tx_hook=pre_tx_hook,
    post_tx_hook=post_tx_hook
)
