import turtle

# Create a turtle object.
t = turtle.Turtle()

# Draw the face.
t.penup()
t.goto(0, -100)
t.pendown()
t.circle(100)

# Draw the eyes.
t.penup()
t.goto(-20, 60)
t.pendown()
t.circle(20)
t.penup()
t.goto(20, 60)
t.pendown()
t.circle(20)

# Draw the nose.
t.penup()
t.goto(0, 0)
t.pendown()
t.forward(50)
t.right(90)
t.forward(20)
t.left(90)
t.forward(50)

# Draw the mouth.
t.penup()
t.goto(0, -20)
t.pendown()
t.right(45)
t.forward(40)
t.left(45)
t.forward(40)

# Finish the drawing.
t.done()
