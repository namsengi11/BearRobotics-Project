class CardReader:
  def __init__(self) -> None:
    self.haveCard = False
    self.cardNum = ""

  # insert card to device
  def insertCard(self, cardNumber: str) -> None:
    self.haveCard = True
    self.cardNum = cardNumber

  # remove card from device
  def removeCard(self) -> None:
    self.haveCard = False
    self.cardNum = ""

  # reads card num from current card
  # returns card number
  def readCard(self) -> int:
    if self.haveCard:
      return self.cardNum
    else:
      raise Exception("No card in reader")