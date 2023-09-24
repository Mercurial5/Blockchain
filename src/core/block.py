from dataclasses import dataclass, field
from datetime import datetime
from hashlib import sha256

from core.transaction import Transaction


@dataclass
class Block:
    index: int
    previous_hash: str
    _transactions: list[Transaction]
    hash: str = field(init=False)
    timestamp: datetime = field(default_factory=datetime.now)

    def __post_init__(self):
        self.hash = ''

        for transaction in self._transactions:
            self.hash = sha256((self.hash + str(transaction)).encode()).hexdigest()

    @property
    def length(self) -> int:
        return len(self._transactions)

    @property
    def transactions(self) -> list[Transaction]:
        return self._transactions
