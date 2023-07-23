while front_is_clear():
    move()
    turn_left()
 
while not at_goal():
    if front_is_clear() and wall_on_right():
        move()
    elif front_is_clear() and right_is_clear():
        for _ in range(3):
            turn_left()
        move()
    elif front_is_clear():
        move()
    elif wall_in_front() and right_is_clear():
        for _ in range(3):
            turn_left()
        move()
    else:
        turn_left()