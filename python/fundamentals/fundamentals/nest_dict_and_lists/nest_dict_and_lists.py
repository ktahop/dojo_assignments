# Update Values in Dictionaries and Lists
x = [[5,2,3], [10,8,9]] 
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [{'x': 10, 'y': 20}]

# 1
x[1][0] = 15
print(x)

# 2
students[0]["last_name"] = "Bryant"
print(students)

# 3
sports_directory["soccer"][0] = "Andres"
print(sports_directory["soccer"])

# 4
z[0]["y"] = 30
print(z)

print(" ") # Used to seperate assignments

# Iterate Through a Listy of Dictionaries
students = [
  {'first_name': 'Michael', 'last_name' : 'Jordan'},
  {'first_name': 'John', 'last_name' : 'Rosales'},
  {'first_name': 'Mark', 'last_name' : 'Guillen'},
  {'first_name': 'KB', 'last_name' : 'Tonel'}
]

def iterateDictionary(some_list):
  name = ""
  for i in some_list:
    for key, val in i.items():
      if key == "first_name":
        name = f"{key} - {val}, "
      else:
        name += f"{key} - {val}"
    print(name)

iterateDictionary(students) 

print(" ")

# Get Values From a List of Dictionaries
def iterateDictionary2(key_name, some_list):
  for i in some_list:
    print(i[key_name])

iterateDictionary2('first_name', students)
iterateDictionary2('last_name', students)

print(" ")

# Iterate Through a Dictionary with List Values
dojo = {
  'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
  'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def printInfo(some_dict):
  for key in some_dict:
    print(len(some_dict[key]), key.upper())
    for val in range(len(some_dict[key])):
      print(some_dict[key][val])
    print(" ")

printInfo(dojo)
