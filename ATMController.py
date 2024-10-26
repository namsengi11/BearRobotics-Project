from src.CardReader import CardReader
from src.BankAPI import BankAPI

class ATMController:
  def __init__(self, cardReader: CardReader, bankAPI: BankAPI) -> None:
    # have dedicated reader to ATM
    self.cardReader = cardReader

    # Establish connection to BANKAPI
    self.BankAPI = bankAPI

    self.currentInfo = {
      "cardNumber": "",
      "enteredCorrectPin": False,
      "accountNumber": ""
    }

  # prompts CardReader to read inserted card
  # returns card number read
  def readCard(self) -> str:
    try:
      cardNum = self.cardReader.readCard()
      self.currentInfo["cardNumber"] = cardNum
      return self.cardReader.readCard()
    except Exception as e:
      print(e)
      return ""

  # checks if pin is correct for inserted card
  # returns success of operation
  def checkPin(self, pin: int) -> bool:
    if self.currentInfo["cardNumber"] == "":
      print("No card")
      return False

    # in real life, controller waits for keypad to enter pin
    try:
    # should hash pin for security
      self.currentInfo["enteredCorrectPin"] = self.BankAPI.isCorrectPin(self.currentInfo["cardNumber"], pin)
      return self.currentInfo["enteredCorrectPin"]
    except Exception as e:
      print(e)
      return False

  # ends current transaction and resets information stored
  def endTransaction(self) -> None:
    self.cardReader.removeCard()
    self.currentInfo = {
      "cardNumber": "",
      "enteredCorrectPin": False,
      "accountNumber": ""
    }