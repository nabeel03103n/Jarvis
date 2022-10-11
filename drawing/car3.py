import turtle

def draw():
    turtle.delay(10)
    turtle.pensize(20)

    # Move the turtle to the extreme left position
    turtle.penup()
    turtle.setposition(-200,-75)

    # Draw the rectangle
    turtle.pendown()
    turtle.forward(400)
    turtle.setheading(90)
    turtle.forward(150)
    turtle.setheading(180)
    turtle.forward(400)
    turtle.setheading(-90)
    turtle.forward(150)

    # Draw the left tire
    turtle.penup()
    turtle.setposition(-175,-75)
    turtle.pendown()
    turtle.forward(50)
    turtle.setheading(0)
    turtle.forward(75)
    turtle.setheading(90)
    turtle.forward(50)

    # Draw the right tire
    turtle.penup()
    turtle.setposition(100,-75)
    turtle.pendown()
    turtle.setheading(270)
    turtle.forward(50)
    turtle.setheading(0)
    turtle.forward(75)
    turtle.setheading(90)
    turtle.forward(50)

    # Draw the uppermost line
    turtle.penup()
    turtle.setposition(-137.5,200)
    turtle.pendown()
    turtle.setheading(0)
    turtle.forward(275)

    # Draw the second uppermost line
    turtle.penup()
    turtle.setposition(-150,150)
    turtle.pendown()
    turtle.setheading(0)
    turtle.forward(300)

    # Draw the left slanted line
    turtle.penup()
    turtle.setposition(-137.5,200)
    turtle.pendown()
    turtle.setposition(-175,75)

    # Draw the right slanted line
    turtle.penup()
    turtle.setposition(137.5,200)
    turtle.pendown()
    turtle.setposition(175,75)

    # Draw the left circle
    turtle.penup()
    turtle.setposition(-125,-25)
    turtle.pendown()
    turtle.circle(25)

    # Draw the right circle
    turtle.penup()
    turtle.setposition(125,-25)
    turtle.pendown()
    turtle.circle(25)

    # Draw the left wiper
    turtle.penup()
    turtle.setposition(-87.5, 75)
    turtle.pendown()
    turtle.setposition(-50, 112.5)

    # Draw the right wiper
    turtle.penup()
    turtle.setposition(62.5, 75)
    turtle.pendown()
    turtle.setposition(100, 112.5)

    # Draw the horizontal lines
    turtle.penup()
    turtle.setposition(-50, -37.5)
    turtle.pendown()
    turtle.setposition(-50, 0)
    turtle.penup()
    turtle.setposition(-15, -37.5)
    turtle.pendown()
    turtle.setposition(-15, 0)
    turtle.penup()
    turtle.setposition(15, -37.5)
    turtle.pendown()
    turtle.setposition(15, 0)
    turtle.penup()
    turtle.setposition(50, -37.5)
    turtle.pendown()
    turtle.setposition(50, 0)