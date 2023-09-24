from flask import Flask, request, redirect, url_for

from core import Blockchain, Transaction

app = Flask(__name__)

blockchain = Blockchain()


@app.route('/')
def index():
    blocks, mem_pool = blockchain.chain, blockchain.mem_pool
    return {'blocks': blocks, 'mem_pool': mem_pool}


@app.route('/add_transaction', methods=['POST'])
def add_transaction():
    sender = request.form['sender']
    receiver = request.form['receiver']
    amount = int(request.form['amount'])

    transaction = Transaction(sender, receiver, amount)
    blockchain.add_transaction(transaction)

    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
