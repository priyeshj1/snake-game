import turtle
import time
import random
import pygame

pygame.mixer.init()
eat_sound = pygame.mixer.Sound("sounds/eat.mp3")
hit_sound = pygame.mixer.Sound("sounds/hit.mp3")

eat_sound.set_volume(1.0)

delay = 0.1

wn = turtle.Screen()
wn.title("Snake Game")
wn.bgcolor("black")
wn.setup(width=600, height=600)
wn.tracer(0)

head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("green")
head.penup()
head.goto(0, 0)
head.direction = "stop"

body = []

def randompointfood():
    food.goto(random.randint(-290, 290), random.randint(-290, 290))

food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0, 100)

meal = turtle.Turtle()
meal.speed(0)
meal.shape("circle")
meal.color("blue")
meal.penup()
meal.goto(1000, 1000)

pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 250)
pen.write("Score : 0  High Score : 0", align="center",
          font=("candara", 24, "bold"))

powerup = turtle.Turtle()
powerup.speed(0)
powerup.shape("square")
powerup.color("yellow")
powerup.penup()
powerup.goto(1000, 1000)

class Set:
    def __init__():
        pass
    def up():
        if head.direction != "down":
            head.direction = "up"
    def down():
        if head.direction != "up":
            head.direction = "down"
    def left():
        if head.direction != "right":
            head.direction = "left"
    def right():
        if head.direction != "left":
            head.direction = "right"

def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

wn.listen()
wn.onkeypress(Set.up, "w")
wn.onkeypress(Set.down, "s")
wn.onkeypress(Set.left, "a")
wn.onkeypress(Set.right, "d")

score = 0
high_score = 0
powerup_duration = 2 # power up will remain active till powerup_duration
powerup_timer = 2 # power up will be activated till powerup_timer
t = 2 
powerup_active = False

meal_timer = 2

while True:
    wn.update()

    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290: 
        pygame.mixer.Sound.play(hit_sound) 
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "stop"
        for i in body:
            i.goto(1000, 1000)
        body = []
        score = 0
        delay = 0.1
        pen.clear()
        pen.write("Score : {} High Score : {} ".format(
            score, high_score), align="center", font=("candara", 24, "bold"))
        
    if head.distance(food) < 20:
        pygame.mixer.Sound.play(eat_sound)
        randompointfood()
        delay -= 0.001
        
        new_body = turtle.Turtle()
        new_body.speed(0)
        new_body.shape("square")
        new_body.color("green")
        new_body.penup()
        body.append(new_body)

        score += 10
        if score > high_score:
            high_score = score
        pen.clear()
        pen.write("Score : {} High Score : {} ".format(
            score, high_score), align="center", font=("candara", 24, "bold"))


    for i in range(len(body)-1, 0, -1):
        x = body[i-1].xcor()
        y = body[i-1].ycor()
        body[i].goto(x, y)

    if len(body) > 0:
        x = head.xcor()
        y = head.ycor()
        body[0].goto(x, y)
    
    move()

    if(time.time() > meal_timer and random.randint(0, 30) == 1):
        meal.goto(random.randint(-290, 290), random.randint(-290, 290))
        meal_timer = time.time() + t
    
    if(head.distance(meal) < 20):
        pygame.mixer.Sound.play(eat_sound)
        meal.goto(1000, 1000)
        delay -= 0.01

        new_body = turtle.Turtle()
        new_body.speed(0)
        new_body.shape("square")
        new_body.color("green")
        new_body.penup()
        body.append(new_body)

        new_body = turtle.Turtle()
        new_body.speed(0)
        new_body.shape("square")
        new_body.color("green")
        new_body.penup()
        body.append(new_body)

        score += 50
        if score > high_score:
            high_score = score
        pen.clear()
        pen.write("Score : {} High Score : {} ".format(
            score, high_score), align="center", font=("candara", 24, "bold"))
    
    if(time.time() > meal_timer):
        meal.goto(1000, 1000)

    if(time.time() > max(powerup_timer,powerup_duration) and random.randint(0, 10) == 1):
        powerup.goto(random.randint(-290, 290), random.randint(-290, 290))
        powerup_timer = time.time() + t
        
    if head.distance(powerup) < 20:
        pygame.mixer.Sound.play(eat_sound)
        powerup_active = True
        powerup_duration = time.time() + 2*t
        powerup.goto(1000, 1000)
        delay /= 2
    
    if powerup_active and time.time() >= powerup_duration:
        powerup_active = False
        delay *= 2
    
    for i in body:
        if i.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"
            for i in body:
                i.goto(1000, 1000)
            body = []
            score = 0
            delay = 0.1
            pen.clear()
            pen.write("Score : {} High Score : {} ".format(
                score, high_score), align="center", font=("candara", 24, "bold"))
    
    time.sleep(delay)
