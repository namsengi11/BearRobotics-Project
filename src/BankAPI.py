class BankAPI:

  def isValidCard(self, cardNum: int) -> bool:
    return cardNum in self.cardNumToUser

