import random
from turtle import Turtle


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape('circle')
        self.color('blue')
        self.shapesize(0.2)
        self.new_food()
        self.speed('fastest')


    def new_food(self):
        x_cor = random.randint(-28, 28) * 10
        y_cor = random.randint(-28, 28) * 10
        self.setpos(x_cor, y_cor)

