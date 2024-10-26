from src.CashBin import CashBin

cashbin = CashBin(1000)

def test_haveMoreThan():
  assert cashbin.haveMoreThan(2000) == False
  assert cashbin.haveMoreThan(500) == True
  assert cashbin.haveMoreThan(1000) == True

def test_addToBalance():
  original = cashbin.balance
  cashbin.addToBalance(100)
  assert cashbin.balance == original + 100

def test_removeFromBalance():
  cashbin.balance = 100
  cashbin.removeFromBalance(50)
  assert cashbin.balance == 50

def test_removeFromBalance_notEnoughBalance():
  try:
    cashbin.balance = 100
    cashbin.removeFromBalance(150)
  except Exception as e:
    assert cashbin.balance == 100
