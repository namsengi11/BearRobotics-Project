class CashBin:
  def __init__(self, balance: int) -> None:
    self.balance = balance

  # returns if the cashbin has more cash than the requested amount
  def haveMoreThan(self, amount: int) -> bool:
    return self.balance >= amount

  def addToBalance(self, amount: int) -> None:
    self.balance += amount

  def removeFromBalance(self, amount:int) -> None:
    if self.balance < amount:
      raise Exception("Not enough money in cashbin")
    self.balance -= amount