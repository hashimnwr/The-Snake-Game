from turtle import Screen
from time import sleep
from snake import Snake
from food import Food
from scores import Score

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

screen.bgcolor('black')
screen.title('The Snake Game')

snape = Snake()
food = Food()
scoreboard = Score()

screen.listen()
screen.onkey(key='Up', fun=snape.up)
screen.onkey(key='Down', fun=snape.down)
screen.onkey(key='Left', fun=snape.left)
screen.onkey(key='Right', fun=snape.right)
screen.onkey(key='q', fun=snape.end_game)


screen.update()


while snape.game_on:
    screen.update()
    sleep(0.03)
    snape.move()
    if snape.head.distance(food) < 15:
        food.refresh()
        snape.extend()
        scoreboard.increase_score()

    if snape.head.xcor() < -290 or snape.head.xcor() > 290 or snape.head.ycor() < -290 or snape.head.ycor() > 290:
        scoreboard.reset()
        snape.reset()
        sleep(3)

    for segment in snape.segments[1:]:
        if snape.head.distance(segment) < 5:
            scoreboard.reset()
            snape.reset()
            sleep(3)

screen.exitonclick()
