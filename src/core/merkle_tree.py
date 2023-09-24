import hashlib


class MerkleTree:
    @staticmethod
    def build_tree(transactions: list[str]) -> str:
        if len(transactions) == 0:
            return '0'

        if len(transactions) == 1:
            return hashlib.sha256(str(transactions[0]).encode()).hexdigest()

        new_transactions = []
        for i in range(0, len(transactions), 2):
            combined = transactions[i]

            if i + 1 < len(transactions):
                combined += transactions[i + 1]

            combined_hash = hashlib.sha256(combined.encode()).hexdigest()
            new_transactions.append(combined_hash)

        return MerkleTree.build_tree(new_transactions)