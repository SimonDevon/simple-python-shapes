# Step 1: Make all the "turtle" commands available to us.
import turtle

# Step 2: create a new turtle, we'll call him bob and make him look like a turtle
bob = turtle.Turtle()
bob.shape("turtle")

# Step 3: lets make Bob use a red pen
bob.color("red")

# Lets draw a star!
for i in range(5):
    bob.forward(200)
    bob.right(144)
    

