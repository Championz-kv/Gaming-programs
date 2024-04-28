import turtle
import time
import random
import threading
from threading import Timer
CURSOR_SIZE = 20
FONT_SIZE = 12
FONT = ('Arial', FONT_SIZE, 'bold')
global ps
ps = "DARK"
global COLORS
COLORS = {1:"blue",2:"red",3:"green",4:"yellow",5:"magenta",6:"purple",7:"cyan",8:"maroon",9:"gold",10:"brown",11:"orange",12:"lightgreen",13:"turquoise",}
global p1c
p1c = COLORS[2]
global p2c
p2c = COLORS[1]
def oneplayer(x,y):
    sin.hideturtle()
    dub.hideturtle()
    sin.clear()
    dub.clear()
    title.clear()
    colored1.hideturtle()
    colored1.clear()
    colored2.hideturtle()
    colored2.clear()
    delay = 0.1
    score = 0
    high_score = 0
    count=1
    stopper=0
    global gamestat
    gamestat =1

    wn = turtle.Screen()
    wn.title("Snake Game - Single Player")
    
    if ps=="DARK":
        wn.bgcolor("black")
    else:
        wn.bgcolor("white")
    width, height = 1240, 600
    canvas = wn.getcanvas()
    left, top = 20, 10
    geom = '{}x{}+{}+{}'.format(width, height, left, top)
    canvas.master.geometry(geom)
    wn.tracer(0)
     
    # head of the snake
    head = turtle.Turtle()
    head.shape("square")
    if ps=="DARK":
        head.color("white")
    else:
        head.color("black")
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
    if ps=="DARK":
        bonus.color("white")
    else:
        bonus.color("black")
    bonus.penup()
    bonus.goto(10000, 10000)

    #scores
    pen = turtle.Turtle()
    pen.speed(0)
    pen.shape("square")
    
    if ps=="DARK":
        pen.color("white")
    else:
        pen.color("black")
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
            delay = 0.1
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
            new_segment.color(COLORS[yy])  # tail colour
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
                    delay = 0.1
                    pen.clear()
                    pen.write("Score : {} High Score : {} ".format(
                        score, high_score), align="center", font=("candara", 24, "bold"))
        time.sleep(delay)
    wn.mainloop()
#################################################################################################
def dubplayer(x,y):
    sin.hideturtle()
    dub.hideturtle()
    sin.clear()
    dub.clear()
    title.clear()
    colored1.hideturtle()
    colored1.clear()
    colored2.hideturtle()
    colored2.clear()
    asegments = []
    bsegments = []
    oscore1 = 0
    oscore2 = 0
    oscore = 'NA'
    delay = 0.1
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
    wn.title("Snake Game - Double Player")
    if ps=="DARK":
        wn.bgcolor("black")
    else:
        wn.bgcolor("white")
    width, height = 1240, 600
    canvas = wn.getcanvas()
    left, top = 20, 10
    geom = '{}x{}+{}+{}'.format(width, height, left, top)
    canvas.master.geometry(geom)

    wn.tracer(0)
     
    head1 = turtle.Turtle()
    head1.shape("square")
    if ps=="DARK":
        head1.color("white")
    else:
        head1.color("black")
    head1.shapesize(1.4)
    head1.penup()
    head1.goto(-100, 0)
    head1.direction = "Stop"

    head2 = turtle.Turtle()
    head2.shape("square")
    if ps=="DARK":
        head2.color("white")
    else:
        head2.color("black")
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
    if ps=="DARK":
        bonus.color("white")
    else:
        bonus.color("black")
    bonus.penup()
    bonus.goto(10000, 10000)
        
    pen = turtle.Turtle()
    pen.speed(0)
    pen.shape("square")
    if ps=="DARK":
        pen.color("white")
    else:
        pen.color("black")
    pen.penup()
    pen.hideturtle()
    pen.goto(0, 255)
    pen.write("Score_1 : 0 Kills : 0 || Overall Winner : NA || High Score : NA || Score_2 : 0 Kills : 0", align="center",
              font=("candara", 20, "bold"))

    bar = turtle.Turtle()
    bar.speed(0)
    bar.shape("square")
    if ps=="DARK":
        bar.color("white")
    else:
        bar.color("black")
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
                delay = 0.1
                pen.clear()
                bar.clear()
                if (cwin == 1):
                    bar.color(COLORS[yy])
                elif (cwin == 2):
                    bar.color(COLORS[xx])
                bar.write("__________________________________________________________________________________________________",align="center",font=("candara",24,"bold"))
                pen.write("Score_1 : {} Kills : {} || Overall Winner : {} || High Score : {}-{} || Score_2 : {} Kills : {}".format(
                    score1,kill1,oscore, highscore,high_score,score2,kill2), align="center", font=("candara", 20, "bold"))
                

            wn.update()
            if head2.xcor() > 610 or head2.xcor() < -610 or head2.ycor() > 240 or head2.ycor() < -290:
                head2.goto(100, 0)
                head2.direction = "Stop"
                count=0
                for bsegment in bsegments:
                    bsegment.goto(1000, 1000)
                bsegments.clear()
                score2 = 0
                delay = 0.1
                pen.clear()
                bar.clear
                if (cwin == 1):
                    bar.color(COLORS[yy])
                elif (cwin == 2):
                    bar.color(COLORS[xx])
                bar.write("__________________________________________________________________________________________________",align="center",font=("candara",24,"bold"))
                pen.write("Score_1 : {} Kills : {} || Overall Winner : {} || High Score : {}-{} || Score_2 : {} Kills : {}".format(
                    score1,kill1,oscore, highscore,high_score,score2,kill2), align="center", font=("candara", 20, "bold"))
                
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
                new1_segment.color(COLORS[yy])  # tail colour
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
                new2_segment.color(COLORS[xx])  # tail colour
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
                highscore = COLORS[yy]
            if  score2 > high_score:
                high_score = score2
                highscore = COLORS[xx]
            if score1 > score2:
                cwin = 1
            elif score2 > score1:
                cwin = 2
            pen.clear()
            bar.clear()
            if (cwin == 1):
                bar.color(COLORS[yy])
            elif (cwin == 2):
                bar.color(COLORS[xx])
            if (oscore1 > oscore2):
                oscore = COLORS[yy]
            elif (oscore2 > oscore1):
                oscore = COLORS[xx]
            bar.write("__________________________________________________________________________________________________",align="center",font=("candara",24,"bold"))
            pen.write("Score_1 : {} Kills : {} || Overall Winner : {} || High Score : {}-{} || Score_2 : {} Kills : {}".format(
                    score1,kill1,oscore, highscore,high_score,score2,kill2), align="center", font=("candara", 20, "bold"))

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
                        delay = 0.1
                        pen.clear()
                        bar.clear()
                        if (cwin == 1):
                            bar.color(COLORS[yy])
                        elif (cwin == 2):
                            bar.color(COLORS[xx])
                        bar.write("__________________________________________________________________________________________________",align="center",font=("candara",24,"bold"))
                        pen.write("Score_1 : {} Kills : {} || Overall Winner : {} || High Score : {}-{} || Score_2 : {} Kills : {}".format(
                            score1,kill1,oscore, highscore,high_score,score2,kill2), align="center", font=("candara", 20, "bold"))
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
                        delay = 0.1
                        pen.clear()
                        bar.clear()
                        if (cwin == 1):
                            bar.color(COLORS[yy])
                        elif (cwin == 2):
                            bar.color(COLORS[xx])
                        bar.write("__________________________________________________________________________________________________",align="center",font=("candara",24,"bold"))
                        pen.write("Score_1 : {} Kills : {} || Overall Winner : {} || High Score : {}-{} || Score_2 : {} Kills : {}".format(
                            score1,kill1,oscore, highscore,high_score,score2,kill2), align="center", font=("candara", 20, "bold"))
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
                        delay = 0.1
                        pen.clear()
                        bar.clear()
                        if (cwin == 1):
                            bar.color(COLORS[yy])
                        elif (cwin == 2):
                            bar.color(COLORS[xx])
                        bar.write("__________________________________________________________________________________________________",align="center",font=("candara",24,"bold"))
                        pen.write("Score_1 : {} Kills : {} || Overall Winner : {} || High Score : {}-{} || Score_2 : {} Kills : {}".format(
                            score1,kill1,oscore, highscore,high_score,score2,kill2), align="center", font=("candara", 20, "bold"))
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
                        delay = 0.1
                        pen.clear()
                        bar.clear()
                        if (cwin == 1):
                            bar.color(COLORS[yy])
                        elif (cwin == 2):
                            bar.color(COLORS[xx])
                        bar.write("__________________________________________________________________________________________________",align="center",font=("candara",24,"bold"))
                        pen.write("Score_1 : {} Kills : {} || Overall Winner : {} || High Score : {}-{} || Score_2 : {} Kills : {}".format(
                            score1,kill1,oscore, highscore,high_score,score2,kill2), align="center", font=("candara", 20, "bold"))

            time.sleep(delay)
    wn.mainloop()
#####################################################################################################################
wn = turtle.Screen()
wn.title("Snake Game Menu")
wn.bgcolor("grey")
width, height = 1240, 600
canvas = wn.getcanvas()
left, top = 20, 10
geom = '{}x{}+{}+{}'.format(width, height, left, top)
canvas.master.geometry(geom)

sin = turtle.Turtle()
sin.hideturtle()
sin.speed(3000)
sin.shape('square')
sin.fillcolor('white')
sin.shapesize(8)
sin.penup()
sin.goto(-300, 0)
sin.write("One Player", align='center', font=FONT)
sin.sety(90 + CURSOR_SIZE + FONT_SIZE)
sin.onclick(oneplayer)
sin.showturtle()

dub = turtle.Turtle()
dub.hideturtle()
dub.speed(3000)
dub.shape('square')
dub.fillcolor('white')
dub.shapesize(8)
dub.penup()
dub.goto(300, 0)
dub.write("Double Player", align='center', font=FONT)
dub.sety(90 + CURSOR_SIZE + FONT_SIZE)
dub.onclick(dubplayer)
dub.showturtle()

title = turtle.Turtle()
title.speed(3000)
title.color("orange")
title.hideturtle()
title.penup()
title.goto(0,50)
title.write("Welcome to SNAKE GAME","Select the number of players", align='center', font=("candara", 25, "bold"))

sped = turtle.Turtle()
sped.speed(3000)
sped.color("black")
sped.hideturtle()
sped.penup()
sped.goto(0,-50)
sped.write("theme : {}".format(ps), align='center', font=("candara", 15, "bold"))



global xx
xx=1
def colorinc1(x,y):
    global xx
    if xx==13:
        xx=0
    xx+=1
    colored1.clear()
    colored1.hideturtle()
    colored1.goto(100,-150)
    colored1.color(COLORS[xx])
    colored1.write("player2 color : {}".format(COLORS[xx]), align='center', font=("candara", 15, "bold"))
    co1 = COLORS[xx]
    colored1.goto(100,-200)
    colored1.showturtle()


global yy
yy=2
def colorinc2(x,y):
    global yy
    if yy==13:
        yy=0
    yy+=1
    colored2.clear()
    colored2.hideturtle()
    colored2.goto(-100,-150)
    colored2.color(COLORS[yy])
    colored2.write("player1 color : {}".format(COLORS[yy]), align='center', font=("candara", 15, "bold"))
    co2 = COLORS[yy]
    colored2.goto(-100,-200)
    colored2.showturtle()
    
colored1 = turtle.Turtle()
colored1.speed(3000)
colored1.color(COLORS[xx])
colored1.shape('square')
colored1.shapesize(3)
colored1.hideturtle()
colored1.penup()
colored1.goto(100,-150)
colored1.write("player2 color : {}".format(COLORS[xx]), align='center', font=("candara", 15, "bold"))
colored1.goto(100,-200)
colored1.onclick(colorinc1)
colored1.showturtle()

colored2 = turtle.Turtle()
colored2.speed(3000)
colored2.color(COLORS[yy])
colored2.shape('square')
colored2.shapesize(3)
colored2.hideturtle()
colored2.penup()
colored2.goto(-100,-150)
colored2.write("player1 color : {}".format(COLORS[yy]), align='center', font=("candara", 15, "bold"))
colored2.goto(-100,-200)
colored2.onclick(colorinc2)
colored2.showturtle()

def ps1():
    global ps
    ps = "LIGHT"
    sped.clear()
    sped.color("white")
    sped.write("theme : {}".format(ps), align='center', font=("candara", 15, "bold"))

def ps0():
    global ps
    ps = "DARK"
    sped.clear()
    sped.color("black")
    sped.write("theme : {}".format(ps), align='center', font=("candara", 15, "bold"))
    
wn.listen()
wn.onkeypress(ps0,"Left")
wn.onkeypress(ps1,"Right")
wn.update()
wn.mainloop()
