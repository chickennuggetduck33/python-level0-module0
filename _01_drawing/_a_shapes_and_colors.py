import turtle

if __name__ == '__main__':
    window = turtle.Screen()
    window.bgcolor('white')

    # This code makes a new Turtle. Pick a new name for the turtle
    bob = turtle.Turtle()

    # Make your turtle's shape 'turtle', .shape('turtle')
    bob.shape('turtle')
    # Set your turtle's speed using .speed(2)
    bob.speed(2)
    # Set your turtle's color using .color('green') and .pencolor('blue')
    bob.color('green')
    bob.pencolor('red')
    # Move your turtle forward using .forward(100)
    bob.forward(100)
    # TEST    Did your turtle move forward?

    # Move your turtle left or right using .left(90) or .right(90)
    for i in range(4):
        bob.left(90)
        bob.forward(100)
    # Now put the forward and left/right code into a for loop to repeat 4 times.
    # TEST    Did your turtle draw a square?

    # Move your turtle to a new place on the screen using .goto(x, y)
    # x=0 and y=0 is the center of the screen
    bob.goto(200, 500)
    bob.goto(200, 200)
    # Have your turtle draw a circle using .circle(radius, steps=30)
    # TEST    Did your turtle draw a circle?

    bob.begin_fill()
    bob.fillcolor('blue')
    bob.circle(radius=10, steps=100)
    # Add color to your shape by adding .begin_fill() before drawing the circle
    # and .end_fill() below
    bob.end_fill()
    # Draw 3 more shapes with different fill colors!
    bob.goto(10, 10)
    bob.begin_fill()
    bob.fillcolor('red')
    bob.circle(radius=10, steps=100)
    bob.end_fill()
    bob.goto(50, 50)
    bob.end_fill()
    bob.begin_fill()
    bob.fillcolor('green')
    bob.circle(radius=10, steps=100)
    bob.end_fill()
    # ===================== DO NOT EDIT THE CODE BELOW ============================
    turtle.done()
