# Reeborg World Exercise
# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json
# Escape the Maze!

def virar():
    turn_left()
    turn_left()
    turn_left()

while front_is_clear():
    move()
turn_left()
 

while not at_goal():
    if front_is_clear() and wall_on_right():
        move()
    elif front_is_clear() and right_is_clear():
        virar()
        move()
    elif front_is_clear():
        move()
    elif wall_in_front() and right_is_clear():
        virar()
        move()
    else:
        turn_left()
         
