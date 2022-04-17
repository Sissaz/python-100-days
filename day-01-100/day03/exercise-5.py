## Love Calculator

# 💪 This is a Difficult Challenge 💪

# Instructions

You are going to write a program that tests the compatibility between two people.  

To work out the love score between two people:

> Take both people's names and check for the number of times the letters in the word TRUE occurs. Then check for the number of times the letters in the word LOVE occurs. Then combine these numbers to make a 2 digit number. 


For Love Scores **less than 10** or **greater than 90**, the message should be:

`"Your score is **x**, you go together like coke and mentos."` 

For Love Scores **between 40** and **50**, the message should be:

`"Your score is **y**, you are alright together."`

Otherwise, the message will just be their score. e.g.:

`"Your score is **z**."`

e.g. 

`name1 = "Angela Yu"`

`name2 = "Jack Bauer"`

T occurs 0 times

R occurs 1 time

U occurs 2 times

E occurs 2 times

Total = 5

L occurs 1 time

O occurs 0 times

V occurs 0 times

E occurs 2 times

Total = 3

Love Score = 53

Print: "Your score is 53."

# Example Input 1

```
name1 = "Kanye West"
```

```
name2 = "Kim Kardashian"
```

# Example Output 1

```
Your score is 42, you are alright together.
```

# Example Input 2

```
name1 = "Brad Pitt"
```

```
name2 = "Jennifer Aniston"
```

# Example Output 2

```
Your score is 73.
```

## Love Calculator

# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

#True
name1_1_lower = name1.lower()
name1_2_lower = name1.lower()
name1_3_lower = name1.lower()
name1_4_lower = name1.lower()

name1_1_count = name1_1_lower.count("t")
name1_2_count = name1_2_lower.count("r")
name1_3_count = name1_3_lower.count("u")
name1_4_count = name1_4_lower.count("e")

result_name_1 = name1_1_count + name1_2_count + name1_3_count + name1_4_count

name2_1_lower = name2.lower()
name2_2_lower = name2.lower()
name2_3_lower = name2.lower()
name2_4_lower = name2.lower()

name2_1_count = name2_1_lower.count("t")
name2_2_count = name2_2_lower.count("r")
name2_3_count = name2_3_lower.count("u")
name2_4_count = name2_4_lower.count("e")

result_name_2 = name2_1_count + name2_2_count + name2_3_count + name2_4_count

result_true = int((result_name_1) + (result_name_2))


#Love

name3_1_lower = name1.lower()
name3_2_lower = name1.lower()
name3_3_lower = name1.lower()
name3_4_lower = name1.lower()

name3_1_count = name3_1_lower.count("l")
name3_2_count = name3_2_lower.count("o")
name3_3_count = name3_3_lower.count("v")
name3_4_count = name3_4_lower.count("e")

result_name_3 = name3_1_count + name3_2_count + name3_3_count + name3_4_count

name4_1_lower = name2.lower()
name4_2_lower = name2.lower()
name4_3_lower = name2.lower()
name4_4_lower = name2.lower()

name4_1_count = name4_1_lower.count("l")
name4_2_count = name4_2_lower.count("o")
name4_3_count = name4_3_lower.count("v")
name4_4_count = name4_4_lower.count("e")

result_name_4 = name4_1_count + name4_2_count + name4_3_count + name4_4_count

result_love = int((result_name_3) + (result_name_4))


result = int(str(result_true) + str(result_love))

if result < 10 or result > 90:
  print(f"Your score is {result}, you go together like coke and mentos.")
elif result >= 40 and result <= 50:
  print(f"Your score is {result}, you are alright together.")
else:
  print(f"Your score is {result}.")
  
  #
