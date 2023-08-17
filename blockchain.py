blockchain = []


def get_last_blockchain_value():
    return blockchain[-1]


def add_value(value, last_transaction=[1]):
    blockchain.append([last_transaction, value])


add_value(1.17)
add_value(123.21, get_last_blockchain_value())
add_value(-14, get_last_blockchain_value())

print(blockchain)
