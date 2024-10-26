from ATMController import ATMController
from src.CardReader import CardReader
from src.BankAPI import BankAPI

cardReader = CardReader()
bankAPI = BankAPI()
controller = ATMController(cardReader, bankAPI)

def test_readCard():
  cardReader.insertCard("1111")
  assert controller.readCard() == "1111"

def test_readCard_RemovedCard():
  cardReader.removeCard()
  assert controller.readCard() == ""

def test_checkPin_correctPIN():
  cardReader.insertCard("1111111111111111")
  controller.readCard()
  print(controller.currentInfo["cardNumber"])
  pin = 1234
  assert controller.checkPin(pin) == True

def test_checkPin_wrongPIN():
  cardReader.insertCard("1111111111111111")
  controller.readCard()
  pin = 4312
  assert controller.checkPin(pin) == False

def test_checkPin_NoCard():
  controller.endTransaction()
  pin = 1234
  assert controller.checkPin(pin) == False

def test_checkPin_invalidCard():
  cardReader.insertCard("1")
  controller.readCard()
  pin = 4312
  assert controller.currentInfo["cardNumber"] == "1"
  assert controller.checkPin(pin) == False

