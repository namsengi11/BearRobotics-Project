from src.CardReader import CardReader

cardReader = CardReader()


def test_insertCard():
  cardReader.insertCard("1111")
  assert cardReader.haveCard == True

def test_readCard_haveCard():
  cardReader.insertCard("2222")
  assert cardReader.cardNum == "2222"

def test_readCard_withoutCard():
  try:
    cardReader.readCard()
  except Exception as e:
    assert cardReader.haveCard == False
    assert cardReader.cardNum == ""

def test_removeCard():
  cardReader.insertCard("1111")
  assert cardReader.cardNum == "1111"
  cardReader.removeCard()
  assert cardReader.haveCard == False
  assert cardReader.cardNum == ""
  try:
    cardReader.readCard()
  except Exception as e:
    assert cardReader.haveCard == False
    assert cardReader.cardNum == ""