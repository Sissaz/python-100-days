## BMI Calculator

# UPDATE
We've moved away from repl.it for coding exercises.
Check out the new exercises on Coding Rooms with automated submissions.

Login to your Udemy course and head over to the link below to get the sign up link:

[Click here](https://www.udemy.com/course/100-days-of-code/learn/lecture/17825914#questions)

# Instructions

Write a program that calculates the Body Mass Index (BMI) from a user's weight and height.

The BMI is a measure of some's weight taking into account their height. e.g. If a tall person and a short person both weigh the same amount, the short person is usually more overweight.

The BMI is calculated by dividing a person's weight (in kg) by the square of their height (in m):

![](https://cdn.fs.teachablecdn.com/jKHjnLrNQjqzdz3MTMyv)

**Warning** you should convert the result to a whole number. 

# Example Input

```
weight = 80
```

```
height = 1.75
```

# Example Output

80 ÷ (1.75 x 1.75) =  26.122448979591837

```
26
```

e.g. When you hit **run**, this is what should happen:  

![](https://cdn.fs.teachablecdn.com/wmjVjddeSmGj0QVtOUrE)
             
######################
             
# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
h = float(height)
w = int(weight)
BMI = str(w/(h**2))


print("Your BMI is: " + BMI[0]+BMI[1])

## Ou:

#BMI = (w/(h**2))
#BMI_int = int(BMI)
#print(BMI_int)
