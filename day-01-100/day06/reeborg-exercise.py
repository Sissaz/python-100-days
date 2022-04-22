# Reeborg World Exercise
# Virando o Reeborg:
# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Alone&url=worlds%2Ftutorial_en%2Falone.json

def turn_right():
    turn_left()
    turn_left()
    turn_left()
turn_left()
move()
turn_right()
move()
turn_right()
move()
turn_right()
move()

# Reeborg World Exercise
# Levando Reeborg até o final:
# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%201&url=worlds%2Ftutorial_en%2Fhurdle1.json

move()
turn_left()
def turn_around():
    turn_left()
    turn_left()
    turn_left()
    move()
def turn_around_2():
    turn_around()
    turn_around()
def caminho():
    move()
    turn_around_2()
    turn_left()
    move()
    turn_left()
for caminhar in range(5):
    caminho()
move()
turn_around_2()

#
