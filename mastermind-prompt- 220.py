#generation of code
import random
def mainm():
         lop =0
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
#game code
         a=b=c=d=e=p=q=r=s=t=var=error=0
         code = ""
         print("put your code-")
         while (var>=0):
                   
                   if (code == "▣▣▣▣▣"):
                             break
                   elif(code == "-----"):
                             break
                   elif(code == "_____"):
                             print("Don't be a cheater! play honestly")
                             code = "."
                             continue
                   else:
                             while True:
                                       try:
                                                 a,b,c,d,e=map( int, input().split())
                                                 break
                                       except ValueError:
                                                 print("Check your code and type it again correctly.")
                                                 print("Enter the code again")
                                                 continue
#smooth gaming
                             if(a==b or a==c):
                                       print("Check your code, repetition is not allowed.")
                                       print("enter the code again")
                                       continue
                             elif(a==d or a==e):
                                       print("Check your code, repetition is not allowed.")
                                       print("enter the code again")
                                       continue
                             elif(b==c or b==d):
                                       print("Check your code, repetition is not allowed.")
                                       print("enter the code again")
                                       continue
                             elif(b==e or c==d):
                                       print("Check your code, repetition is not allowed.")
                                       print("enter the code again")   
                                       continue
                             elif(c==e or d==e):
                                       print("Check your code, repetition is not allowed.")
                                       print("enter the code again")
                                       continue
                             if(a//10!=0):
                                       print("Check your code,use single digits")
                                       continue
                             if(b//10!=0):
                                       print("Check your code,use single digits")
                                       continue
                             if(c//10!=0):
                                       print("Check your code,use single digits")
                                       continue
                             if(d//10!=0):
                                       print("Check your code,use single digits")
                                       continue
                             if(e//10!=0):
                                       print("Check your code,use single digits")
                                       continue
#scoring                      
                             if(a==A):
                                       p="▣"
                             elif(a==B or a==C):
                                       p="▢"
                             elif(a==D or a==E):
                                       p="▢"
                             elif(a==0 ):
                                       p="-"
                             elif (a==9):
                                       p="["
                             else:
                                       p=""                                 
                             if(b==B):
                                       q="▣"
                             elif(b==A or b==C):
                                       q="▢"
                             elif(b==D or b==E):
                                       q="▢"
                             else:
                                       q=""
                             if(c==C):
                                       r="▣"
                             elif(c==B or c==A):
                                       r="▢"
                             elif(c==D or c==E):
                                       r="▢"
                             else:
                                       r=""
                             if(d==D):
                                       s="▣"
                             elif(d==B or d==C):
                                       s="▢"
                             elif(d==A or d==E):
                                       s="▢"
                             else:
                                       s=""
                             if(e==E):
                                       t="▣"
                             elif(e==B or e==C):
                                       t="▢"
                             elif(e==D or e==A):
                                       t="▢"
                             else:
                                       t=""
#shuffling the score
                             shuffle =1
                             if (shuffle ==1):
                                       code =(p+q+r+s+t)
                             elif (shuffle ==2):
                                       code =(p+r+q+s+t)
                             elif (shuffle ==3):
                                       code =(p+s+r+q+t)
                             elif (shuffle ==4):
                                       code =(t+q+r+s+p)
                             elif (shuffle ==5):
                                       code =(t+s+r+q+p)
                             elif (shuffle ==6):
                                       code =(p+t+r+s+q)
                             elif (shuffle ==7):
                                       code =(q+p+r+s+t)
                             elif (shuffle ==8):
                                       code =(p+r+q+t+s)
                             elif (shuffle ==9):
                                       code =(s+q+p+r+t)
                             else:
                                       shuffle =0
                                       code =(s+q+r+p+t)
                             shuffle+=1
                             if (p=="-"):
                                       code = "-----"
                             if (p=="["):
                                       code = "_____"
                                       
                             print(code)
#results/end                              
                   var+=1                    
         if (code == "▣▣▣▣▣"):
                   print("Great ! You CRACKED THE CODE in",var,"chances.")
         
         elif(code == "-----"):
                   print ("you gave-up, the code was ",A,B,C,D,E)

#rules for the game
def rulesm():
         print()
         print()
         print()
         print()
         print()
         print()
         print()
         print()
         print()
         print()
         print()
         print()
         print()
         print()
         print("-----------------------------------------------------------------------------------------")
         print("MASTERMIND, a game to crack the code")
         print("-----------------------------------------------------------------------------------------")
         print()
         print("THERE IS A 5 DIGIT CODE, CRACK IT !!")
         print("RULES:")
         print("Enter a number code using digits 1 to 8. ")
         print("Please put SINGLE SPACES with SPACES in between.")
         print("No repeat of numbers allowed.")
         print("▣ means that you have a number in your code which is in CORRECT position.")
         print("▢ means that you have a number in your code which is there but in WRONG position.")
         print("Number of total boxes determines how many numbers you have there in both the codes.")
         print("Type 0 and any four digits if you want to give-up.")
         print("Type 9 and any four digits to cheat.")
         print()
#to play the game
rulesm()
mainm()
print()
#game repeat
repeater = 0
while (repeater==0):
         restart = input("Press p to play again, q to exit  or m to go to menu     -  ")  
         if (restart == "p" or restart=="P"):
                   mainm()
         elif(restart=="m" or restart=="M"):  
                   menu()
         elif(restart=="q" or restart=="Q"):
                   quit()
