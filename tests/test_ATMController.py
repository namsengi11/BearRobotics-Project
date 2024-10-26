from ATMController import ATMController
from src.CardReader import CardReader
from src.BankAPI import BankAPI

cardReader = CardReader()
bankAPI = BankAPI()
controller = ATMController(cardReader, bankAPI)

def test_readCardFromController():
  cardReader.insertCard("1111")
  assert controller.readCard() == "1111"

def test_readRemovedCard():
  cardReader.removeCard()
  assert controller.readCard() == ""