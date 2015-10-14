import turtle

window = turtle.Screen()
window.bgcolor("blue")

g_square = turtle.Turtle()
g_square.color('pink')

g_circle = turtle.Turtle()
g_circle.color('green')

def draw_flower():
     for b in range(1,37):
         square(150)
         g_square.right(10)

     for a in range(1,5):
         circle(75)
         g_circle.right(90)

     window.exitonclick()    
         


def square(side):
    for i in range(1,5):
      g_square.forward(side)
      g_square.right(90)  

def circle(radius):
    g_circle.circle(radius)

draw_flower()
