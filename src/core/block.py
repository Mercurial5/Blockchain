import hashlib
from dataclasses import dataclass, field
from datetime import datetime

from core.merkle_tree import MerkleTree
from core.transaction import Transaction


@dataclass
class Block:
    index: int
    previous_hash: str
    _transactions: list[Transaction]
    nonce: int = 0
    difficulty: int = 2
    merkle_root: str = field(init=False)
    hash: str = field(init=False)
    timestamp: datetime = field(default_factory=datetime.now)

    def __post_init__(self):
        transactions_str = [str(transaction) for transaction in self.transactions]
        self.merkle_root = MerkleTree.build_tree(transactions_str)

        self.hash = self.__calculate_hash()

    @property
    def length(self) -> int:
        return len(self._transactions)

    @property
    def transactions(self) -> list[Transaction]:
        return self._transactions

    def __calculate_hash(self) -> str:
        new_hash = ''
        while new_hash[:self.difficulty] != '0' * self.difficulty:
            self.nonce += 1
            new_hash = f'{self.index}{self.previous_hash}{self.timestamp}{self.transactions}{self.merkle_root}{self.nonce}'
            new_hash = hashlib.sha256(new_hash.encode()).hexdigest()

        return new_hash
