class BankAPI:
  def __init__(self) -> None:
    # hypothetical data in DB
    self.cardNumToPin = {
      "1111111111111111": 1234,
      "2222222222222222": 0000,
      "3333333333333333": 4321
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
    return self.cardNumToPin[cardNum] == pin


