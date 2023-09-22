from dataclasses import dataclass


@dataclass
class Transaction:
    sender: str
    receiver: str
    amount: int

    def __str__(self) -> str:
        return f'<Transaction {self.sender} -> {self.receiver}: {self.amount}>'
