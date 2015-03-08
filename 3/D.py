def recursive_squares(turtle, rec_depth=200, offset = 0.2, length=100):
    angle =  degrees(atan(length*offset/(length-length*offset)))
    for i in range(rec_depth):
        for j in range(4): #draw square
            turtle.forward(length)
            turtle.right(90)
        turtle.penup()
        turtle.forward(length*offset)
        turtle.pendown()
        turtle.right(angle)