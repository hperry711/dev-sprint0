# Flower excercise (4.2) from Week 0

# Name: Hunter Perry


from TurtleWorld import * 		

import math
bob.delay = 0.00001
world.clear()
bob = Turtle()
def arc (turtle, r, arc_angle):

    n_sides = arc_angle				
    segment_length = 2*math.pi*r/360
    turn_angle = 1
    for i in range (n_sides):
	fd (turtle, segment_length)
	lt (turtle, turn_angle)

def petal (turtle, r, arc_angle):

    turn_angle = 180 - arc_angle

    arc (turtle,r, arc_angle)
    lt (bob, turn_angle)
    arc (turtle, r, arc_angle)
    lt (bob, turn_angle)

def flower (turtle, r, n, angle):

    for i in range (n):
	arc_angle = angle
	turn_angle = 360/n  	

	petal (turtle, r, arc_angle)
	lt (turtle, turn_angle)

def move_turtle (turtle, n):

    pu (bob)
    fd (bob, n)
    pd (bob)

radius = 400
arc_theta = 30
n_petals = 10

move_turtle (bob, 200)
flower (bob, radius, n_petals, arc_theta)


wait_for_user()					

