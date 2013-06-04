# Polygon excercise from Week 0

# Name: Hunter Perry


from TurtleWorld import *   	
world = TurtleWorld()			
bob = Turtle()				
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
