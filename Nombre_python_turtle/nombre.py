import turtle

tortuga = turtle.Turtle()
tortuga.pensize(15)
tortuga.color("purple")
tortuga.shape('turtle')
tortuga.right(-180)
numbers = 1
tortuga.speed(0)
for i in range(10):
    numbers *= 2
    tortuga.circle(numbers)
