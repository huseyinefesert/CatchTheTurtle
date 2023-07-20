import turtle
from turtle import *
from tkinter import *
import time
from random import randint
import random

screen = turtle.Screen()
screen.title("CatchTheTurtle")
screen.bgcolor("white")
game_over = False
score = 0

skor_turtle = turtle.Turtle()
skor_turtle.speed(0)
skor_turtle.color("black")
skor_turtle.penup()
skor_turtle.hideturtle()

time_turtle = turtle.Turtle()
time_turtle.speed(1)
time_turtle.color("black")
time_turtle.penup()
time_turtle.hideturtle()

zaman_turtle = turtle.Turtle()
zaman_turtle.speed(1)
zaman_turtle.color("black")
zaman_turtle.penup()
zaman_turtle.hideturtle()
start = time.monotonic()
time_limit = 20

def zaman_writer(str):
    zaman_turtle.clear()
    zaman_turtle.goto(-50,250)
    zaman_turtle.write(f"{str}: ", align="left", font=("Arial", 15, "normal"))
def time_counter():
    global game_over
    time_turtle.clear()
    time_turtle.goto(25,250)
    remaining_time = (int)(23-time.monotonic()+start)
    time_turtle.write(f"{remaining_time}",align="left",font=("Arial",15,"normal"))
    if remaining_time > 0:
        time_turtle.getscreen().ontimer(time_counter,1000)
    if remaining_time == 0:
        game_over = True
        kaplumbaga.hideturtle()
        time_turtle.clear()
        time_turtle.hideturtle()
        zaman_writer("Oyun Bitti!!!")

def update_score():
    skor_turtle.clear()
    skor_turtle.goto(-50, 280)
    skor_turtle.write(f"Skor: {score}", align="left", font=("Arial", 15, "normal"))

def increase_score():
    global score
    score += 1
    update_score()

kaplumbaga = turtle.Turtle()
kaplumbaga.shape("turtle")
kaplumbaga.color("magenta")
kaplumbaga.shapesize(2)
def get_turtle():
    global game_over
    kaplumbaga.penup()

    if not game_over:
        x = random.randint(-200, 200)
        y = random.randint(-200, 200)
        kaplumbaga.penup()
        kaplumbaga.hideturtle()
        kaplumbaga.goto(x,y)
        kaplumbaga.showturtle()

        kaplumbaga.getscreen().ontimer(get_turtle, 500)
def on_click(a,b):
    if not game_over:
        if kaplumbaga.distance(a,b)<20:
            increase_score()

screen.listen()
screen.onscreenclick(on_click)
zaman_writer("Zaman")
update_score()
time_counter()
get_turtle()

turtle.mainloop()