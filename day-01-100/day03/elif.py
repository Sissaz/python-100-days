# elif

height = int(input("What is your height in cm? "))

if height >= 120:
  print("You can ride the rollercoaster!")
  age = int(input("What is your age? "))
  if age < 12:
    print("Please pay $5.")
  elif age <= 18:
    print("Please pay $7.")
    
 # We can add how many elif we want to.

  else:
    print("Please pay $12.")
else:
  print("Sorry, you have to grow taller before you can ride.")
