# Step 1: Make all the "turtle" commands available to us.
import turtle

# Step 2: create a new turtle, we'll call him bob and make him look like a turtle
bob = turtle.Turtle()
bob.shape("turtle")

# Step 3: lets make Bob draw a blue star
bob.color("blue")

# Lets draw a star!
for i in range(3):
    bob.forward(200)
    bob.left(120)
    

