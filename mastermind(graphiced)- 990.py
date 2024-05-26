#IMPORTS
import turtle
import time
import random
lop=0
#CODE VARIABLES
global A
global B
global C
global D
global E
#CODE GENERATION
A = random.randint(1,8)
B = random.randint(1,8)
while (lop ==0):
        if (B==A):
                  B = random.randint(1,8)
        else:
                  break
C = random.randint(1,8)
while (lop ==0):
        if (C==A or C==B):
                  C = random.randint(1,8)
        else:
                  break
D = random.randint(1,8)
while (lop ==0):
        if (D==A or D==B ):
                  D = random.randint(1,8)
        elif ( D==C):
                  D = random.randint(1,8)
        else:
                  break
E = random.randint(1,8)
while (lop ==0):
        if (E==A or E==B ):
                  E = random.randint(1,8)
        elif ( E==C or E==D):
                  E = random.randint(1,8)
        else:
                  break
#SCREEN SETUP
wn = turtle.Screen()
wn.title("MASTERMIND")
wn.bgcolor("gray10")
width, height = 1240, 600
canvas = wn.getcanvas()
left, top = 20, 10
geom = '{}x{}+{}+{}'.format(width, height, left, top)
canvas.master.geometry(geom)
load = ["Loading","Loading .","Loading . .","Loading . . .","Loading . . . .","Loading . . . . ."]
loading = turtle.Turtle()
loading.speed(1000)
loading.hideturtle()
loading.penup()
loading.goto(300,230)
loading.write(load[0],align="left",font=("candara",15,"bold"))
head = turtle.Turtle()
head.speed(500)
head.hideturtle()
head.color("SeaGreen1")
head.penup()
head.goto(-540,-230)
head.pendown()
head.width(5)
head.left(90)
head.forward(360)
head.circle(-50,  extent = 90)
head.forward(990)
head.circle(-50,  extent = 90)
head.forward(360)
head.circle(-50,  extent = 90)
head.forward (990)
head.circle(-50,  extent = 90)
head.width(3)
loading.clear()
loading.write(load[1],align="left",font=("candara",15,"bold"))
head.penup()

#PLAYING BOARD GENERATION
global pos
pos = -490
x = -550##
loader = 1
for i in range (15) :
           x = x+70
           if loader < 5 :
                   loader = loader + 1
                   loading.clear()
                   loading.write(load[loader],align="left",font=("candara",15,"bold"))
           else :
                   loader = 0
                   loading.clear()
                   loading.write(load[0],align="left",font=("candara",15,"bold"))
           if i == 13 :
                      head.goto(x,-7)
                      head.pendown()
                      head.penup()
                      head.goto(x,-57)
                      head.pendown()
                      head.penup()
                      head.goto(x,-107)
                      head.pendown()
                      head.penup()
                      head.goto(x,-157)
                      head.pendown()
                      head.penup()
                      head.goto(x,-207)
                      head.pendown()
                      head.penup()
           else :
                      head.goto(x,-5)
                      head.pendown()
                      head.circle(10)
                      head.penup()
                      head.goto(x,-55)
                      head.pendown()
                      head.circle(10)
                      head.penup()
                      head.goto(x,-105)
                      head.pendown()
                      head.circle(10)
                      head.penup()
                      head.goto(x,-155)
                      head.pendown()
                      head.circle(10)
                      head.penup()
                      head.goto(x,-205)
                      head.pendown()
                      head.circle(10)
                      head.penup()
global sop
sop = -565
loader = 4
x = -555
head.width(2)
for i in range (15) :
           x = x+70
           if loader < 5 :
                   loader = loader + 1
                   loading.clear()
                   loading.write(load[loader],align="left",font=("candara",15,"bold"))
           else :
                   loader = 0
                   loading.clear()
                   loading.write(load[0],align="left",font=("candara",15,"bold"))
           if i == 13 :
                      continue
           else :
                      head.goto(x,120)
                      head.pendown()
                      head.circle(5)
                      head.penup()
                      head.goto(x,105)
                      head.pendown()
                      head.circle(5)
                      head.penup()
                      head.goto(x,90)
                      head.pendown()
                      head.circle(5)
                      head.penup()
                      head.goto(x,75)
                      head.pendown()
                      head.circle(5)
                      head.penup()
                      head.goto(x,60)
                      head.pendown()
                      head.circle(5)
                      head.penup()
#SHORTCUTS TO PUT PIECES INTO PLACES USING NUMBERS ( A NUMBER FOR EACH COLOUR )
global inpos1
inpos1 = 0
global inpos2
inpos2 = 0
global inpos3
inpos3 = 0
global inpos4
inpos4 = 0
global inpos5
inpos5 = 0
loading.clear()
loading.write(load[2],align="left",font=("candara",15,"bold"))
def got1(x=0,y=0):
           global inpos1
           global inpos2
           global inpos3
           global inpos4
           global inpos5
           if col1.xcor() == pos and col1.ycor() == -5 :
                      col1.goto(-400,250)
                      inpos1 = 0
           elif col1.xcor() == pos and col1.ycor() == -55 :
                      col1.goto(-400,250)
                      inpos2 = 0
           elif col1.xcor() == pos and col1.ycor() == -105 :
                      col1.goto(-400,250)
                      inpos3 = 0
           elif col1.xcor() == pos and col1.ycor() == -155 :
                      col1.goto(-400,250)
                      inpos4 = 0
           elif col1.xcor() == pos and col1.ycor() == -205 :
                      col1.goto(-400,250)
                      inpos5 = 0
           elif inpos1 == 0  :
                      col1.goto(pos,-5)
                      inpos1 = 1
           elif inpos2 == 0 :
                      col1.goto(pos,-55)
                      inpos2 = 1
           elif inpos3 == 0 :
                      col1.goto(pos,-105)
                      inpos3 = 1
           elif inpos4 == 0 :
                      col1.goto(pos,-155)
                      inpos4 = 1
           elif inpos5 == 0 :
                      col1.goto(pos,-205)
                      inpos5 = 1
def got2(x=0,y=0):
           global inpos1
           global inpos2
           global inpos3
           global inpos4
           global inpos5
           if col2.xcor() == pos and col2.ycor() == -5 :
                      col2.goto(-350,250)
                      inpos1 = 0
           elif col2.xcor() == pos and col2.ycor() == -55 :
                      col2.goto(-350,250)
                      inpos2 = 0
           elif col2.xcor() == pos and col2.ycor() == -105 :
                      col2.goto(-350,250)
                      inpos3 = 0
           elif col2.xcor() == pos and col2.ycor() == -155 :
                      col2.goto(-350,250)
                      inpos4 = 0
           elif col2.xcor() == pos and col2.ycor() == -205 :
                      col2.goto(-350,250)
                      inpos5 = 0
           elif inpos1 == 0 :
                      col2.goto(pos,-5)
                      inpos1 = 1
           elif inpos2 == 0 :
                      col2.goto(pos,-55)
                      inpos2 = 1
           elif inpos3 == 0 :
                      col2.goto(pos,-105)
                      inpos3 = 1
           elif inpos4 == 0 :
                      col2.goto(pos,-155)
                      inpos4 = 1
           elif inpos5 == 0 :
                      col2.goto(pos,-205)
                      inpos5 = 1
def got3(x=0,y=0):
           global inpos1
           global inpos2
           global inpos3
           global inpos4
           global inpos5
           if col3.xcor() == pos and col3.ycor() == -5 :
                      col3.goto(-300,250)
                      inpos1 = 0
           elif col3.xcor() == pos and col3.ycor() == -55 :
                      col3.goto(-300,250)
                      inpos2 = 0
           elif col3.xcor() == pos and col3.ycor() == -105 :
                      col3.goto(-300,250)
                      inpos3 = 0
           elif col3.xcor() == pos and col3.ycor() == -155 :
                      col3.goto(-300,250)
                      inpos4 = 0
           elif col3.xcor() == pos and col3.ycor() == -205 :
                      col3.goto(-300,250)
                      inpos5 = 0
           elif inpos1 == 0 :
                      col3.goto(pos,-5)
                      inpos1 = 1
           elif inpos2 == 0 :
                      col3.goto(pos,-55)
                      inpos2 = 1
           elif inpos3 == 0 :
                      col3.goto(pos,-105)
                      inpos3 = 1
           elif inpos4 == 0 :
                      col3.goto(pos,-155)
                      inpos4 = 1
           elif inpos5 == 0 :
                      col3.goto(pos,-205)
                      inpos5 = 1
def got4(x=0,y=0):
           global inpos1
           global inpos2
           global inpos3
           global inpos4
           global inpos5
           if col4.xcor() == pos and col4.ycor() == -5 :
                      col4.goto(-250,250)
                      inpos1 = 0
           elif col4.xcor() == pos and col4.ycor() == -55 :
                      col4.goto(-250,250)
                      inpos2 = 0
           elif col4.xcor() == pos and col4.ycor() == -105 :
                      col4.goto(-250,250)
                      inpos3 = 0
           elif col4.xcor() == pos and col4.ycor() == -155 :
                      col4.goto(-250,250)
                      inpos4 = 0
           elif col4.xcor() == pos and col4.ycor() == -205 :
                      col4.goto(-250,250)
                      inpos5 = 0
           elif inpos1 == 0 :
                      col4.goto(pos,-5)
                      inpos1 = 1
           elif inpos2 == 0 :
                      col4.goto(pos,-55)
                      inpos2 = 1
           elif inpos3 == 0 :
                      col4.goto(pos,-105)
                      inpos3 = 1
           elif inpos4 == 0 :
                      col4.goto(pos,-155)
                      inpos4 = 1
           elif inpos5 == 0 :
                      col4.goto(pos,-205)
                      inpos5 = 1
def got5(x=0,y=0):
           global inpos1
           global inpos2
           global inpos3
           global inpos4
           global inpos5
           if col5.xcor() == pos and col5.ycor() == -5 :
                      col5.goto(-200,250)
                      inpos1 = 0
           elif col5.xcor() == pos and col5.ycor() == -55 :
                      col5.goto(-200,250)
                      inpos2 = 0
           elif col5.xcor() == pos and col5.ycor() == -105 :
                      col5.goto(-200,250)
                      inpos3 = 0
           elif col5.xcor() == pos and col5.ycor() == -155 :
                      col5.goto(-200,250)
                      inpos4 = 0
           elif col5.xcor() == pos and col5.ycor() == -205 :
                      col5.goto(-200,250)
                      inpos5 = 0
           elif inpos1 == 0 :
                      col5.goto(pos,-5)
                      inpos1 = 1
           elif inpos2 == 0 :
                      col5.goto(pos,-55)
                      inpos2 = 1
           elif inpos3 == 0 :
                      col5.goto(pos,-105)
                      inpos3 = 1
           elif inpos4 == 0 :
                      col5.goto(pos,-155)
                      inpos4 = 1
           elif inpos5 == 0 :
                      col5.goto(pos,-205)
                      inpos5 = 1
def got6(x=0,y=0):
           global inpos1
           global inpos2
           global inpos3
           global inpos4
           global inpos5
           if col6.xcor() == pos and col6.ycor() == -5 :
                      col6.goto(-150,250)
                      inpos1 = 0
           elif col6.xcor() == pos and col6.ycor() == -55 :
                      col6.goto(-150,250)
                      inpos2 = 0
           elif col6.xcor() == pos and col6.ycor() == -105 :
                      col6.goto(-150,250)
                      inpos3 = 0
           elif col6.xcor() == pos and col6.ycor() == -155 :
                      col6.goto(-150,250)
                      inpos4 = 0
           elif col6.xcor() == pos and col6.ycor() == -205 :
                      col6.goto(-150,250)
                      inpos5 = 0
           elif inpos1 == 0 :
                      col6.goto(pos,-5)
                      inpos1 = 1
           elif inpos2 == 0 :
                      col6.goto(pos,-55)
                      inpos2 = 1
           elif inpos3 == 0 :
                      col6.goto(pos,-105)
                      inpos3 = 1
           elif inpos4 == 0 :
                      col6.goto(pos,-155)
                      inpos4 = 1
           elif inpos5 == 0 :
                      col6.goto(pos,-205)
                      inpos5 = 1
def got7(x=0,y=0):
           global inpos1
           global inpos2
           global inpos3
           global inpos4
           global inpos5
           if col7.xcor() == pos and col7.ycor() == -5 :
                      col7.goto(-100,250)
                      inpos1 = 0
           elif col7.xcor() == pos and col7.ycor() == -55 :
                      col7.goto(-100,250)
                      inpos2 = 0
           elif col7.xcor() == pos and col7.ycor() == -105 :
                      col7.goto(-100,250)
                      inpos3 = 0
           elif col7.xcor() == pos and col7.ycor() == -155 :
                      col7.goto(-100,250)
                      inpos4 = 0
           elif col7.xcor() == pos and col7.ycor() == -205 :
                      col7.goto(-100,250)
                      inpos5 = 0
           elif inpos1 == 0 :
                      col7.goto(pos,-5)
                      inpos1 = 1
           elif inpos2 == 0 :
                      col7.goto(pos,-55)
                      inpos2 = 1
           elif inpos3 == 0 :
                      col7.goto(pos,-105)
                      inpos3 = 1
           elif inpos4 == 0 :
                      col7.goto(pos,-155)
                      inpos4 = 1
           elif inpos5 == 0 :
                      col7.goto(pos,-205)
                      inpos5 = 1
def got8(x=0,y=0):
           global inpos1
           global inpos2
           global inpos3
           global inpos4
           global inpos5
           if col8.xcor() == pos and col8.ycor() == -5 :
                      col8.goto(-50,250)
                      inpos1 = 0
           elif col8.xcor() == pos and col8.ycor() == -55 :
                      col8.goto(-50,250)
                      inpos2 = 0
           elif col8.xcor() == pos and col8.ycor() == -105 :
                      col8.goto(-50,250)
                      inpos3 = 0
           elif col8.xcor() == pos and col8.ycor() == -155 :
                      col8.goto(-50,250)
                      inpos4 = 0
           elif col8.xcor() == pos and col8.ycor() == -205 :
                      col8.goto(-50,250)
                      inpos5 = 0
           elif inpos1 == 0 :
                      col8.goto(pos,-5)
                      inpos1 = 1
           elif inpos2 == 0 :
                      col8.goto(pos,-55)
                      inpos2 = 1
           elif inpos3 == 0 :
                      col8.goto(pos,-105)
                      inpos3 = 1
           elif inpos4 == 0 :
                      col8.goto(pos,-155)
                      inpos4 = 1
           elif inpos5 == 0 :
                      col8.goto(pos,-205)
                      inpos5 = 1
# GAME REPLAY ( CONTAINS A NEW CODE GENERATION SYSTEM IN IT FOR AFTER RESET)
global confirmwork
confirmwork =1
def replaying(x,y) :
        hidepeg.goto(1000,1000)
        jynx.clear()
        lavapede.clear()
        replay.clear()
        replay.goto(1000,1000)
        global pos
        pos = -490
        global sop
        sop = -565
        col1.goto(-400,250)
        col2.goto(-350,250)
        col3.goto(-300,250)
        col4.goto(-250,250)
        col5.goto(-200,250)
        col6.goto(-150,250)
        col7.goto(-100,250)
        col8.goto(-50,250)
        lop=0
        global A
        global B
        global C
        global D
        global E
        A = random.randint(1,8)
        B = random.randint(1,8)
        while (lop ==0):
                if (B==A):
                          B = random.randint(1,8)
                else:
                          break
        C = random.randint(1,8)
        while (lop ==0):
                if (C==A or C==B):
                          C = random.randint(1,8)
                else:
                          break
        D = random.randint(1,8)
        while (lop ==0):
                if (D==A or D==B ):
                          D = random.randint(1,8)
                elif ( D==C):
                          D = random.randint(1,8)
                else:
                          break
        E = random.randint(1,8)
        while (lop ==0):
                if (E==A or E==B ):
                          E = random.randint(1,8)
                elif ( E==C or E==D):
                          E = random.randint(1,8)
                else:
                          break
# SURRENDER ( SHOWS THE HIDDEN CODE )
def surrendering(x=0,y=0) :
         hidepeg.goto(-220,400)
         hidepeg.showturtle()
         jynx.goto(-300,220)
         jynx.color('red')
         jynx.write("YOU LOSE !",align="left",font=("candara",28,"bold"))
         codex = [A,B,C,D,E]
         ylist = [-5,-55,-105,-155,-205]
         yon = 0
         replay.goto(320,260)
         replay.write("RE-PLAY",align="left",font=("candara",15,"bold"))
         replay.showturtle()
         replay.goto(355,230)
         for con in codex :
                 if con == 1 :
                         col1.goto(490 ,ylist[yon])
                 elif con == 2 :
                         col2.goto(490 ,ylist[yon])
                 elif con == 3 :
                         col3.goto(490 ,ylist[yon])
                 elif con == 4 :
                         col4.goto(490 ,ylist[yon])
                 elif con == 5 :
                         col5.goto(490 ,ylist[yon])
                 elif con == 6 :
                         col6.goto(490 ,ylist[yon])
                 elif con == 7 :
                         col7.goto(490 ,ylist[yon])
                 elif con == 8 :
                         col8.goto(490 ,ylist[yon])
                 yon = yon + 1
#MAIN CODE ENGINE
def confirmation(x=0,y=0) :
           global confirmwork
           global inpos1
           global inpos2
           global inpos3
           global inpos4
           global inpos5
           if inpos1 == 1 and inpos2 == 1 and inpos3 == 1 and inpos4 == 1 and inpos5 == 1 and confirmwork < 13:
                      global pos
                      pos = pos + 70
                      global sop
                      sop = sop + 70
                      confirmwork = confirmwork + 1
                      inpos1 = 0
                      inpos2 = 0
                      inpos3 = 0
                      inpos4 = 0
                      inpos5 = 0
                      yylist = [-5,-55,-105,-155,-205]
                      colist = [col1,col2,col3,col4,col5,col6,col7,col8]
                      alu = 0
                      #PRINTS COLOURS ON PREVIOUS ROW CIRCLES FOR SAVING THE COLOUR CODE YOU USED
                      for yy in yylist :
                                 for cen in colist :
                                            if cen.xcor() == pos-70 and cen.ycor() == yy :
                                                       alu = alu+ 1
                                                       jynx.goto(pos-70,yy-15)
                                                       jynx.pendown()
                                                       if cen == col1 :
                                                                  jynx.color('blue')
                                                                  if alu == 1 :
                                                                             a = 1
                                                                  elif alu == 2 :
                                                                             b = 1
                                                                  elif alu == 3 :
                                                                             c = 1
                                                                  elif alu == 4 :
                                                                             d = 1
                                                                  elif alu == 5 :
                                                                             e = 1
                                                       elif cen == col2 :
                                                                  jynx.color('red')
                                                                  if alu ==1 :
                                                                             a = 2
                                                                  elif alu == 2 :
                                                                             b = 2
                                                                  elif alu == 3 :
                                                                             c = 2
                                                                  elif alu == 4 :
                                                                             d = 2
                                                                  elif alu == 5 :
                                                                             e = 2
                                                       elif cen == col3 :
                                                                  jynx.color('magenta')
                                                                  if alu == 1 :
                                                                             a = 3
                                                                  elif alu == 2 :
                                                                             b = 3
                                                                  elif alu == 3 :
                                                                             c = 3
                                                                  elif alu == 4 :
                                                                             d = 3
                                                                  elif alu == 5 :
                                                                             e = 3
                                                       elif cen == col4 :
                                                                  jynx.color('LightSkyBlue')
                                                                  if alu == 1 :
                                                                             a = 4
                                                                  elif alu == 2 :
                                                                             b = 4
                                                                  elif alu == 3 :
                                                                             c = 4
                                                                  elif alu == 4 :
                                                                             d = 4
                                                                  elif alu == 5 :
                                                                             e = 4
                                                       elif cen == col5 :
                                                                  jynx.color('yellow')
                                                                  if alu == 1 :
                                                                             a = 5
                                                                  elif alu == 2 :
                                                                             b = 5
                                                                  elif alu == 3 :
                                                                             c = 5
                                                                  elif alu == 4 :
                                                                             d = 5
                                                                  elif alu == 5 :
                                                                             e = 5
                                                       elif cen == col6 :
                                                                  jynx.color('orange')
                                                                  if alu == 1 :
                                                                             a = 6
                                                                  elif alu == 2 :
                                                                             b = 6
                                                                  elif alu == 3 :
                                                                             c = 6
                                                                  elif alu == 4 :
                                                                             d = 6
                                                                  elif alu == 5 :
                                                                             e = 6
                                                       elif cen == col7 :
                                                                  jynx.color('white')
                                                                  if alu == 1 :
                                                                             a = 7
                                                                  elif alu == 2 :
                                                                             b =7
                                                                  elif alu == 3 :
                                                                             c = 7
                                                                  elif alu == 4 :
                                                                             d =7
                                                                  elif alu == 5 :
                                                                             e = 7
                                                       elif cen == col8 :
                                                                  jynx.color('dark violet')
                                                                  if alu == 1 :
                                                                             a = 8
                                                                  elif alu == 2 :
                                                                             b = 8
                                                                  elif alu == 3 :
                                                                             c = 8
                                                                  elif alu == 4 :
                                                                             d = 8
                                                                  elif alu == 5 :
                                                                             e = 8
                                                       jynx.begin_fill()
                                                       jynx.circle(15)
                                                       jynx.end_fill()
                                                       jynx.penup()
                                                       jynx.goto(1000,1000)
                      col1.goto(-400,250)
                      col2.goto(-350,250)
                      col3.goto(-300,250)
                      col4.goto(-250,250)
                      col5.goto(-200,250)
                      col6.goto(-150,250)
                      col7.goto(-100,250)
                      col8.goto(-50,250)
                      # INTERPRETS AND MATCHES COMBINATION FOR RANDOM CODE AND YOUR CODE
                      # W = RED RESULT , V = WHITE RESULT , OTHERS ARE BLANK
                      if(a==A):
                            p="w"
                      elif(a==B or a==C):
                            p="v"
                      elif(a==D or a==E):
                            p="v"
                      elif(a==0 ):
                            p="-"
                      elif (a==9):
                            p="["
                      else:
                            p=""                                 
                      if(b==B):
                            q="w"
                      elif(b==A or b==C):
                            q="v"
                      elif(b==D or b==E):
                            q="v"
                      else:
                            q=""
                      if(c==C):
                            r="w"
                      elif(c==B or c==A):
                            r="v"
                      elif(c==D or c==E):
                            r="v"
                      else:
                            r=""
                      if(d==D):
                            s="w"
                      elif(d==B or d==C):
                            s="v"
                      elif(d==A or d==E):
                            s="v"
                      else:
                            s=""
                      if(e==E):
                            t="w"
                      elif(e==B or e==C):
                            t="v"
                      elif(e==D or e==A):
                            t="v"
                      else:
                            t=""
                #PRINTS THE SIDE CODE IN A SORTED MANNER AND MAKES UP CODE IN V AND W FORM TO ANALYZE
                      code = (p+q+r+s+t)
                      code = sorted(code)
                      soplist = [120,105,90,75,60]
                      gobhi = 0
                      ox = len(code)
                      for yyy in soplist :
                                 if gobhi == ox:
                                         break
                                 if code[gobhi] == "w" :
                                            jynx.goto(sop+5,yyy-5)
                                            jynx.pendown()
                                            jynx.color('red')
                                            jynx.begin_fill()
                                            jynx.circle(4)
                                            jynx.end_fill()
                                            jynx.penup()
                                            jynx.goto(1000,1000)
                                 elif code[gobhi] == "v" :
                                            jynx.goto(sop+5,yyy-5)
                                            jynx.pendown()
                                            jynx.color('white')
                                            jynx.begin_fill()
                                            jynx.circle(4)
                                            jynx.end_fill()
                                            jynx.penup()
                                            jynx.goto(1000,1000)
                                 else :
                                            continue
                                 gobhi = gobhi + 1
                        # IF ALL RED YOU WIN
                      if code == ["w","w","w","w","w"] :
                                 hidepeg.goto(-220,400)
                                 hidepeg.showturtle()
                                 jynx.goto(-300,220)
                                 jynx.color('red')
                                 jynx.write("YOU WIN !",align="left",font=("candara",28,"bold"))
                                 codex = [A,B,C,D,E]
                                 ylist = [-5,-55,-105,-155,-205]
                                 yon = 0
                                 replay.goto(320,260)
                                 replay.write("RE-PLAY",align="left",font=("candara",15,"bold"))
                                 replay.showturtle()
                                 replay.goto(355,230)
                                 
                                 #RESET PLACES FOR MAIN COLOUR TURTLES
                                 for con in codex :
                                         if con == 1 :
                                                 col1.goto(490 ,ylist[yon])
                                         elif con == 2 :
                                                 col2.goto(490 ,ylist[yon])
                                         elif con == 3 :
                                                 col3.goto(490 ,ylist[yon])
                                         elif con == 4 :
                                                 col4.goto(490 ,ylist[yon])
                                         elif con == 5 :
                                                 col5.goto(490 ,ylist[yon])
                                         elif con == 6 :
                                                 col6.goto(490 ,ylist[yon])
                                         elif con == 7 :
                                                 col7.goto(490 ,ylist[yon])
                                         elif con == 8 :
                                                 col8.goto(490 ,ylist[yon])
                                         yon = yon + 1
        #IF YOU USED MORE THAN 13 CHANCES AND DIDN'T WIN YOU LOSE
           elif confirmwork >= 13 :
                         lavapede.goto(-380,240)
                         lavapede.color('black')
                         lavapede.write("YOU LOST ",align="left",font=("candara",17,"bold"))
                         codex = [A,B,C,D,E]
                         ylist = [-5,-55,-105,-155,-205]
                         yon = 0
                         replay.goto(320,260)
                         replay.write("RE-PLAY",align="left",font=("candara",15,"bold"))
                         replay.showturtle()
                         replay.goto(355,230)
                         #RESET PLACES FOR MAIN COLOUR TURTLES
                         for con in codex :
                                 if con == 1 :
                                         col1.goto(490 ,ylist[yon])
                                 elif con == 2 :
                                         col2.goto(490 ,ylist[yon])
                                 elif con == 3 :
                                         col3.goto(490 ,ylist[yon])
                                 elif con == 4 :
                                         col4.goto(490 ,ylist[yon])
                                 elif con == 5 :
                                         col5.goto(490 ,ylist[yon])
                                 elif con == 6 :
                                         col6.goto(490 ,ylist[yon])
                                 elif con == 7 :
                                         col7.goto(490 ,ylist[yon])
                                 elif con == 8 :
                                         col8.goto(490 ,ylist[yon])
                                 yon = yon + 1
           else :
                   #IF ALL SLOTS ARE NOT FILLED YET
                      hidepeg.goto(-220,400)
                      hidepeg.showturtle()
                      lavapede.goto(-380,240)
                      lavapede.color('white')
                      lavapede.write("PLEASE FILL ALL THE SLOTS FIRST !",align="left",font=("candara",17,"bold"))
                      time.sleep(1)
                      lavapede.clear()
                      hidepeg.hideturtle()
                      hidepeg.goto(1000,1000)

#MAKING ALL THE MAIN COLOUR TURTLES ( THIS IS THE FIRST STEP AFTER BOARD MAKING, BEFORE WERE JUST DEFINED FUNCTIONS)
lavapede = turtle.Turtle()
lavapede.penup()
lavapede.speed(1000)
lavapede.hideturtle()
hidepeg = turtle.Turtle()
hidepeg.color('gray10')
hidepeg.penup()
hidepeg.shape('square')
hidepeg.shapesize(20)
hidepeg.hideturtle()
hidepeg.speed(1000)
hidepeg.goto(1000,1000)
jynx = turtle.Turtle()
jynx.color("white")
jynx.hideturtle()
jynx.speed(1000)
jynx.penup()
loading.clear()
loading.write(load[3],align="left",font=("candara",15,"bold"))
col1 = turtle.Turtle()
col1.penup()
col1.shape('circle')
col1.color('blue')
col1.shapesize(1.5)
col1.speed(100)
col1.goto(-400,250)
col1.onclick(got1)
col2 = turtle.Turtle()
col2.penup()
col2.shape('circle')
col2.color('red')
col2.shapesize(1.5)
col2.speed(100)
col2.goto(-350,250)
col2.onclick(got2)
loading.clear()
loading.write(load[4],align="left",font=("candara",15,"bold"))
col3 = turtle.Turtle()
col3.penup()
col3.shape('circle')
col3.color('magenta')
col3.shapesize(1.5)
col3.speed(100)
col3.goto(-300,250)
col3.onclick(got3)
col4 = turtle.Turtle()
col4.penup()
col4.shape('circle')
col4.color('LightSkyBlue')
col4.shapesize(1.5)
col4.speed(100)
col4.goto(-250,250)
col4.onclick(got4)
loading.clear()
loading.write(load[5],align="left",font=("candara",15,"bold"))
col5 = turtle.Turtle()
col5.penup()
col5.shape('circle')
col5.color('yellow')
col5.shapesize(1.5)
col5.speed(100)
col5.goto(-200,250)
col5.onclick(got5)
replay = turtle.Turtle()
replay.shape('circle')
replay.color('LightYellow')
replay.shapesize(2.5)
replay.hideturtle()
replay.penup()
replay.speed(1000)
replay.goto(1000,1000)
replay.onclick(replaying)
col6 = turtle.Turtle()
col6.penup()
col6.shape('circle')
col6.color('orange')
col6.shapesize(1.5)
col6.speed(100)
col6.goto(-150,250)
col6.onclick(got6)
loading.clear()
loading.write(load[0],align="left",font=("candara",15,"bold"))
col7 = turtle.Turtle()
col7.penup()
col7.shape('circle')
col7.color('white')
col7.shapesize(1.5)
col7.speed(100)
col7.goto(-100,250)
col7.onclick(got7)
col8 = turtle.Turtle()
col8.penup()
col8.shape('circle')
col8.color('dark violet')
col8.shapesize(1.5)
col8.speed(100)
col8.goto(-50,250)
col8.onclick(got8)
loading.clear()
loading.write(load[1],align="left",font=("candara",15,"bold"))
surrender = turtle.Turtle()
surrender.penup()
surrender.shape('circle')
surrender.color('IndianRed1')
surrender.speed(10000)
surrender.shapesize(2.5)
surrender.goto(200,260)
surrender.write("SURRENDER",align="left",font=("candara",15,"bold"))
surrender.onclick(surrendering)
surrender.goto(245,230)
confirm = turtle.Turtle()
confirm.penup()
confirm.shape('circle')
confirm.color('bisque')
confirm.speed(10000)
confirm.shapesize(2.5)
confirm.goto(100,260)
confirm.write("CONFIRM",align="left",font=("candara",15,"bold"))

confirm.goto(140,230)
#THIS FUNCTION JUST BELOW CALLS FOR THE MAIN ENGINE THAT CHECKS THE CODE
confirm.onclick(confirmation)
####ABOVE FUNCTION WORKS FOR ALL THE TIME WHILE THE SCREEN IS OPEN
loading.clear()
loading.write(load[2],align="left",font=("candara",15,"bold"))
loading.clear()
#LISTENING TO KEYS
wn.listen()
wn.onkeypress(got8,"1")
wn.onkeypress(got2,"2")
wn.onkeypress(got3,"3")
wn.onkeypress(got4,"4")
wn.onkeypress(got5,"5")
wn.onkeypress(got6,"6")
wn.onkeypress(got7,"7")
wn.onkeypress(got8,"8")
wn.onkeypress(confirmation,"Return")
wn.onkeypress(surrendering,"Escape")

turtle.done()