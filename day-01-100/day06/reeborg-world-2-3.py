# For and While

for item in list_of_items:
	#Do something to each item

for number in range(a,b):
	print(number)
  
while something_is_true:
  #Do something repeatedly

# Reeborg World 2 Exercise

# Chasing the Flag!

# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%202&url=worlds%2Ftutorial_en%2Fhurdle2.json

def virar():
    turn_left()
    turn_left()
    turn_left()
def caminho():
    move()
    turn_left()
    move()
    virar()
    move()
    virar()
    move()
    turn_left()
while not at_goal():
    caminho()
    if at_goal()is True:
        break
	
	
# Reeborg World 3 Exercise

# The position and number of hurdles changes each time this world is reloaded.

# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%203&url=worlds%2Ftutorial_en%2Fhurdle3.json

def virar():
    turn_left()
    turn_left()
    turn_left()
def parede():
    turn_left()
    move()
    virar()
    move()
    virar()
    move()
    turn_left()
while not at_goal():
    if front_is_clear():
        move()
    elif wall_in_front():
        parede()

