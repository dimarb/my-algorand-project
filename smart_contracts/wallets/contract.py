from algopy import ARC4Contract, LocalState, Txn, UInt64
from algopy.arc4 import abimethod


class Wallets(ARC4Contract):
    def __init__(self) -> None:
        self.local = LocalState(UInt64)

    @abimethod(allow_actions = ["OptIn"])
    def setBalace(self, balance: UInt64) -> None:
        self.local[Txn.sender] = balance

    @abimethod()
    def getBalance(self) -> UInt64:
        result, exists = self.local.maybe(Txn.sender)
        assert exists, "no data for balance for account"
        return result
