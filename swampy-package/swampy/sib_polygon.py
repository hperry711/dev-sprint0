# Polygon excercise from Week 0

# Name: Hunter Perry


from TurtleWorld import * 		
world = TurtleWorld()			
bob = Turtle()				
def square(turtle, n):
    for i in range(4):
    fd(turtle, n)
    lt(turtle)
square(bob, 90)

def polygon(turtle, length, n):
    for i in range(n):
    fd(turtle, length)
    lt(turtle, (360.0/n))
polygon(bob, 5, 100)

def circle(turtle, radius):
    polygon(turtle, radius, 9)
circle(bob, 40)

def arc(turtle, radius, theta):
    for i in range(theta):
    fd(turtle, ((math.pi * radius * 2) / 360))
    lt(turtle, 1)

arc(bob, 8, 90)



wait_for_user()					
