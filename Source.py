         # Title-     Rock Paper Scissor Game
         # label-       Rock paper Scissor
         #            -Player- -vs- -Computer-
         #            -------------------
         #          -Rock-  -Paper-  -Scissor-
         #               -Reset Game-


from tkinter import *
import random

window = Tk()

window.geometry("300x300")

window.title("Rock Paper Scissor Game")

window.config(background="purple")

ai_option = {
    0: "Rock",
    1: "Paper",
    2: "Scissor"
}

def reset_game():
    button1["state"] = "active"
    button2["state"] = "active"
    button3["state"] = "active"
    label1.config(text="Player     ")
    label3.config(text="    Computer")
    label4.config(text="")

def button_disable():
    button1["state"] = "disable"
    button2["state"] = "disable"
    button3["state"] = "disable"

def player_selected_rock():
    ai_picked = ai_option[random.randint(0, 2)]
    if ai_picked == "Rock":
        match_result = "=====Draw====="
    elif ai_picked == "Scissor":
        match_result = ":) You Win :)"
    else:
        match_result = "AI Win"
    label4.config(text=match_result)
    label1.config(text="Rock     ")
    label3.config(text=ai_picked)
    button_disable()

def player_selected_paper():
    ai_picked = ai_option[random.randint(0, 2)]
    if ai_picked == "Paper":
        match_result = "=====Draw====="
    elif ai_picked == "Scissor":
        match_result = "Computer Win"
    else:
        match_result = ":) You Win :)"
    label4.config(text=match_result)
    label1.config(text="Paper     ")
    label3.config(text=ai_picked)
    button_disable()

def player_selected_scissor():
    ai_picked = ai_option[random.randint(0,2)]
    if ai_picked == "Rock":
        match_result = "Computer Win"
    elif ai_picked == "Scissor":
        match_result = "=====Draw====="
    else:
        match_result = ":) You Win :)"
    label4.config(text=match_result)
    label1.config(text="Scissor     ")
    label3.config(text=ai_picked)
    button_disable()

Label(window,text="Rock Paper Scissor",background="purple",font="normal 20 bold",fg="blue").pack(pady=20)

frame = Frame(window)
frame.pack()


label1 = Label(frame,background="Purple",text="Player      ",font=30)

label2 = Label(frame,background="Purple",text="   VS    ",font=30)

label3 = Label(frame,background="Purple",text="     Computer",font=30)

label1.pack(side=LEFT)
label2.pack(side=LEFT)
label3.pack()

label4 = Label(window,text="",font="normal 20 bold",bg="white",width=15,borderwidth=2,relief="solid")

label4.pack(pady=20)

frame1 = Frame(window)
frame1.pack()

button1 = Button(frame1,background="fuchsia", text="Rock",font=10, width=7,command=player_selected_rock)

button2 = Button(frame1,background="Fuchsia", text="Paper ",font=10, width=7,command=player_selected_paper)

button3 = Button(frame1,background="Fuchsia", text="Scissor",font=10, width=7,command=player_selected_scissor)

button1.pack(side=LEFT)
button2.pack(side=LEFT)
button3.pack(side=RIGHT)

Button(window,text="Reset Game",background="Grey",font=10, fg="BLack", command=reset_game).pack(pady=20)

window.mainloop()