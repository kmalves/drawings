import turtle

def draw_shapes():
    window = turtle.Screen()
    window.bgcolor("red")

    triangle_equilateral(100)
    square(150)
    circle(100)

    window.exitonclick()

def triangle_equilateral(t_side):
    g_triangle = turtle.Turtle()
    g_triangle.color('blue')
    g_triangle.forward(t_side)
    for i in range(1,3):
      g_triangle.right(120)
      g_triangle.forward(t_side)
      
    
def square(side):
    g_square = turtle.Turtle()
    g_square.color('pink')
    g_square.right(90)
    for i in range(1,5):
      g_square.forward(side)
      g_square.right(90)


def circle(radius):
    g_circle = turtle.Turtle()
    g_circle.color('green')
    g_circle.circle(radius)
    
draw_shapes()     
    

