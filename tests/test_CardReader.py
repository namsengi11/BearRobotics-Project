from src.CardReader import CardReader

cardReader = CardReader()

def test_readWithoutCard():
  try:
    cardReader.readCard()
  except Exception as e:
    assert isinstance(e, Exception) == True

def test_insertCard():
  cardReader.insertCard("1111")
  assert cardReader.haveCard == True

def test_readInsertedCard():
  cardReader.insertCard("1111")
  assert cardReader.cardNum == "1111"

def test_removeCard():
  cardReader.insertCard("1111")
  assert cardReader.cardNum == "1111"
  cardReader.removeCard()
  assert cardReader.haveCard == False
  assert cardReader.cardNum == ""
  try:
    cardReader.readCard()
  except Exception as e:
    assert isinstance(e, Exception)