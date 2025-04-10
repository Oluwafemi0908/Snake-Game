from turtle import Turtle, Screen
import time

screen = Screen()


class Snake:
    def __init__(self):
        self.snake_body = 10
        self.snake_body_list = []
        self.x_cor = 0
        self.y_cor = 0
        self.num = 4
        self.head = ''
        self.tail = ''

    def create_snake(self):
        for body in range(1, self.snake_body + 1):
            s = Turtle()
            s.penup()
            self.x_cor = s.xcor()
            self.x_cor -= (body - 1) * 4
            self.y_cor = s.ycor()
            s.shape('square')
            s.color('white')
            s.shapesize(0.2)
            s.setpos(self.x_cor, self.y_cor)
            self.snake_body_list.append(s)
        self.head = self.snake_body_list[0]

    def add_body(self):
        self.tail = self.snake_body_list[-1]
        self.x_cor = self.tail.xcor()
        self.y_cor = self.tail.ycor()

        tail_pos = self.tail.pos()
        self.snake_body += 5
        for body in range(len(self.snake_body_list), self.snake_body + 1):
            s = Turtle()
            s.penup()
            s.shape('square')
            s.color('white')
            s.shapesize(0.2)
            s.speed('fastest')
            self.snake_body_list.append(s)
            self.follow_head()

    def follow_head(self):
        for segment in range(len(self.snake_body_list) - 1, 0, -1):
            prev_x_cor = self.snake_body_list[segment - 1].xcor()
            prev_y_cor = self.snake_body_list[segment - 1].ycor()
            self.snake_body_list[segment].setpos(prev_x_cor, prev_y_cor)
        self.head.forward(self.num)
        screen.update()
        time.sleep(1 / (self.snake_body*2))

    def move_forward(self):
        self.follow_head()

    def east(self):
        if self.head.heading() != 180:
            self.head.setheading(0)
            self.num = 5
            self.move_forward()
            self.num = 5
            self.follow_head()

    def west(self):
        if self.head.heading() != 0:
            self.head.setheading(180)
            self.num = 5
            self.move_forward()
            self.num = 5
            self.follow_head()

    def north(self):
        if self.head.heading() != 270:
            self.head.setheading(90)
            self.num = 5
            self.move_forward()
            self.num = 5
            self.follow_head()

    def south(self):
        if self.head.heading() != 90:
            self.head.setheading(270)
            self.num = 5
            self.move_forward()
            self.num = 5
            self.follow_head()
