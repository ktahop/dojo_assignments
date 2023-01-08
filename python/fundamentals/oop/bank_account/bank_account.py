class BankAccount:
  acct_info = []

  def __init__(self, int_rate, balance = 0):
    self.int_rate = float(int_rate/100)
    self.balance = float(balance)
    BankAccount.acct_info.append(self)

  def deposit(self, amount):
    self.balance += amount
    return self

  def withdraw(self, amount):
    if amount > self.balance:
      print("Insufficient funds: Charging a $5 fee")
      self.balance -= 5
      return self
    self.balance -= amount
    return self

  def display_account_info(self):
    print(f"Balance: ${round(self.balance, 2)}")
    return self

  def yield_interest(self):
    if self.balance > 0:
      self.balance += self.balance * self.int_rate
    return self

  @classmethod 
  def all_acct_info(cls):
    for acct in cls.acct_info:
      acct.display_account_info()


acct1 = BankAccount(1, 500)
acct2 = BankAccount(2, 1000)

acct1.deposit(100.25).deposit(200.50).deposit(300.75).withdraw(400).yield_interest().display_account_info()

acct2.deposit(500.10).deposit(500.20).withdraw(100.30).withdraw(200.40).withdraw(300.50).withdraw(400.60).yield_interest().display_account_info()

BankAccount.all_acct_info()