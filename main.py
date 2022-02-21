import turtle #1 Import modules
import random

#Part A
window = turtle.Screen() #2 Create a screen
window.bgcolor('lightblue')

michelangelo = turtle.Turtle() #3 Create two turtles
leonardo = turtle.Turtle()
michelangelo.color('orange')
leonardo.color('green')
michelangelo.shape('turtle')
leonardo.shape('turtle')

michelangelo.up() #4 Pick up the pen so we don’t get lines
leonardo.up()
michelangelo.goto(-100,20)
leonardo.goto(-100,-20)

#5 Your code goes here
def race_1():
  michelangelo.forward(random.randrange(1,101))
  leonardo.forward(random.randrange(1,101))
race_1()
michelangelo.goto(-100,20)
leonardo.goto(-100,-20)

def race_2():
  for i in range(10):
    michelangelo.forward(random.randrange(0,11))
    leonardo.forward(random.randrange(0,11))
race_2()
michelangelo.goto(-100,20)
leonardo.goto(-100,-20)
#Are these the right thing to do?

#Part B
color = ["blue","purple","white","black"]
leonardo.goto(-50,90)
def turtle_drawing(size):
  angle = 360/size
  length = 60
  for i in range(int(size)):
    leonardo.down()
    leonardo.forward(length)
    leonardo.right(angle)
    leonardo.up()
  leonardo.clear()
  leonardo.down()
turtle_drawing(3)
leonardo.color(color[0])
turtle_drawing(4)
leonardo.color(color[1])
turtle_drawing(6)
leonardo.color(color[2])
turtle_drawing(9)
leonardo.color(color[3])
turtle_drawing(12)
#How to make this part not repeatitive? How to put this in a loop/function?
window.exitonclick()