from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.color("black")
        self.level = 0
        self.hideturtle()
        self.level_update()
        self.level_up()

    def level_update(self):
        self.clear()
        self.goto(-280, 260)
        self.write(f"Level: {self.level}", False, align="left", font=FONT)

    def level_up(self):
        self.level += 1
        self.level_update()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", False, align="center", font=FONT)
