import turtle

"""
This is not part of the book. This is my self example of using recursion visualizing as tress branch. 

Each branch is a recursive function call. 
It draws itself, then makes two recursive calls to draw left and right sub-branches. 
When the depth reaches 0, it stops. This is the base case. 
The shape that emerges is a fractal — a classic product of recursion.
"""


def draw_branch(t, length, depth):
    if depth == 0:
        return
    t.forward(length)
    # Left sub-branch
    t.left(30)
    draw_branch(t, length * 0.7, depth - 1)
    # Right sub-branch
    t.right(60)
    draw_branch(t, length * 0.7, depth - 1)
    # Restore heading
    t.left(30)
    t.backward(length)


screen = turtle.Screen()
screen.bgcolor("white")
screen.title("Fractal Tree (Recursive Visualization)")
t = turtle.Turtle()
t.speed(0)
t.color("forestgreen")
t.left(90)
t.penup()
t.goto(0, -250)
t.pendown()

draw_branch(t, length=200, depth=10)
screen.exitonclick()
