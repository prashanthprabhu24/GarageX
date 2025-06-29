import turtle

"""
This is not part of the book. This is my self example of using recursion visualized in geometry.
Each triangle is drawn from recursion call 
"""


def draw_triangle(points, color, t):
    t.fillcolor(color)
    t.up()
    t.goto(points[0])
    t.down()
    t.begin_fill()
    for point in points[1:] + [points[0]]:
        t.goto(point)
    t.end_fill()


def get_mid(p1, p2):
    return [(p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2]


def sierpinski(points, depth, t):
    colormap = ['blue', 'red', 'green', 'white', 'yellow', 'violet', 'orange']
    draw_triangle(points, colormap[depth], t)
    if depth > 0:
        sierpinski([points[0],
                    get_mid(points[0], points[1]),
                    get_mid(points[0], points[2])],
                   depth - 1, t)
        sierpinski([points[1],
                    get_mid(points[0], points[1]),
                    get_mid(points[1], points[2])],
                   depth - 1, t)
        sierpinski([points[2],
                    get_mid(points[2], points[1]),
                    get_mid(points[0], points[2])],
                   depth - 1, t)


t = turtle.Turtle()
t.speed(0)
screen = turtle.Screen()
screen.bgcolor("black")
points = [[-200, -100], [0, 200], [200, -100]]
sierpinski(points, 4, t)
screen.exitonclick()
