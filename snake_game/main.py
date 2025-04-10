from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard

is_on = True


def play_game():
    screen = Screen()
    screen.setup(width=600, height=600)
    screen.bgcolor('black')
    screen.title('Snake Game')
    screen.tracer(0)
    global is_on
    snake = Snake()
    food = Food()
    scoreboard = Scoreboard()

    snake.create_snake()
    screen.listen()

    screen.onkey(snake.east, 'Right')
    screen.onkey(snake.west, 'Left')
    screen.onkey(snake.north, 'Up')
    screen.onkey(snake.south, 'Down')
    while is_on:
        snake.move_forward()

        if snake.head.distance(food) <= 8:
            food.new_food()
            snake.add_body()
            scoreboard.increase_score()

        if (snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() <
                -290):
            scoreboard.game_over()
            is_on = False

        for segment in snake.snake_body_list[1:]:
            if snake.head.distance(segment) < 4:
                scoreboard.game_over()
                is_on = False

    if not is_on:
        restart = screen.textinput('restart', "Restart")
        if restart == 'r':
            screen.clearscreen()
            is_on = True
            play_game()

    screen.exitonclick()


play_game()
