blockchain = [[1]]


def add_value(value):
    blockchain.append([blockchain[-1], value])
    print(blockchain)
