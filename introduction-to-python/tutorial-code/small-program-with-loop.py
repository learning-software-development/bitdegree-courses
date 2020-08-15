a = []
n = input("How many items do you want to submit: ")
n = int(n)
x = 0

while x < n:
  i = input("Input %d: " % (x+1))
  a.insert(x, i)
  x += 1

print(a)

a = sorted(a)
print("We have sorted this list: ")
x = 0
while x < n:
  print(a[x])
  x += 1

# How many items do you want to submit: 3
# Input 1: Apple
# Input 2: Pear
# Input 3: Grape
# ['Apple', 'Pear', 'Grape']
# We have sorted this list:
# Apple
# Grape
# Pear
