import turtle
import randome
t = turtle.Turtle()
colors = [
    "lime",
    "coral",
    "navy",
    "violet",]
t.speed (-1)
t.pencoler(randome.choice(colors))
f = 300
for i in range (100):
    for _ in range (4):
        t. forward(200)
        t. left(90)
        t. left (3.6)
