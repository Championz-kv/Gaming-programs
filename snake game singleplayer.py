import turtle
import time
import random
import threading
from threading import Timer

delay = 0.05
score = 0
high_score = 0
count=1
stopper=0
global gamestat
gamestat =1

wn = turtle.Screen()
wn.title("Snake Game")
wn.bgcolor("black")
width, height = 1240, 600
canvas = wn.getcanvas()
left, top = 20, 10
geom = '{}x{}+{}+{}'.format(width, height, left, top)
canvas.master.geometry(geom)
wn.tracer(0)
 
# head of the snake
head = turtle.Turtle()
head.shape("square")
head.color("white")
head.shapesize(1.4)
head.penup()
head.goto(0, 0)
head.direction = "Stop"
 
# food in the game
food = turtle.Turtle()
colors = random.choice(['red', 'green', 'blue'])
shapes = random.choice(['circle'])
food.speed(0)
food.shape(shapes)
food.color(colors)
food.penup()
food.goto(0, 100)

bonus= turtle.Turtle()
shapes = random.choice(['circle'])
bonus.shape(shapes)
bonus.color('white')
bonus.penup()
bonus.goto(10000, 10000)

#scores
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 250)
pen.write("Score : 0  High Score : 0", align="center",
          font=("candara", 24, "bold"))
 
# assigning key directions
def group():
    if head.direction != "down":
        head.direction = "up"
def godown():
    if head.direction != "up":
        head.direction = "down"
def goleft():
    if head.direction != "right":
        head.direction = "left"
def goright():
    if head.direction != "left":
        head.direction = "right"
def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y+25)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y-25)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x-25)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x+25)
def exitwin():
    wn.bye()
def on():
    global gamestat
    if gamestat == 0:
        gamestat = 1
    else:
        gamestat = 0
        
wn.listen()
wn.onkeypress(group, "Up")
wn.onkeypress(godown, "Down")
wn.onkeypress(goleft, "Left")
wn.onkeypress(goright, "Right")
wn.onkeypress(group, "w")
wn.onkeypress(godown, "s")
wn.onkeypress(goleft, "a")
wn.onkeypress(goright, "d")
wn.onkeypress(on,"space")
wn.onkeypress(exitwin,"Escape")
segments = []

 
# Main Gameplay
while True:
    wn.update()
    if head.xcor() > 610 or head.xcor() < -610 or head.ycor() > 290 or head.ycor() < -290:
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "Stop"
        count=0
        colors = random.choice(['red', 'blue', 'green'])
        shapes = random.choice(['square', 'circle'])
        for segment in segments:
            segment.goto(1000, 1000)
        segments.clear()
        score = 0
        delay = 0.05
        pen.clear()
        pen.write("Score : {} High Score : {} ".format(
            score, high_score), align="center", font=("candara", 24, "bold"))
   
    if head.distance(food) < 20:
        x = random.randint(-580, 580)
        y = random.randint(-270, 270)
        colors = random.choice(['red', 'green', 'blue','yellow','cyan','magenta'])
        food.color(colors)
        food.goto(x, y)
        bonus.goto(10000,10000)
        stopper =0
        count+=1
        score+=10
        # Adding segment
        new_segment = turtle.Turtle()        
        new_segment.speed(1)
        new_segment.shape("square")
        new_segment.color("orange")  # tail colour
        new_segment.shapesize(1.2)
        new_segment.penup()
        segments.append(new_segment)
        delay -= 0.001
    if(count%7 == 0 and stopper==0):
        x = random.randint(-580, 580)
        y = random.randint(-270, 270)
        bonus.goto(x,y)
        count+=1
        stopper+=1
    if head.distance(bonus) < 20:
        bonus.goto(10000,10000)
        score+=25
        stopper =0

    if score > high_score:
        high_score = score
            
    pen.clear()
    pen.write("Score : {} High Score : {} ".format(
        score, high_score), align="center", font=("candara", 24, "bold"))
    # Checking for head collisions with body segments
    if(gamestat):
        for index in range(len(segments)-1, 0, -1):
            x = segments[index-1].xcor()
            y = segments[index-1].ycor()
            segments[index].goto(x, y)
        if len(segments) > 0:
            x = head.xcor()
            y = head.ycor()
            segments[0].goto(x, y)
        move()
        for segment in segments:
            if segment.distance(head) < 20:
                time.sleep(1)
                head.goto(0, 0)
                head.direction = "stop"
                count=0
                for segment in segments:
                    segment.goto(1000, 1000)
                segments.clear()
     
                score = 0
                delay = 0.05
                pen.clear()
                pen.write("Score : {} High Score : {} ".format(
                    score, high_score), align="center", font=("candara", 24, "bold"))
    time.sleep(delay)
 
wn.mainloop()
