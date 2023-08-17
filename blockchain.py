blockchain = [[1]]


def get_last_blockchain_value():
    return blockchain[-1]


def add_value(value):
    blockchain.append([get_last_blockchain_value(), value])


add_value(1.17)
add_value(123.21)
add_value(-14)

print(blockchain)
