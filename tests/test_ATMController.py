from ATMController import ATMController
from src.CardReader import CardReader
from src.BankAPI import BankAPI
from src.CashBin import CashBin

cardReader = CardReader()
bankAPI = BankAPI()
cashBin = CashBin()
controller = ATMController(cardReader, bankAPI, cashBin)

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

def test_getConnectedAccounts_validCard():
  cardReader.insertCard("1111111111111111")
  controller.readCard()
  pin = 1234

  assert controller.checkPin(pin) == True

  assert controller.getConnectedAccounts() == ["123-11", "123-12"]

def test_getConnectedAccounts_invalidCard():
  cardReader.insertCard("1")
  controller.readCard()
  pin = 1234

  assert controller.checkPin(pin) == False

  assert controller.getConnectedAccounts() == []

def test_getConnectedAccounts_wrongPin():
  cardReader.insertCard("1111111111111111")
  controller.readCard()
  pin = 12345

  assert controller.checkPin(pin) == False

  assert controller.getConnectedAccounts() == []

def test_selectAccount_validCard():
  cardReader.insertCard("1111111111111111")
  controller.readCard()
  pin = 1234
  controller.checkPin(pin)

  assert controller.selectAccount(0) == True
  assert controller.currentInfo["accountNumber"] == "123-11"

  assert controller.selectAccount(2) == False
  assert controller.currentInfo["accountNumber"] == ""

def test_endTransaction():
  controller.endTransaction()
  assert cardReader.haveCard == False
  assert controller.currentInfo["cardNumber"] == ""
  assert controller.currentInfo["enteredCorrectPin"] == False
  assert controller.currentInfo["accountNumber"] == ""
