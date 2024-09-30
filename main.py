import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle Road Crossing")
screen.bgcolor("black")
screen.tracer(0)

player = Player()
car_manager = CarManager()
score_board = Scoreboard()

screen.listen()
screen.onkeypress(player.move_forward, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()

    for car in car_manager.cars:
        if player.distance(car) < 20:
            game_is_on = False
            score_board.game_over()

    if player.is_finished():
        score_board.upgrade_score()
        player.reset_position()
        car_manager.increase_speed()

screen.exitonclick()
