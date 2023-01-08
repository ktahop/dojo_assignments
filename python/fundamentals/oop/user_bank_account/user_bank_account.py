class BankAccount:
  def __init__(self, int_rate, balance = 0):
    self.int_rate = float(int_rate/100)
    self.balance = float(balance)

  def deposit(self, amount):
    self.balance += amount
    return self

  def withdraw(self, amount):
    if amount > self.balance:
      print("Insufficient funds: Charging a $5 fee")
      self.balance -= 5
    else:
      self.balance -= amount
    return self

  def display_account_info(self):
    print(f"Balance: ${round(self.balance, 2)}")
    return self

  def yield_interest(self):
    if self.balance > 0:
      self.balance += self.balance * self.int_rate
    return self

class User:
  def __init__(self, name, email):
    self.name = name
    self.email = email
    self.checking = BankAccount(int_rate=0.02, balance=0)
    self.savings = BankAccount(0, 0)

  def make_deposit(self, amount, acct_type = "checking"):
    if acct_type != "checking":
      self.savings.deposit(amount)
    self.checking.deposit(amount)
    return self

  def make_withdraw(self, amount, acct_type = "checking"):
    if acct_type != "checking":
      self.savings.withdraw(amount)
    self.checking.withdraw(amount)
    return self

  def display_user_balance(self):
    print(f"User: {self.name}, Checking Balance: {self.checking.balance}\n"
          f"User: {self.name}, Savings Balance: {self.savings.balance}")
    # self.account.display_account_info()
    return self

  def transfer_money(self, amount, other_user):
    self.checking.withdraw(amount)
    other_user.checking.deposit(amount)
    return self


acct1 = User("Kris", "ktahop@gmail.com")
acct2 = User("Kat", "kat.f@gmail.com")

acct1.make_deposit(200).transfer_money(50, acct2).display_user_balance()

acct2.make_deposit(200).make_deposit(50,"savings").display_user_balance()

