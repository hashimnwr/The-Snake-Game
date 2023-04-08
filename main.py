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
screen.onkey(key='Up', fun=snape.up, )
screen.onkey(key='Down', fun=snape.down, )
screen.onkey(key='Left', fun=snape.left, )
screen.onkey(key='Right', fun=snape.right, )


screen.update()
game_on = True

while game_on:
    screen.update()
    sleep(0.05)
    snape.move()
    if snape.head.distance(food) < 15:
        food.refresh()
        snape.extend()
        scoreboard.increase_score()

    if snape.head.xcor() < -290 or snape.head.xcor() > 290 or snape.head.ycor() < -290 or snape.head.ycor() > 290:
        game_on = False
        scoreboard.game_over()

    for segment in snape.segments[1:]:
        if snape.head.distance(segment) < 5:
            game_on = False
            scoreboard.game_over()

screen.exitonclick()
