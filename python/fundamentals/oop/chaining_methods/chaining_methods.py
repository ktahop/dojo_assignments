class User:
  def __init__(self, first_name, last_name, email, age):
    self.first_name = first_name
    self.last_name = last_name
    self.email = email
    self.age = age
    self.is_rewards_member = False
    self.gold_card_points = 0

  def display_info(self):
    print(f"{self.first_name}\n" 
          f"{self.last_name}\n" 
          f"{self.email}\n"
          f"{self.age}\n"
          f"{self.is_rewards_member}\n"
          f"{self.gold_card_points}")
    return self

  def enroll(self):
    if self.is_rewards_member:
      print("User already a member.")
    else:
      self.is_rewards_member = True
      self.gold_card_points = 200
    return self

  def spend_points(self, amount):
    if amount > self.gold_card_points:
      print("Not enough points.")
    else:
      self.gold_card_points -= amount
    return self

user1 = User("Kris", "Tahop", "ktahop@gmail.com", 34)
user2 = User("Katrina", "Farinas", "katrina.f@gmail.com", 35)
user3 = User("Joyce", "Russell", "joyce.r@gmail.com", 39)

user1.display_info().enroll().spend_points(50).display_info().enroll()
user2.enroll().spend_points(80).display_info()
user3.display_info().spend_points(40)