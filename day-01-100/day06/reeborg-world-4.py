# Reeborg World 4 Exercise

# The position, the height and the number of hurdles changes each time this world is reloaded.

# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%204&url=worlds%2Ftutorial_en%2Fhurdle4.json


# Mais Lento:

def virar():
    turn_left()
    turn_left()
    turn_left()
while not at_goal():
    if wall_in_front():
        turn_left()
        move()
        virar()
        if front_is_clear():
            move()
            virar()
            move()
            while front_is_clear():
                move()
            if wall_in_front():
                turn_left()
    if front_is_clear():
        move()
    if at_goal():
        break
     
   
# Mais Rapido (melhor):

def virar():
    turn_left()
    turn_left()
    turn_left()
while not at_goal():
    if wall_in_front():
        turn_left()
        move()
        while wall_on_right():
            move()
        if right_is_clear():
            virar()
            move()
            virar()
            move()
            while front_is_clear():
                move()
            if wall_in_front():
                turn_left()                
    elif front_is_clear():
        move()
    elif at_goal():
        break
