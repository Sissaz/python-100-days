## BMI Calculator 2.0

# Instructions

Write a program that interprets the Body Mass Index (BMI) based on a user's weight and height.

It should tell them the interpretation of their BMI based on the BMI value.

- Under 18.5 they are underweight
- Over 18.5 but below 25 they have a normal weight
- Over 25 but below 30 they are slightly overweight
- Over 30 but below 35 they are obese
- Above 35 they are clinically obese.

![](https://cdn.fs.teachablecdn.com/qTOp8afxSkGfU5YGYf36)

The BMI is calculated by dividing a person's weight (in kg) by the square of their height (in m):

![](https://cdn.fs.teachablecdn.com/jKHjnLrNQjqzdz3MTMyv)

**Warning** you should **round** the result to the nearest whole number. The interpretation message needs to include the words in bold from the interpretations above. e.g. **underweight, normal weight,  overweight, obese, clinically obese**. 

# Example Input

```
weight = 85
```

```
height = 1.75
```

# Example Output

85 ÷ (1.75 x 1.75) =  27.755102040816325

```
Your BMI is 28, you are slightly overweight.
```

e.g. When you hit **run**, this is what should happen:   

![](https://cdn.fs.teachablecdn.com/mGRynIETXuVqoDk8unci)

The testing code will check for print output that is formatted like one of the lines below:

```
"Your BMI is 18, you are underweight."
"Your BMI is 22, you have a normal weight."
"Your BMI is 28, you are slightly overweight."
"Your BMI is 33, you are obese."
"Your BMI is 40, you are clinically obese."
```

## BMI Calculator 2.0

height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
result = ((weight)/(height**2))
result = (round(result))
if result < 18.5:
  print(f"Your BMI is {result}, you are underweight.")
elif 18.5 < result < 25:
  print(f"Your BMI is {result}, you have a normal weight.")
elif 25 < result < 30:
  print(f"Your BMI is {result}, you are slightly overweight.")
elif 30 < result < 35:
  print(f"Your BMI is {result}, you are obese.")
else:
  print(f"Your BMI is {result}, you are clinically obese.")

##
  
# enter your height in m: 1.60
# enter your weight in kg: 60
# Your BMI is 23, you have a normal weight.

