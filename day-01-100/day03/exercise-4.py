## Pizza Order
# Instructions

Congratulations, you've got a job at Python Pizza. Your first job is to build an automatic pizza order program. 

Based on a user's order, work out their final bill. 

```
Small Pizza: $15
```

```
Medium Pizza: $20
```

```
Large Pizza: $25
```

```
Pepperoni for Small Pizza: +$2
```

```
Pepperoni for Medium or Large Pizza: +$3
```

```
Extra cheese for any size pizza: + $1
```

# Example Input

```
size = "L"
```

```
add_pepperoni = "Y"
```

```
extra_cheese = "N"
```

# Example Output

```
Your final bill is: $28.
```

#

## Pizza Order

# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
print("Case-sensitive Script!")
size = input("What size pizza do you want? S, M, or L: ")
add_pepperoni = input("Do you want pepperoni? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
pizza_small = 15
pizza_medium = 20
pizza_large = 25


if size == "S":
  if add_pepperoni == "N":
    pizza_small = 15
  else:
    pizza_small += 2
  if extra_cheese == "N":
    pizza_small
    print(f"Your final bill is: ${pizza_small}.")
  else:
    pizza_small += 1
    print(f"Your final bill is: ${pizza_small}.")
    
if size == "L":
  if add_pepperoni == "N":
    pizza_large = 25
  else:
    pizza_large += 3
    if extra_cheese == "N":
      pizza_large
      print(f"Your final bill is: ${pizza_large}.")
    else:
      pizza_large += 1
      print(f"Your final bill is: ${pizza_large}.")  

if size == "M":
  if add_pepperoni == "N":
    pizza_medium = 20
  else:
    pizza_medium += 3
    if extra_cheese == "N":
      pizza_medium
      print(f"Your final bill is: ${pizza_medium}.")
    else:
      pizza_medium += 1
      print(f"Your final bill is: ${pizza_medium}.")
  
