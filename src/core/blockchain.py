from core.block import Block
from core.transaction import Transaction
from utils import get_logger

logger = get_logger(__name__)


class Blockchain:
    AMOUNT_OF_TRANSACTIONS_PER_BLOCK = 100

    def __init__(self):
        genesis_block = Block(0, '', '0')
        self.chain: list[Block] = [genesis_block]

    @property
    def latest(self) -> Block:
        return self.chain[-1]

    def add_transaction(self, transaction: Transaction) -> None:
        logger.info(f'Adding new transaction - {transaction}')

        if self.latest.length == self.AMOUNT_OF_TRANSACTIONS_PER_BLOCK:
            logger.info('Current block holds max number of transaction, creating new block')
            self.__add_block()

        self.latest.add_transaction(transaction)

    def __add_block(self) -> None:
        block = Block(len(self.chain), self.latest.hash)
        self.chain.append(block)

    def __str__(self) -> str:
        return f'<Blockchain length={len(self.chain)}>'
