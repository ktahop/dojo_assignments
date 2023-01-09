import pet

class Ninja:
  def __init__(self, first_name, last_name, pet, treats, pet_food):
    self.first_name = first_name
    self.last_name = last_name
    self.pet = pet
    self.treats = treats
    self.pet_food = pet_food

  def walk(self):
    self.pet.play()
    print("Enjoyed the walk!")
    return self

  def feed(self):
    self.pet.eat()
    print("Finished food quickly!")
    return self

  def bathe(self):
    self.pet.noise()
    return self

rufus = pet.Dog("Rufus", "bulldog", "shake")
kris = Ninja("Kris", "Tahop", rufus, "Milk-Bone", "Pedigree")

kris.walk().feed().bathe()
