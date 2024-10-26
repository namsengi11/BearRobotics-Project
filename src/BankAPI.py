class BankAPI:
  def __init__(self) -> None:
    # hypothetical data in DB
    self.cardNumToPin = {
      "1111111111111111": 1234,
      "2222222222222222": 0000,
      "3333333333333333": 4321
    }

    self.cardNumToAcc = {
      "1111111111111111": ["123-11", "123-12"],
      "2222222222222222": ["200-10"],
      "3333333333333333":
      ["312-100", "312-483"]
    }

    self.accBalance = {
      "123-11": 100,
      "123-12": 200,
      "200-10": 0,
      "312-100": 1000,
      "312-483": 500
    }

  # checks if card number is registered
  # returns validity of card
  def isValidCard(self, cardNum: str) -> bool:
    return cardNum in self.cardNumToPin

  # checks if given pin is correct for card number
  # returns correctness of pin
  def isCorrectPin(self, cardNum: str, pin: int) -> bool:
    # check validity of card number first
    if not self.isValidCard(cardNum):
      raise Exception("Invalid Card")
    # replace to token to prove access
    return self.cardNumToPin[cardNum] == pin

  # return account associated with card number, empty if no account
  def getConnectedAccounts(self, cardNum: str) -> list:
    if cardNum in self.cardNumToAcc:
      return self.cardNumToAcc[cardNum]
    return []

  # returns balance in account
  # returns 0 if account not registered
  def checkBalance(self, accountNumber: str):
    if accountNumber in self.accBalance:
      return self.accBalance[accountNumber]

    return 0

  # adds indicated amount into balance of account
  # returns success of depositing
  def depositToAccount(self, accountNumber: str, amount: int) -> bool:
    if accountNumber in self.accBalance:
      self.accBalance[accountNumber] += amount
      return True

    raise Exception("No such account")

  # withdraws indicated amount from balance of account
  # returns success of depositing
  def withdrawFromAccount(self, accountNumber: str, amount: int) -> bool:
    if accountNumber in self.accBalance and self.accBalance[accountNumber] >= amount:
      self.accBalance[accountNumber] -= amount
      return True
    elif accountNumber in self.accBalance:
      raise Exception("Not enough balance")

    raise Exception("No such account")