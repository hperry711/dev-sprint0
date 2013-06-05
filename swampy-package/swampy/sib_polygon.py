# Polygon excercise from Week 0

# Name: Hunter Perry


from TurtleWorld import *   	
world = TurtleWorld()			
bob = Turtle()				
<<<<<<< HEAD
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
=======
# 2A
world.clear()
bob = Turtle()
fd(bob, 50)
lt(bob)
fd(bob, 50)
lt(bob)
fd(bob, 50)
lt(bob)
fd(bob, 50)
lt(bob)
#2.1 & 2.2
world.clear()
bob = Turtle()
def square(n, length):
    for i in range(4):
        fd(n, length)
        lt(n)
square(bob, 91)
#2.3
world.clear()
bob = Turtle()
world.clear()
bob = Turtle()
def polygon(t, n, length):
    angle = 360.0 / n
    for i in range(n):
        fd(t, length)
        lt(t, angle)
polygon(bob, 10, 40)
def circle(t, r):
    circumference = 2 * math.pi * r
    n = int(circumference / 3) + 1
    length = circumference / n
    polygon(t, n, length)
    



wait_for_user()	
>>>>>>> 03f141be16e38c4fc31cd2ffab237c36c9fee0d0
