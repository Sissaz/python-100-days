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
     
   
# Mais Rapido:

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
    if front_is_clear():
        move()
        if at_goal():
            break

 

        
