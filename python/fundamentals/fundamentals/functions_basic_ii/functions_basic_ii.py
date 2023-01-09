# 1
def countdown(num):
  list = []
  while num >= 0:
    list.append(num)
    num -= 1
  return list

print(countdown(5))

# 2
def print_and_return(list):
  print(list[0])
  return list[1]

print(print_and_return([1,2]))

# 3
def first_plus_length(list):
  return list[0] + len(list)

print(first_plus_length([1,2,3,4,5]))

# 4
def values_greater_than_seconds(list):
  new_list = []
  if len(list) < 2:
    return False
  for int in range(len(list)):
    if list[int] >= list[2]:
      new_list.append(list[int])
  return new_list

print(values_greater_than_seconds([5,2,3,2,1,4]))
print(values_greater_than_seconds([3]))

# 5
def length_and_value(size, value):
  list = []
  for int in range(size):
    list.append(value)
  return list

print(length_and_value(4,7))
print(length_and_value(6,2))