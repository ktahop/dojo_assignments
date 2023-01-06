num1 = 42 # variable declaration, numbers
num2 = 2.3 # variable declaration, numbers (float)
boolean = True # variable declaration, boolean
string = 'Hello World' # variable declaration, strings
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] # variable declaration, list
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} # variable declaration, dictionary
fruit = ('blueberry', 'strawberry', 'banana') # variable declaration, tuples
print(type(fruit)) # log statement, type check
print(pizza_toppings[1]) # log statement, list, access value
pizza_toppings.append('Mushrooms') # list, add value
print(person['name']) # log statement, dictionary, access value
person['name'] = 'George' # dictionary, change value
person['eye_color'] = 'blue' # dictionary, add value
print(fruit[2]) # log statement, tuples, access value

if num1 > 45: # conditional, if
    print("It's greater")
else: # conditional, else
    print("It's lower")

if len(string) < 5: # conditional, if
    print("It's a short word!")
elif len(string) > 15: # conditional, else if
    print("It's a long word!")
else: # conditional, else
    print("Just right!")

for x in range(5): # for loop, stop
    print(x)
for x in range(2,5): # for loop, start, stop
    print(x)
for x in range(2,10,3): # for loop, start, stop, increment
    print(x)
x = 0
while(x < 5): #while loop
    print(x)
    x += 1 # while loop, increment

pizza_toppings.pop() # list, delete value
pizza_toppings.pop(1) # list, access value, delete value

print(person) # log statement, dictionary
person.pop('eye_color') # dictionary, delete value
print(person) # log statement, dictionary

"""
for loop with two if conditionals
if topping is Pepperoni, do nothing and continue loop
print if first conditional is false
stop loop if second conditional is true
"""
for topping in pizza_toppings:
    if topping == 'Pepperoni':
        continue
    print('After 1st if statement')
    if topping == 'Olives':
        break

"""
function
for loop that prints "Hello" until num reaches the value of range
"""
def print_hello_ten_times():
    for num in range(10):
        print('Hello')

print_hello_ten_times() # execute function

"""
function with parameter
prints "Hello" x amount a times set by parameter
"""
def print_hello_x_times(x):
    for num in range(x):
        print('Hello')

"""
calls function with argument
"""
print_hello_x_times(4)

def print_hello_x_or_ten_times(x = 10):
    for num in range(x):
        print('Hello')

print_hello_x_or_ten_times() # calls function without argument
print_hello_x_or_ten_times(4) # calls function with argument


"""
Bonus section
"""

# print(num3)
# num3 = 72
# fruit[0] = 'cranberry'
# print(person['favorite_team'])
# print(pizza_toppings[7])
#   print(boolean)
# fruit.append('raspberry')
# fruit.pop(1)