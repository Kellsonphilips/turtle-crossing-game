import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle Busy Road Crossing")
screen.tracer(0)

car_collection = CarManager()
player = Player()
score = Scoreboard()

screen.listen()
screen.onkey(player.up, "Up")

game_starts = True

while game_starts:
    time.sleep(0.1)
    screen.update()

    car_collection.create_car()
    car_collection.move_cars()

    # Detect collision with car
    for car in car_collection.all_cars:
        if car.distance(player) < 20:
            game_starts = False
            score.game_over()

    # Detect reaching finished line
    if player.cross_finish_line():
        score.level_up()
        player.go_to_start()
        car_collection.increase_speed()

screen.exitonclick()
