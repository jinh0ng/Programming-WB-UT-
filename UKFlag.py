# File: UKFlag.py
# Student:  Yejin Hong
# UT EID:   yh25386
# Course Name: CS303E
# 
# Date:     04/17/24
# Description of Program: drawing UKFlag using turtle graphics

import turtle

# Function to draw a polygon given a list of vertices
def drawPolygon(t, vertices):
    t.penup()
    t.goto(vertices[0])
    t.pendown()
    for vertex in vertices[1:]:
        t.goto(vertex)
    t.goto(vertices[0])

# Function to fill a polygon with a given color
def fillPolygon(t, vertices, color):
    t.fillcolor(color)
    t.begin_fill()
    drawPolygon(t, vertices)
    t.end_fill()

# Function to draw the Union Jack flag
def drawUnionJack():
    # Set up the turtle
    screen = turtle.Screen()
    screen.setup(width=600, height=1000)
    screen.bgcolor("white")
    t = turtle.Turtle()
    t.speed(0)
    t.width(2)

    # Define colors
    myBlue = (0, 36, 125)
    myRed = (207, 20, 43)
    myWhite = (255, 255, 255)

    # Draw blue background
    fillPolygon(t, [(-300, 500), (-300, -500), (300, -500), (300, 500)], myBlue)

    # Draw white diagonal stripes
    fillPolygon(t, [(300, 500), (-300, 500), (-300, 333)], myWhite)
    fillPolygon(t, [(300, -500), (-300, -500), (-300, -333)], myWhite)

    # Draw red diagonal stripes
    fillPolygon(t, [(300, 500), (-300, 500), (-200, 333)], myRed)
    fillPolygon(t, [(300, -500), (-300, -500), (-200, -333)], myRed)

    # Draw horizontal and vertical white stripes
    fillPolygon(t, [(-300, 167), (-300, -167), (300, -167), (300, 167)], myWhite)
    fillPolygon(t, [(-100, 500), (-100, -500), (100, -500), (100, 500)], myWhite)

    # Draw small red crosses
    t.color(myRed)
    t.penup()
    t.goto(-50, 167)
    t.pendown()
    t.goto(-50, -167)
    t.penup()
    t.goto(50, 167)
    t.pendown()
    t.goto(50, -167)
    t.penup()
    t.goto(-100, 83)
    t.pendown()
    t.goto(100, -83)
    t.penup()
    t.goto(100, 83)
    t.pendown()
    t.goto(-100, -83)

    # Hide turtle and display the drawing
    t.hideturtle()
    turtle.done()

# Call the function to draw the Union Jack
drawUnionJack()
