## Heads or Tails

# Instructions

You are going to write a virtual coin toss program. It will randomly tell the user "Heads" or "Tails". 

**Important**, the first letter should be capitalised and spelt exactly like in the example e.g. Heads, not heads.

There are many ways of doing this. But to practice what we learnt in the last lesson, you should generate a random number, either 0 or 1. Then use that number to print out Heads or Tails.

e.g.
1 means Heads
0 means Tails 

# Example Output

```
Heads
```

or

```
Tails
```

## Heads or Tails

#Write your code below this line 👇
#Hint: Remember to import the random module first. 🎲

import random

dados = random.randint(0,1)

if dados == 1:
  print("Heads")
elif dados == 0:
  print("Tails")
  
  
