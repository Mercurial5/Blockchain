from config import AMOUNT_OF_TRANSACTIONS_PER_BLOCK
from core.block import Block
from core.transaction import Transaction
from utils import get_logger

logger = get_logger(__name__)


class Blockchain:
    mem_pool: list[Transaction] = []

    def __init__(self):
        genesis_block = Block(0, '', [])
        self.chain: list[Block] = [genesis_block]

    @property
    def latest(self) -> Block:
        return self.chain[-1]

    def add_transaction(self, transaction: Transaction) -> None:
        logger.info(f'Adding new transaction - {transaction}')
        self.mem_pool.append(transaction)

        if len(self.mem_pool) == AMOUNT_OF_TRANSACTIONS_PER_BLOCK:
            logger.info('Mem pool is full, creating a block')
            block = Block(len(self.chain), self.latest.hash, self.mem_pool.copy())
            self.chain.append(block)
            self.mem_pool.clear()

    def __str__(self) -> str:
        return f'<Blockchain length={len(self.chain)}>'
