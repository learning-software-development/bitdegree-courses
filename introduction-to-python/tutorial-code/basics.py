# The basics of Python Syntax

system = "Python"
greeting_message = "Hello there, " + system+ " world!"

print(greeting_message)


name = input("Please enter your name: ")
print("Your name is", name)

if name == "Spiderman":
  print("With great power there must also come great responsibility.")
elif name == "Batman":
  print("He's the hero Gotham deserves, but not the one it needs right now.")
else:
  print("Victory needs no explanation, defeat allows none.")

running = True
options = ["Play some games", "Do a task around the house", "Contribute to open source"]

while running:
  c = 1
  for x in options:
    print("%d. %s" % (c, x))
    c += 1

  value = input("What would you like to do: ")
  print("You have decided to %s (%s)" % (options[int(value)-1], value))
  running = False
