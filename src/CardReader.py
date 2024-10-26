class CardReader:
  def __init__(self) -> None:
    self.haveCard = False
    self.cardNum = ""

  def insertCard(self, cardNumber: str) -> None:
    self.haveCard = True
    self.cardNum = cardNumber

  def removeCard(self) -> None:
    self.haveCard = False
    self.cardNum = ""

  def readCard(self):
    if self.haveCard:
      return self.cardNum
    else:
      raise Exception("No card in reader")