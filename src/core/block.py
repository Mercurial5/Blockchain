from dataclasses import dataclass, field
from datetime import datetime
from hashlib import sha256

from core.transaction import Transaction


@dataclass
class Block:
    index: int
    previous_hash: str
    hash: str = ''
    timestamp: datetime = field(default_factory=datetime.now)
    _transactions: list[Transaction] = field(default_factory=list)

    def add_transaction(self, transaction: Transaction) -> None:
        new_hash = sha256((self.hash + str(transaction)).encode()).hexdigest()
        self.hash = new_hash
        self._transactions.append(transaction)

    @property
    def length(self) -> int:
        return len(self._transactions)

    @property
    def transactions(self) -> list[Transaction]:
        return self._transactions
