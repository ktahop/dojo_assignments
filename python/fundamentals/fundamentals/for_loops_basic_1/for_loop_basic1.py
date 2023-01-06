# 1
for int in range(0,151):
  print(int)

# 2
for int in range(5,1001):
  if int%5 == 0:
    print(int)

# 3
for int in range(1, 1001):
  if int%10 == 0:
    print("Coding Dojo")
  elif int%5 == 0:
    print("Coding")
  else:
    print(int)

# 4
sum = 0
for int in range(0,500001):
  if int%2 != 0:
    sum += int
print(sum)

# 5
for int in range(2018,0,-4):
  print(int)

# 6
lowNum = 2
highNum = 9
multi = 3
for int in range(lowNum, highNum+1):
  if int%multi == 0:
    print(int)