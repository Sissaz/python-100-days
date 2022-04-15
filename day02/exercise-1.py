## Data Types

# UPDATE
We've moved away from repl.it for coding exercises.
Check out the new exercises on Coding Rooms with automated submissions.

Login to your Udemy course and head over to the link below to get the sign up link:

[Click here](https://www.udemy.com/course/100-days-of-code/learn/lecture/17825914#questions)

# Instructions

Write a program that adds the digits in a 2 digit number. e.g. if the input was 35, then the output should be 3 + 5 = 8

**Warning.** Do not change the code on lines 1-3. Your program should work for different inputs. e.g. any two-digit number.

# Example Input

```
39
```

# Example Output

3 + 9 = 12

```
12
```

e.g. When you hit **run**, this is what should happen:  

![](https://cdn.fs.teachablecdn.com/iyJTPDDRRJCB1gmdVQMS)
             
###############################################################             
# 🚨 Don't change the code below 👇
two_digit_number = input("Type a two digit number: ")
# 🚨 Don't change the code above 👆
####################################
#Write your code below this line 👇
print(type(two_digit_number))

first_digit = (two_digit_number[0])
second_digit = (two_digit_number[1])

result = int(first_digit) + int(second_digit)
print(result)

#
