#PART 1 - IMPORT AND SCREEN SETUP
import turtle
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Neon Mandela")

#PART 2 - CREATE THE TURTLE PEN 
board =turtle.Turtle()
board.speed("fastest")
board.hideturtle()

#PART 3 - OUTER COLOR SPIRAL (MOVEMENT + LOOPS + COLOR)
colours = ["red", "orange", "yellow", "lime", "cyan", "violet", "pink", "white"]
for i in range(80):
    board.color(colours[i % len(colours)])
    board.width(2)
    board.forward(i - 2)
    board.right(91)

#PART 4 - PEN CONTROL:
board.penup()
board.goto(0, -60)
board.setheading(90)
board.pendown()
board.color("gold", "yellow")
board.begin_fill()
for i in range(5):
    board.forward(130)
    board.right(144)
board.end_fill()

board.penup()
board.goto(0, 0)
board.pendown()
petal_colors = ["cyan","lime","violet","orange", "deepink"]

for i in range(4):
    board.forward(55)
    board.right(90)
board.end_fill()
board