from core import Blockchain, Transaction


def main():
    blockchain = Blockchain()

    transaction1 = Transaction('dias', 'ayazhan', 1000)
    blockchain.add_transaction(transaction1)

    transaction2 = Transaction('ayazhan', 'daulet', 1000)
    blockchain.add_transaction(transaction2)

    transaction3 = Transaction('daulet', 'dias', 1000)
    blockchain.add_transaction(transaction3)

    print('Current chain:', blockchain.chain)
    print('Current mem pool:', blockchain.mem_pool)


if __name__ == '__main__':
    main()
