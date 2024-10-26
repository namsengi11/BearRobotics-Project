from src.CardReader import CardReader
from src.BankAPI import BankAPI
from src.CashBin import CashBin

class ATMController:
  def __init__(self, cardReader: CardReader, bankAPI: BankAPI, cashBin: CashBin) -> None:
    # have dedicated reader to ATM
    self.cardReader = cardReader

    # Establish connection to BANKAPI
    self.BankAPI = bankAPI

    # Connect to internal cashbin
    self.cashBin = cashBin

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

  # return list of accounts associated with card inserted
  def getConnectedAccounts(self) -> list:
    if self.currentInfo["enteredCorrectPin"]:
      return self.BankAPI.getConnectedAccounts(self.currentInfo["cardNumber"])
    else:
      return []
  # select account for transaction in ATM
  # returns success of operation
  def selectAccount(self, idx: int) -> None:
    accountList = self.getConnectedAccounts()
    try:
      self.currentInfo["accountNumber"] = accountList[idx]
      return True
    except Exception as e:
      print(e)
      self.currentInfo["accountNumber"] = ""
      return False

  # returns balance of account currently accessed
  # returns 0 if no account is accessible
  def checkBalance(self) -> int:
    if self.currentInfo["accountNumber"] == "":
      return 0
    return self.BankAPI.checkBalance(self.currentInfo["accountNumber"])

  # adds amount to accessed account
  # return whether if deposit is successful
  def deposit(self, amount: int) -> bool:
    if self.currentInfo["accountNumber"] == "":
      return False

    try:
      self.BankAPI.depositToAccount(self.currentInfo["accountNumber"], amount)
      self.cashBin.addToBalance(amount)
      return True
    except Exception as e:
      print(e)
      return False

  # withdraws amount from account
  # returns success of operation
  def withdraw(self, amount: int) -> bool:
    if self.currentInfo["accountNumber"] == "":
      return False
    elif not self.cashBin.haveMoreThan(amount):
      return False

    try:
      self.BankAPI.withdrawFromAccount(self.currentInfo["accountNumber"], amount)
      self.cashBin.removeFromBalance(amount)
      return True
    except Exception as e:
      print(e)
      return False

  # ends current transaction and resets information stored
  def endTransaction(self) -> None:
    self.cardReader.removeCard()
    # clear internal cache
    self.currentInfo = {
      "cardNumber": "",
      "enteredCorrectPin": False,
      "accountNumber": ""
    }
