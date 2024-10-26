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
