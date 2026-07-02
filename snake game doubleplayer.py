import turtle
import time
import random
import threading
from threading import Timer
delayconst = 0.05
asegments = []
bsegments = []
oscore1 = 0
oscore2 = 0
oscore = 'NA'
delay = delayconst
score1 = 0
score2 = 0
high_score = 0
highscore = 'NA'
count=1
stopper=0
cwin=0
d1 = "Stop"
d2 = "Stop"
x1 = 0
x2 = 0
y1 = 0
y2 = 0
kill1 = 0
kill2 = 0
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
 
head1 = turtle.Turtle()
head1.shape("square")
head1.color("white")
head1.shapesize(1.4)
head1.penup()
head1.goto(-100, 0)
head1.direction = "Stop"

head2 = turtle.Turtle()
head2.shape("square")
head2.color("white")
head2.shapesize(1.4)
head2.penup()
head2.goto(100, 0)
head2.direction = "Stop"

food = turtle.Turtle()
colors = random.choice(['orange', 'green', 'yellow'])
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
    
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 255)
pen.write("Score_1 : 0 Kills : 0 || Overall Winner : NA || High Score : NA || Score_2 : 0 Kills : 0", align="center",
          font=("candara", 24, "bold"))

bar = turtle.Turtle()
bar.speed(0)
bar.shape("square")
bar.color("white")
bar.penup()
bar.hideturtle()
bar.goto(0, 250)
bar.write("__________________________________________________________________________________________________",align="center",font=("candara",24,"bold"))

def group1():
    if head1.direction != "down":
        head1.direction = "up"
def godown1():
    if head1.direction != "up":
        head1.direction = "down"
def goleft1():
    if head1.direction != "right":
        head1.direction = "left"
def goright1():
    if head1.direction != "left":
        head1.direction = "right"
def move1():
    if head1.direction == "up":
        y = head1.ycor()
        head1.sety(y+25)
    if head1.direction == "down":
        y = head1.ycor()
        head1.sety(y-25)
    if head1.direction == "left":
        x = head1.xcor()
        head1.setx(x-25)
    if head1.direction == "right":
        x = head1.xcor()
        head1.setx(x+25)

def group2():
    if head2.direction != "down":
        head2.direction = "up"
def godown2():
    if head2.direction != "up":
        head2.direction = "down"
def goleft2():
    if head2.direction != "right":
        head2.direction = "left"
def goright2():
    if head2.direction != "left":
        head2.direction = "right"
def move2():
    if head2.direction == "up":
        y = head2.ycor()
        head2.sety(y+25)
    if head2.direction == "down":
        y = head2.ycor()
        head2.sety(y-25)
    if head2.direction == "left":
        x = head2.xcor()
        head2.setx(x-25)
    if head2.direction == "right":
        x = head2.xcor()
        head2.setx(x+25)
def exitwin():
    wn.bye()
def on():
    global gamestat
    if gamestat == 0:
        gamestat = 1
    else:
        gamestat = 0

wn.listen()
wn.onkeypress(group2, "Up")
wn.onkeypress(godown2, "Down")
wn.onkeypress(goleft2, "Left")
wn.onkeypress(goright2, "Right")
wn.onkeypress(group1, "w")
wn.onkeypress(godown1, "s")
wn.onkeypress(goleft1, "a")
wn.onkeypress(goright1, "d")
wn.onkeypress(on,"space")
wn.onkeypress(exitwin,"Escape")


while True:
        wn.update()
        if head1.xcor() > 610 or head1.xcor() < -610 or head1.ycor() > 240 or head1.ycor() < -290:
            head1.goto(-100, 0)
            head1.direction = "Stop"
            count=0
            for asegment in asegments:
                asegment.goto(1000, 1000)
            asegments.clear()
            score1 = 0
            delay = delayconst
            pen.clear()
            bar.clear()
            if (cwin == 1):
                bar.color("red")
            elif (cwin == 2):
                bar.color("blue")
            bar.write("__________________________________________________________________________________________________",align="center",font=("candara",24,"bold"))
            pen.write("Score_1 : {} Kills : {} || Overall Winner : {} || High Score : {}-{} || Score_2 : {} Kills : {}".format(
                score1,kill1,oscore, highscore,high_score,score2,kill2), align="center", font=("candara", 24, "bold"))
            

        wn.update()
        if head2.xcor() > 610 or head2.xcor() < -610 or head2.ycor() > 240 or head2.ycor() < -290:
            head2.goto(100, 0)
            head2.direction = "Stop"
            count=0
            for bsegment in bsegments:
                bsegment.goto(1000, 1000)
            bsegments.clear()
            score2 = 0
            delay = delayconst
            pen.clear()
            bar.clear
            if (cwin == 1):
                bar.color("red")
            elif (cwin == 2):
                bar.color("blue")
            bar.write("__________________________________________________________________________________________________",align="center",font=("candara",24,"bold"))
            pen.write("Score_1 : {} Kills : {} || Overall Winner : {} || High Score : {}-{} || Score_2 : {} Kills : {}".format(
                score1,kill1,oscore, highscore,high_score,score2,kill2), align="center", font=("candara", 24, "bold"))
            
        if head1.distance(food) < 20:
            x = random.randint(-580, 580)
            y = random.randint(-270, 220)
            colors = random.choice(['green', 'orange','yellow','cyan','magenta','purple'])
            food.color(colors)
            food.goto(x, y)
            bonus.goto(10000,10000)
            stopper =0
            count+=1
            score1+=10
            oscore1 += 10
            
            new1_segment = turtle.Turtle()
            new1_segment.speed(1)
            new1_segment.shape("square")
            new1_segment.color("red")  # tail colour
            new1_segment.shapesize(1.2)
            new1_segment.penup()
            asegments.append(new1_segment)
            delay -= 0.001
            
        if head2.distance(food) < 20:
            x = random.randint(-580, 580)
            y = random.randint(-270, 220)
            colors = random.choice(['green', 'orange','yellow','cyan','magenta','purple'])
            food.color(colors)
            food.goto(x, y)
            bonus.goto(10000,10000)
            stopper =0
            count+=1
            score2+=10
            oscore2+=10
            
            new2_segment = turtle.Turtle()
            new2_segment.speed(1)
            new2_segment.shape("square")
            new2_segment.color("blue")  # tail colour
            new2_segment.shapesize(1.2)
            new2_segment.penup()
            bsegments.append(new2_segment)
            delay -= 0.001
            
        if(count%7 == 0 and stopper==0):
            x = random.randint(-580, 580)
            y = random.randint(-270, 220)
            bonus.goto(x,y)
            count+=1
            stopper+=1
        if head1.distance(bonus) < 20 :
            bonus.goto(10000,10000)
            score1+=25
            oscore1 +=25
            stopper =0
        if head2.distance(bonus) < 20 :
            bonus.goto(10000,10000)
            score2+=25
            oscore2 += 25
            stopper =0

        if score1 > high_score:
            high_score = score1
            highscore = 'RED'
        if  score2 > high_score:
            high_score = score2
            highscore = 'BLUE'
        if score1 > score2:
            cwin = 1
        elif score2 > score1:
            cwin = 2
        pen.clear()
        bar.clear()
        if (cwin == 1):
            bar.color("red")
        elif (cwin == 2):
            bar.color("blue")
        if (oscore1 > oscore2):
            oscore = "RED"
        elif (oscore2 > oscore1):
            oscore = "BLUE"
        bar.write("__________________________________________________________________________________________________",align="center",font=("candara",24,"bold"))
        pen.write("Score_1 : {} Kills : {} || Overall Winner : {} || High Score : {}-{} || Score_2 : {} Kills : {}".format(
                score1,kill1,oscore, highscore,high_score,score2,kill2), align="center", font=("candara", 24, "bold"))

        # Checking for head collisions with body segments
        if(gamestat):
            for index in range(len(asegments)-1, 0, -1):
                x = asegments[index-1].xcor()
                y = asegments[index-1].ycor()
                asegments[index].goto(x, y)
            if len(asegments) > 0:
                x = head1.xcor()
                y = head1.ycor()
                asegments[0].goto(x, y)
            move1()
            for asegment in asegments:
                if asegment.distance(head1) < 20:
                    head1.goto(-100, 0)
                    head1.direction = "stop"
                    count=0
                    for asegment in asegments:
                        asegment.goto(1000, 1000)
                    asegments.clear()         
                    score1 = 0
                    delay = delayconst
                    pen.clear()
                    bar.clear()
                    if (cwin == 1):
                        bar.color("red")
                    elif (cwin == 2):
                        bar.color("blue")
                    bar.write("__________________________________________________________________________________________________",align="center",font=("candara",24,"bold"))
                    pen.write("Score_1 : {} Kills : {} || Overall Winner : {} || High Score : {}-{} || Score_2 : {} Kills : {}".format(
                        score1,kill1,oscore, highscore,high_score,score2,kill2), align="center", font=("candara", 24, "bold"))
                if asegment.distance(head2) < 20:
                    head2.goto(100, 0)
                    head2.direction = "stop"
                    count=0
                    for bsegment in bsegments:
                        bsegment.goto(1000, 1000)
                    bsegments.clear()
                    score2 = 0
                    score1 +=15
                    kill1+=1
                    delay = delayconst
                    pen.clear()
                    bar.clear()
                    if (cwin == 1):
                        bar.color("red")
                    elif (cwin == 2):
                        bar.color("blue")
                    bar.write("__________________________________________________________________________________________________",align="center",font=("candara",24,"bold"))
                    pen.write("Score_1 : {} Kills : {} || Overall Winner : {} || High Score : {}-{} || Score_2 : {} Kills : {}".format(
                        score1,kill1,oscore, highscore,high_score,score2,kill2), align="center", font=("candara", 24, "bold"))
        if(gamestat):       
            for index in range(len(bsegments)-1, 0, -1):
                x = bsegments[index-1].xcor()
                y = bsegments[index-1].ycor()
                bsegments[index].goto(x, y)
            if len(bsegments) > 0:
                x = head2.xcor()
                y = head2.ycor()
                bsegments[0].goto(x, y)
            move2()
            for bsegment in bsegments:
                if bsegment.distance(head2) < 20:            
                    head2.goto(100, 0)
                    head2.direction = "stop"
                    count=0
                    for bsegment in bsegments:
                        bsegment.goto(1000, 1000)
                    bsegments.clear()
                    score2 = 0
                    delay = delayconst
                    pen.clear()
                    bar.clear()
                    if (cwin == 1):
                        bar.color("red")
                    elif (cwin == 2):
                        bar.color("blue")
                    bar.write("__________________________________________________________________________________________________",align="center",font=("candara",24,"bold"))
                    pen.write("Score_1 : {} Kills : {} || Overall Winner : {} || High Score : {}-{} || Score_2 : {} Kills : {}".format(
                        score1,kill1,oscore, highscore,high_score,score2,kill2), align="center", font=("candara", 24, "bold"))
                if bsegment.distance(head1) < 20:
                    head1.goto(-100, 0)
                    head1.direction = "stop"
                    count=0
                    for asegment in asegments:
                        asegment.goto(1000, 1000)
                    asegments.clear()
                    score1 = 0
                    score2 += 15
                    kill2+=1
                    delay = delayconst
                    pen.clear()
                    bar.clear()
                    if (cwin == 1):
                        bar.color("red")
                    elif (cwin == 2):
                        bar.color("blue")
                    bar.write("__________________________________________________________________________________________________",align="center",font=("candara",24,"bold"))
                    pen.write("Score_1 : {} Kills : {} || Overall Winner : {} || High Score : {}-{} || Score_2 : {} Kills : {}".format(
                        score1,kill1,oscore, highscore,high_score,score2,kill2), align="center", font=("candara", 24, "bold"))

        time.sleep(delay)
wn.mainloop()
