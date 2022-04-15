## Tip Calculator

# Instructions

If the bill was $150.00, split between 5 people, with 12% tip. 

Each person should pay (150.00 / 5) * 1.12 = 33.6

Format the result to 2 decimal places = 33.60

Thus everyone's share of the total bill is $30.00 plus a $3.60 tip.

Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪


# Example Input

```
Welcome to the tip calculator!
What was the total bill? $124.56
How much tip would you like to give? 10, 12, or 15? 12
How many people to split the bill? 7
```

# Example Output

```
Each person should pay: $19.93
```

## Tip Calculator


#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
first_tip = 10
second_tip = 12
third_tip = 15

print("Welcome to the tip calculator!")
bill = input(f"What was the total bill? $")
bill_float = float(bill)

tip = input(f"What percentage tip would you like to give? 10, 12 or 15? ")
tip_float = float(tip)
tip_float /= 100

people = input(f"How many people to split the bill? ")
people_int = int(people)

result = (((bill_float * tip_float) + bill_float)/people_int)
final_result = round(result, 2)
final_result = "{:.2f}".format(result)

print(f"Each person should pay: ${final_result}")
