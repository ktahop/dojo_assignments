from classes.deck import Deck
import random

bicycle = Deck()

random1 = random.choice(bicycle.cards)
random2 = random.choice(bicycle.cards)

# if random.choice(bicycle.cards.ke) > random1.keys():
#   print("YUP")
# else:
#   print("NOPE")
print(bicycle.cards[0])