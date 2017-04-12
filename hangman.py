import turtle
import random

def main(): #Main Function to Play
    turtle.hideturtle()
    word_list = setup_turt()
    draw_gallows()
    word = choose_word(word_list)
    check_list1 = []
    for x in word:
        check_list1.append(x)
    draw_word(word)
    count = 0
    places = []
    check_list2 = []
    while (count != 6) and (check_list2 != check_list1):
        flag = guess_letter(word)
        if flag != False:
            num = draw_letter(flag,word,places)
            for x in num:
                turtle.penup()
                turtle.goto(400 + (x * 60),900)
                turtle.pendown()
                turtle.write(flag,False,align = "left", font=("Arial",20,"normal"))
                check_list2.insert(x,flag)
        else:
            draw_person(count)
            count += 1
    if count == 6:
        lose_game(word)
    else:
        win_game()

def draw_person(n): #Draws BodyPart
    turtle.penup()
    turtle.goto(500,700)
    turtle.pendown()
    if n == 0: #Based on counter of incorrect guesses, counter goes up
        draw_head()
    elif n == 1:
        draw_torso()
    elif n == 2:
        draw_arm_setup()
        turtle.setheading(230)
        turtle.forward(75)
    elif n == 3:
        draw_arm_setup()
        turtle.setheading(310)
        turtle.forward(75)
    elif n == 4:
        draw_leg_setup()
        turtle.setheading(310)
        turtle.forward(85)
    elif n == 5:
        draw_leg_setup()
        turtle.setheading(230)
        turtle.forward(85)
    turtle.penup()
    turtle.goto(400,900)
    turtle.setheading(0)
    turtle.pendown()



def guess_letter(word): #Allows player to guess letter and tests
    let = turtle.textinput("GUESS","What letter would you like to guess?")
    if str(let) in word:
        return let
    elif str(let) == "":
        return False
    else:
        return False

def draw_gallows(): #Draws Gallows at Beginning
    turtle.penup()
    turtle.goto(750,0)
    turtle.pendown()
    turtle.left(90)
    turtle.forward(800)
    turtle.left(90)
    turtle.forward(250)
    turtle.left(90)
    turtle.forward(100)
    turtle.left(90)

def draw_word(some_word): #Draws Out Lines for Letters
    turtle.penup()
    turtle.goto(400,900)
    turtle.pendown()
    for x in some_word:
        turtle.forward(40)
        turtle.penup()
        turtle.forward(20)
        turtle.pendown()

def choose_word(somelist): #Picks random word from the list of words
    chosen = somelist[random.randint(0,19)]
    return chosen

def setup_turt(): #Sets Up Turtle and List
    turtle.speed(0)
    turtle.delay(0)
    turtle.setworldcoordinates(0,0,1000,1000)
    word_list = ["doctor","west","derelict","coat","muscular","captivity",
    "hurdle","mistaken","parachute","caramel","long","magnetic","legend",
    "hobby","grill","pocket","fossil","identical","plush","luck"]
    return word_list

def draw_head(): #Draws Head
    turtle.penup()
    turtle.forward(50)
    turtle.right(90)
    turtle.forward(50)
    turtle.setheading(90)
    turtle.pendown()
    turtle.circle(50)

def draw_arm_setup(): #Gets pointer into position for arms
    turtle.penup()
    turtle.setheading(270)
    turtle.forward(150)
    turtle.pendown()

def draw_torso(): #Draws torso
    turtle.penup()
    turtle.setheading(0)
    turtle.right(90)
    turtle.forward(100)
    turtle.pendown()
    turtle.forward(200)

def draw_leg_setup(): #Gets pointer into position for legs
    turtle.penup()
    turtle.setheading(270)
    turtle.forward(300)
    turtle.pendown()

def lose_game(word): #Code for when User Loses Game
    turtle.penup()
    turtle.goto(50,150)
    turtle.pendown()
    turtle.write("Sorry, You Lose!",False, align = "left", font = ("Arial",24,"normal"))
    turtle.penup()
    turtle.goto(50,50)
    turtle.write(("Your word was", word),False, align = "left", font = ("Arial", 24, "normal"))
    turtle.penup()
    turtle.goto(-10,-10)
    play_again()

def draw_letter(let,word,some_list): #Draws Letters that Were Guessed Correctly
    new_list = []
    some_list = []
    for x in word:
        new_list += x
    for i,j in enumerate(new_list):
        if let == j:
            some_list.append(i)
    return some_list

def win_game(): #Code for when User Wins Game
    turtle.penup()
    turtle.goto(50,150)
    turtle.pendown()
    turtle.write("Congratulations!!",False, align = "left", font = ("Arial", 24, "normal"))
    play_again()

def play_again(): #Asks user to Play Again
    ans = str(turtle.textinput("PLAY AGAIN","Play Again? (Y/N)"))
    if ans == "Y":
        turtle.reset() #Resets Drawing
        main()
    else:
        return

main()
API Training Shop Blog About
© 2017 GitHub, Inc. Help Support
