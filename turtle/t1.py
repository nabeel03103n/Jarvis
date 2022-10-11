from turtle import Turtle
import random

root = Turtle()
color = ['red','blue','green','brown','black','purple','yellow']
col = random.choice(color)
root.goto(0,0)

root.left(0)
root.forward(200)

root.left(90)
root.forward(80)

root.left(90)
root.forward(80)

root.right(40)
root.forward(80)

root.left(40)
root.forward(80)

root.left(40)
root.forward(80)

root.right(40)
root.forward(80)

root.left(90)
root.forward(80)

root.left(90)
root.forward(80)
root.forward(90)

root.backward(100)
root.right(90)
root.backward(20)
root.circle(30)


