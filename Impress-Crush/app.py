import turtle

# Create the turtle object
t = turtle.Turtle()

# Set the title of the window
turtle.title("for boyfriend")

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("black")

# Set the color for the heart
t.color("red")
t.fillcolor("red")

# Start drawing the heart
t.begin_fill()
t.left(140)
t.forward(180)
t.circle(-90, 200)
t.setheading(60)
t.circle(-90, 200)
t.forward(100)
t.end_fill()

# Move the turtle to position for the text
t.up()
t.setpos(-80, 150)
t.down()

# Set the color for the text
t.color("white")

# Write the message
t.write("I LOVE YOU", font=("Rockwell Nova", 20, "bold"))

# Hide the turtle after drawing
t.ht()

# Keep the window open
turtle.mainloop()
