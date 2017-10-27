import turtle
import os

op1 = True
op2 = op3 = op4 = op5 = op7 = op6 = op8 = op9 = op10 = op11 = op12 = op13 = False
t1w = turtle.Turtle()
t2w = turtle.Turtle()
t3w = turtle.Turtle()
t4w = turtle.Turtle()

t = turtle.Turtle()
t.color("white")
t.penup()

points = 0


def selectionbox(x, y):
    global op1, op2, op3, op4, op5, op6, op7,op8,op9,op10,op11,op12, op13, points

    if op1:
        if x > -547 and x < -250 and y > -49 and y < 124:      #GOOD
            op1 = False
            op2 = True
            t3w.clear(), t1w.clear(), t2w.clear()
            t3w.write("College scouts have been watching your game since you were a freshman but you've narrowed your options down to two colleges. UCLA and Kentucky.\nYou will put up stats on UCLA but your draft stock might go down due to your inevitable dissapointing record. On the other hand, Kentucky\n have offered you spot as the second option and are frequent title contenders. Which will you choose?", False, align="left", font=("Times New Roman", 18, "normal"))
            t1w.penup()
            t1w.goto(-475,50)
            t1w.pendown()
            t1w.write(" Kentucky", False, align="left", font=("Times New Roman", 24, "normal"))
            t2w.penup()
            t2w.goto(325,50)
            t2w.write("UCLA", False, align="left", font=("Times New Roman", 24, "normal"))



        elif x > 225 and x < 547 and y > -47 and y < 124:
            op1= False
            op3 = True
            t3w.clear(), t1w.clear(), t2w.clear()
            t3w.write("Among international basketball, 2 countries reign king; Spain and China. Both countries are home to competitive leagues stuffed with unsigned NBA free\nagents, retired NBA vets, and seasoned international ballers.Your draft stock might take a dip because of your unorthodox route to the league but your \nskills are sure to improve playing amongst the best in the world",False, align="left", font=("Times New Roman", 18, "normal"))
            t1w.penup()
            t1w.goto(-475, 50)
            t1w.pendown()
            t1w.write("China", False, align="left", font=("Times New Roman", 24, "normal"))
            t2w.penup()
            t2w.goto(325, 50)
            t2w.write("Spain", False, align="left", font=("Times New Roman", 24, "normal"))



    elif op2:
        if x > -547 and x < -250 and y > -49 and y < 124:
            op2 = False
            op4 = True
            t3w.clear(), t1w.clear(), t2w.clear()
            t3w.write(" You have made Kentucky's Roster. This puts you in a great position to win the NCAA tourney and improve your draft stock.\n March Madness starts next week and you have 2 options. Your coach has offered you a starting spot but you twisted your ankle\n during the regular season and would like to rest. What will you do?",False, align="left", font=("Times New Roman", 18, "normal"))
            t1w.penup()
            t1w.goto(-500, 50)
            t1w.pendown()
            t1w.write(" Start and play more minutes", False, align="left", font=("Times New Roman", 20, "normal"))
            t2w.penup()
            t2w.goto(300, 50)
            t2w.write("Come off bench and rest ankle", False, align="left", font=("Times New Roman", 20, "normal"))

        elif x > 225 and x < 547 and y > -47 and y < 124:  #GOOD
            op2 = False
            op6 = True
            t3w.clear(), t1w.clear(), t2w.clear()
            t3w.penup()
            t3w.right(90), t3w.forward(30)
            t3w.write("California has treated you well.  On UCLA you have put up monster numbers and are by far the best player on the team. The regular season\n is coming to an end and you've earned the title of NCAA player of the year(+10 Points)but your team has no hopes of becoming\nthe NCAA champion.You have impressed NBA talent scouts and are predicted to go in the top-3. Click either box to continue to draft day.  ",False, align="left", font=("Times New Roman", 18, "normal"))
            points = points + 10
            t4w.clear()
            t4w.write(" MVP - 50 Points \n All NBA First Team - 30 Points \n All NBA Second Team - 20 Points \n All NBA Third Team - 15 Points \n Championship - 30 Points \n Rookie of the Year - 10 Points \n Sixth Man - 10 Points \n Defensive Player of Year - 10 Points \n Playoffs - 10 Points \n NCAA Player of the Year - 10 Points \nInternational Player of the Year - 10 points \n NCAA Champs - 10 Points\n Current Points - " + str(points), False, align="left", font=("Times New Roman", 14, "normal"))
            t1w.penup()
            t1w.goto(-565, 50)
            t1w.pendown()
            t1w.write("Continue to Draft", False, align="left", font=("Times New Roman", 20, "normal"))
            t2w.penup()
            t2w.goto(325, 50)
            t2w.write("Continue to Draft", False, align="left", font=("Times New Roman", 24, "normal"))

    elif op3:
        if x > -547 and x < -250 and y > -49 and y < 124:
            op3 = False
            op6 = True
            t3w.clear(), t1w.clear(), t2w.clear()
            t3w.write("Your season in China is coming to a close. You absolutely big bodied everyone and NBA scouts are starting to take notice.\nYou did not recieve the international player of the year award but are projected to go top 5.  You have been invited to a predraft workout\nwith the Golden State Warriors and one with the Los Angeles Lakers. Which will you attend?", False, align="left", font=("Times New Roman", 20, "normal"))
            t1w.penup()
            t1w.goto(-475,50)
            t1w.pendown()
            t1w.write(" Warriors", False, align="left", font=("Times New Roman", 24, "normal"))
            t2w.penup()
            t2w.goto(325,50)
            t2w.write("Lakers", False, align="left", font=("Times New Roman", 24, "normal"))



        elif x > 225 and x < 547 and y > -47 and y < 124:
            op3= False
            op6 = True
            t3w.clear(), t1w.clear(), t2w.clear()
            t3w.write("Going to Spain was definetly a good career choice for you. The slow paced game allowed you to compete and work on your game\nwith little risk of injury. You were the star player of your pro club and the international player of the year(+10 points).\nYour durablity and skill has you projected top 10.You have been invited to a predraft workout with the Golden State Warriors and one with the Los Angeles Lakers.\nWhich will you attend?", False, align="left", font=("Times New Roman", 20, "normal"))
            points = points + 10
            t4w.clear()
            t4w.write(" MVP - 50 Points \n All NBA First Team - 30 Points \n All NBA Second Team - 20 Points \n All NBA Third Team - 15 Points \n Championship - 30 Points \n Rookie of the Year - 10 Points \n Sixth Man - 10 Points \n Defensive Player of Year - 10 Points \n Playoffs - 10 Points \n NCAA Player of the Year - 10 Points \nInternational Player of the Year - 10 points \n NCAA Champs - 10 Points\n Current Points - " + str(points), False, align="left", font=("Times New Roman", 14, "normal"))
            t3w.penup()
            t3w.goto(-475, 50)
            t3w.pendown()
            t3w.write("Lakers", False, align="left", font=("Times New Roman", 24, "normal"))
            t2w.penup()
            t2w.goto(325, 50)
            t2w.write("Warriors", False, align="left", font=("Times New Roman", 24, "normal"))
    elif op4:
        if x > -547 and x < -250 and y > -49 and y < 124:   #GOOD
            op4 = False
            op6 = True
            t3w.clear(), t1w.clear(), t2w.clear()
            t3w.write(" Uh oh. Your twisted ankle popped right out in your first game.  Probably should have rested it a little more.\n Your team loses the NCAA playoffs and you do not get to participate in the tournament.\nClick either selection box to continue to the draft, where your recently twisted ankle has lowered your draft stock to the twenties.",False, align="left", font=("Times New Roman", 18, "normal"))
            t1w.penup()
            t1w.goto(-500, 50)
            t1w.pendown()
            t1w.write(" Continue to Draft", False, align="left", font=("Times New Roman", 20, "normal"))
            t2w.penup()
            t2w.goto(300, 50)
            t2w.write("Continue to Draft", False, align="left", font=("Times New Roman", 20, "normal"))
        elif x > 225 and x < 547 and y > -47 and y < 124:
            op4= False
            op6 = True
            t3w.clear(), t1w.clear(), t2w.clear()
            t3w.write("Wow. Just wow. You came off the bench and tore it up. Within a few games you were ready to start.\nYou went on to lead your to team to the NCAA championship(+10 points). And have made a great impression on all NBA scouts\nfor your playmaking, composure, and descision making. You are projected to be in the top 10. Click either box to continue to draft day", False, align="left", font=("Times New Roman", 20, "normal"))
            points = points + 10
            t4w.clear()
            t4w.write(" MVP - 50 Points \n All NBA First Team - 30 Points \n All NBA Second Team - 20 Points \n All NBA Third Team - 15 Points \n Championship - 30 Points \n Rookie of the Year - 10 Points \n Sixth Man - 10 Points \n Defensive Player of Year - 10 Points \n Playoffs - 10 Points \n NCAA Player of the Year - 10 Points \nInternational Player of the Year - 10 points \n NCAA Champs - 10 Points\n Current Points - " + str(points), False, align="left", font=("Times New Roman", 14, "normal"))
            t3w.penup()
            t3w.goto(-475, 50)
            t3w.pendown()
            t3w.write("Draft", False, align="left", font=("Times New Roman", 24, "normal"))
            t2w.penup()
            t2w.goto(325, 50)
            t2w.write("Draft", False, align="left", font=("Times New Roman", 24, "normal"))
    elif op6:
            op6 = False
            op10 = True
            t3w.clear(), t1w.clear(), t2w.clear()
            t3w.penup()
            t3w.goto(-564,-425)
            t3w.write("Draft day. This is where your journey truly starts.  This is what dreams are made of.\nPre-draft workouts went well and the Lakers and the Warriors have agreed to draft you if given the chance.\n The warriors are title contenders and the Lakers are a young and hungry playoff bound dynasty.  Which will you choose?",False, align="left", font=("Times New Roman", 18, "normal"))
            t1w.penup()
            t1w.goto(-500, 50)
            t1w.pendown()
            t1w.write("Lakers", False, align="left", font=("Times New Roman", 20, "normal"))
            t2w.penup()
            t2w.goto(300, 50)
            t2w.write("Warriors", False, align="left", font=("Times New Roman", 20, "normal"))
    elif op10:
        if x > -547 and x < -250 and y > -49 and y < 124:      #GOOD
            op10 = False
            op11 = True
            t3w.clear(), t1w.clear(), t2w.clear()
            t3w.write("The regular season is over and the warriors absolutely crushed the competition.\n The team is set a new wins record and you were awarded the sixth man and ROY award.(+15 points) Click either box to continue to playoffs.  ", False, align="left", font=("Times New Roman", 18, "normal"))
            points = points + 20
            t4w.clear()
            t4w.write(" MVP - 50 Points \n All NBA First Team - 30 Points \n All NBA Second Team - 20 Points \n All NBA Third Team - 15 Points \n Championship - 30 Points \n Rookie of the Year - 10 Points \n Sixth Man - 10 Points \n Defensive Player of Year - 10 Points \n Playoffs - 10 Points \n NCAA Player of the Year - 10 Points \nInternational Player of the Year - 10 points \n NCAA Champs - 10 Points\n Current Points - " + str( points), False, align="left", font=("Times New Roman", 14, "normal"))
            t1w.penup()
            t1w.penup()
            t1w.goto(-475,50)
            t1w.pendown()
            t1w.write(" Continue to Playoffs", False, align="left", font=("Times New Roman", 24, "normal"))
            t2w.penup()
            t2w.goto(325,50)
            t2w.write("Continue to Playoffs", False, align="left", font=("Times New Roman", 24, "normal"))

        elif x > 225 and x < 547 and y > -47 and y < 124:
            op10= False
            op11 = True
            t3w.clear(), t1w.clear(), t2w.clear()
            t3w.write("It was a breakout season for the young lakers. You and another UCLA alumni took the league by storm.\n You were awarded the ROY and ALL NBA Third team nods(+25 points).  Click either box to continue to playoffs",False, align="left", font=("Times New Roman", 18, "normal"))
            points = points + 25
            t4w.clear()
            t4w.write(" MVP - 50 Points \n All NBA First Team - 30 Points \n All NBA Second Team - 20 Points \n All NBA Third Team - 15 Points \n Championship - 30 Points \n Rookie of the Year - 10 Points \n Sixth Man - 10 Points \n Defensive Player of Year - 10 Points \n Playoffs - 10 Points \n NCAA Player of the Year - 10 Points \nInternational Player of the Year - 10 points \n NCAA Champs - 10 Points\n Current Points - " + str(points), False, align="left", font=("Times New Roman", 14, "normal"))
            t1w.penup()
            t1w.penup()
            t1w.goto(-475, 50)
            t1w.pendown()
            t1w.write(" Continue to Playoffs", False, align="left", font=("Times New Roman", 24, "normal"))
            t2w.penup()
            t2w.goto(325, 50)
            t2w.write(" Continue to Playoffs", False, align="left", font=("Times New Roman", 24, "normal"))

    elif op11:
            op11 = False
            op12 = True
            t3w.clear(), t1w.clear(), t2w.clear()
            t3w.write(" NBA Finals.  Game 7. Season went by so fast.  But this is what it all led up to.\nClock winding down. Ball in your hands. 3... 2... 1...\n Pass or Shoot?",False, align="left", font=("Times New Roman", 18, "normal"))
            t1w.penup()
            t1w.goto(-500, 50)
            t1w.pendown()
            t1w.write("Pass", False, align="left", font=("Times New Roman", 20, "normal"))
            t2w.penup()
            t2w.goto(300, 50)
            t2w.write("Shoot", False, align="left", font=("Times New Roman", 20, "normal"))
    elif op12:
        if x > -547 and x < -250 and y > -49 and y < 124:  # GOOD
            op12 = False
            op13 = True
            t3w.clear(), t1w.clear(), t2w.clear()
            t3w.write("You hit the open man and he drilled it!  You won the championship congrats! ",False, align="left", font=("Times New Roman", 18, "normal"))
            points = points + 50
            t4w.clear()
            t4w.write(" MVP - 50 Points \n All NBA First Team - 30 Points \n All NBA Second Team - 20 Points \n All NBA Third Team - 15 Points \n Championship - 30 Points \n Rookie of the Year - 10 Points \n Sixth Man - 10 Points \n Defensive Player of Year - 10 Points \n Playoffs - 10 Points \n NCAA Player of the Year - 10 Points \nInternational Player of the Year - 10 points \n NCAA Champs - 10 Points\n Current Points - " + str( points), False, align="left", font=("Times New Roman", 14, "normal"))
            t1w.penup()
            t1w.goto(-475, 50)
            t1w.pendown()
            t1w.write("Did you get 100 points?", False, align="left", font=("Times New Roman", 16, "normal"))
            t2w.penup()
            t2w.goto(325, 50)
            t2w.write("Did you get 100 points?", False, align="left", font=("Times New Roman", 16, "normal"))

        elif x > 225 and x < 547 and y > -47 and y < 124:
            op12 = False
            op13 = True
            t3w.clear(), t1w.clear(), t2w.clear()
            t3w.write("Swish.  Jordan-like.  You made the gamewinner, won the championship, and also gained MVP nods for your performance.\n (+80 points)",False, align="left", font=("Times New Roman", 18, "normal"))
            points = points + 80
            t4w.clear()
            t4w.write(" MVP - 50 Points \n All NBA First Team - 30 Points \n All NBA Second Team - 20 Points \n All NBA Third Team - 15 Points \n Championship - 30 Points \n Rookie of the Year - 10 Points \n Sixth Man - 10 Points \n Defensive Player of Year - 10 Points \n Playoffs - 10 Points \n NCAA Player of the Year - 10 Points \nInternational Player of the Year - 10 points \n NCAA Champs - 10 Points\n Current Points - " + str(points), False, align="left", font=("Times New Roman", 14, "normal"))
            t1w.penup()
            t1w.penup()
            t1w.goto(-475, 50)
            t1w.pendown()
            t1w.write(" Did you get 100 points?", False, align="left", font=("Times New Roman", 24, "normal"))
            t2w.penup()
            t2w.goto(325, 50)
            t2w.write(" Did you get 100 points?", False, align="left", font=("Times New Roman", 24, "normal"))


def main():
    global points

    wn = turtle.Screen()
    t1b = turtle.Turtle()
    image = turtle.Turtle()

    t1b.tracer(2)


    t1b.pensize(6)
    t1b.pencolor("gray")

    t1b.penup()
    t1b.goto(-250,-50)
    t1b.pendown()
    for i in range (2):
        t1b.left(90)                    # drawing selection box 1
        t1b.forward(175)
        t1b.left(90)
        t1b.forward(325)

    t1b.penup()
    t1b.goto(550,-50)
    t1b.pendown()
    for i in range(2):
        t1b.left(90)                    # drawing selection box 2
        t1b.forward(175)
        t1b.left(90)
        t1b.forward(325)

    t1b.penup()
    t1b.goto(550,-450)
    t1b.pendown()
    for i in range(2):
        t1b.left(90)                    # drawing dialogue box
        t1b.forward(175)
        t1b.left(90)
        t1b.forward(1125)


    wn.addshape(os.path.expanduser("nbalogo.gif"))
    image.shape(os.path.expanduser("nbalogo.gif"))             # nba logo image

    t1b.penup()
    t1b.goto(250,225)
    t1b.pendown()
    for i in range(2):
        t1b.left(90)                    # drawing accolade box
        t1b.forward(275)
        t1b.left(90)
        t1b.forward(525)

    t4w.penup()
    t4w.goto(-110,455)
    t4w.write(" Point Index - 100 to Win", False, align="left", font=("Times New Roman",20, "normal"))
    t4w.goto(-110,250)
    t4w.pencolor("black")
    t4w.write(" MVP - 50 Points \n All NBA First Team - 30 Points \n All NBA Second Team - 20 Points \n All NBA Third Team - 15 Points \n Championship - 30 Points \n Rookie of the Year - 10 Points \n Sixth Man - 10 Points \n Defensive Player of Year - 10 Points \n Playoffs - 10 Points \n NCAA Player of the Year - 10 Points \nInternational Player of the Year - 10 points \n NCAA Champs - 10 Points\n Current Points - " + str(points), False, align="left", font=("Times New Roman", 14, "normal"))


    t3w.penup()
    t3w.goto(-565,-400)
    t3w.pencolor("black")                        # Dialogue
    t3w.pendown()
    t3w.write("Congratulations! You have graduated high school as the top prospect in your class.  You are well on your way to become an NBA superstar.\nHowever, you still need to deciede whether or not to go to college! College scouts have already been recruiting you \nbut you have also been intrested in professional international play. It is up to you to decide what is better for your career.\nYour choices along the way will determine the amount of points you receive. 100 and you make the hall of fame. Good Luck!", False, align="left", font=("Times New Roman", 18, "normal"))

    t1w.penup()
    t1w.goto(-450, 50)
    t1w.pendown()                                 # selection box 1 text
    t1w.write("College", False, align="left", font=("Times New Roman", 24, "normal"))

    t2w.penup()
    t2w.goto(350, 50)
    t2w.pendown()                       # selection box 2 text
    t2w.write("International", False, align="left", font=("Times New Roman", 24, "normal"))

    for i in range(30):
        t1b.left(1)


    wn.onscreenclick(selectionbox)

    turtle.done()


main()