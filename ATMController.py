from src.CardReader import CardReader
from src.BankAPI import BankAPI

class ATMController:
  def __init__(self, cardReader: CardReader, bankAPI: BankAPI) -> None:
    # have dedicated reader to ATM
    self.cardReader = cardReader

    # Establish connection to BANKAPI
    self.BankAPI = bankAPI

  def readCard(self) -> str:
    try:
      return self.cardReader.readCard()
    except Exception as e:
      print(e)