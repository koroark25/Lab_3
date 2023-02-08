import turtle

def square_turtle(x):
    fred = turtle.Turtle()
    fred.color(x)
    fred.forward(100)
    fred.right(90)
    fred.forward(100)
    fred.right(90)
    fred.forward(100)
    fred.right(90)
    fred.forward(100)
    fred.right(90)

square_turtle("cyan")
square_turtle("blue")
square_turtle("green")
square_turtle("gold")
