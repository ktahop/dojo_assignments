class User:
  def __init__(self, first_name, last_name, email, age = 20):
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

  # def add_points(self)

  def enroll(self):
    if self.is_rewards_member:
      print("User already a member.")
    else:
      self.is_rewards_member = True
      self.gold_card_points = 200

  def spend_points(self, amount):
    if amount > self.gold_card_points:
      print("Not enough points.")
    else:
      self.gold_card_points -= amount

user1 = User("Kris", "Tahop", "ktahop@gmail.com")
user1.display_info()
print(" ")

user1.enroll()
print(user1.is_rewards_member)
print(" ")

user2 = User("Katrina", "Farinas", "katrina.f@gmail.com", 35)
user3 = User("Joyce", "Russell", "joyce.r@gmail.com", 39)
user1.spend_points(50)
user2.enroll()
user2.spend_points(80)

user1.display_info()
print(" ")
user2.display_info()
print(" ")
user3.display_info()
print(" ")

user1.enroll()
print(" ")

user3.spend_points(40)
