from tkinter import *

from tkinter import messagebox

from tkinter import filedialog

import random

# -----------------
# create a window
# -----------------

root=Tk()
root.title("The world of the Games")
root.geometry("500x500+50+30")
root.configure(bg="#1E293B")

# -------------------------
# python's Quiz
# -------------------------

def pythons_Quiz():
    root.withdraw()
    screen2=Toplevel(root)
    screen2.title("Python's Quiz")
    screen2.geometry("600x700")
    screen2.configure(bg="#1E293B")


# -----------------
# Questions
# -----------------

    questions=[

        ("What does print() do?",
        ["Gets input", "Shows output", "Deletes data", "Creates a loop"],
        1,"print() shows output on the screen."),

        ("What is the first index of a list?",
        ["0", "1", "-1", "10"],
        0,"Python lists start at index 0."),

        ("What does len() do?",
        ["Deletes items", "Counts items", "Sorts items", "Adds items"],
        1,"len() counts the number of items."),

        ("Which keyword creates a function?",
        ["func", "def", "function", "make"],
        1,"def is used to create a function."),

        ("What does append() do?",
        ["Adds an item", "Deletes an item", "Sorts a list", "Copies a list"],
        0,
        "append() adds an item to a list in the end."),

        ("Which symbol starts a comment?",
        ["//", "#", "/*", "--"],
        1,"# starts a comment in Python."),

        ("Which one is a string?",
        ["25", "True", '"Hello"', "3.5"],
        2,"Text inside quotes is a string."),

        ("Which one is an integer?",
        ["3.5", "Hello", "10", "True"],
        2,"integer doesn't have decimals."),

        ("Which one is a Boolean?",
        ["Hello", "25", "True", "3.5"],
        2,"True and False are Boolean values."),

        ("What does == mean?",
        ["Assignment", "Equal ", "Not equal", "Greater than"],
        1,"== means Equal."),

        ("Which keyword creates a condition?",
        ["for", "if", "def", "print"],
        1,"if is used to check a condition."),

        ("Which one is a loop?",
        ["if", "for", "def", "return"],
        1,"for is used to create a loop."),

        ("What does break do?",
        ["Stops a loop", "Starts a loop", "Creates a list", "Prints text"],
        0,"break stops a loop."),

        ("What does continue do?",
        ["Skips an iteration", "Stops Python", "Creates a function", "Deletes data"],
        0,"continue skips the current iteration."),

        ("What does input() do?",
        ["Gets user input", "Prints text", "Deletes data", "Creates a loop"],
        0,"input() gets information from the user."),

        ("What does type() do?",
        ["Shows the data type", "Deletes data", "Creates a list", "Sorts data"],
        0,"type() tells you the type of a value."),

        ("What does pop() do?",
        ["Adds an item", "Removes an item", "Sorts a list", "Copies a list"],
        1,"pop() removes an item from a list."),

        ("What does import do?",
        ["Imports a module", "Deletes a module", "Creates a loop", "Prints text"],
        0,"import brings a module into your program."),

        ("What is the output of print(2 + 3)?",
        ["2", "3", "5", "6"],
        2,"2 + 3 equals 5."),

        ("What does a for loop do?",
        ["Repeats code", "Deletes code", "Creates a variable", "Stops Python"],
        0,"A for loop repeats code for each item.")]

# ---------------
# variables
# ---------------

    number=[0]
    score=[0]
    lives=[3]
    answered=[False]

# -----------------
# functions
# -----------------

    def show_question():

        answered[0] = False
        q = questions[number[0]]

        question.config(text="Question " + str(number[0] + 1) + "/20\n\n" + q[0])

        result1.config(text="")

        for i in range(4):
            buttons[i].config(text=q[1][i])

        lives_label.config(
            text="Lives: " + str(lives[0]))

        score_label.config(text="Score: " + str(score[0]))

    def answer(choice):

        if answered[0]:
            return

        answered[0] = True

        q = questions[number[0]]

        if choice == q[2]:
            score[0] += 100
            result1.config(text="Correct! +100 points",fg="#22C55E")

        else:

            lives[0] -= 1
            result1.config(text="Wrong! Correct answer: " +q[1][q[2]] +" Explanation: " +q[3],fg="#EF4444")

        lives_label.config(text="Lives: " + str(lives[0]))
        score_label.config(text="Score: " + str(score[0]))

        next_button.config(state=NORMAL)
        
    def next_question():

        if answered[0] == False:
            return
           
        if lives[0] <= 0:
            question.config(text="GAME OVER!")
            result1.config(text="Final Score: " + str(score[0]),fg="#EF4444")
            return

        number[0] += 1

        if number[0] < 20:
            show_question()
            next_button.config(state=DISABLED)

        else:
            question.config(text="YOU FINISHED!")
            result1.config(text="Final Score: " +str(score[0]) +"/2000",fg="#22C55E")

    def restart():
        number[0] = 0
        score[0] = 0
        lives[0] = 3
        random.shuffle(questions)

        show_question()

    def mainscreen():
        screen2.destroy()
        root.deiconify()

    def go_draw():
        screen2.destroy()
        draw()

    def go_rps():
        screen2.destroy()
        Rps()

    def show_menu2():
        menu2.post(520,50)

# ------------
# labels
# ------------

    title = Label(screen2,text="PYTHON CHALLENGE",font=("Algerian", 25),bg="#1E293B",fg="white")
    title.pack(pady=20)

    lives_label = Label(screen2,text="Lives: 3",font=("Arial", 14),bg="#1E293B",fg="#EF4444")
    lives_label.pack(pady=5)

    score_label = Label(screen2,text="Score: 0",font=("Arial", 14),bg="#1E293B",fg="#22C55E")
    score_label.pack(pady=5)

    question = Label(screen2,text="",font=("Arial", 19),bg="#1E293B",fg="white")
    question.pack(pady=30)

# --------------------
# Answer's button
# --------------------

    buttons = []

    for i in range(4):
        b = Button(screen2,text="",font=("Arial", 13),width=40,bg="#334155",fg="white",activebackground="#3B82F6",activeforeground="white")
        b.pack(pady=5)
        buttons.append(b)


    buttons[0].config(command=lambda: answer(0))
    buttons[1].config(command=lambda: answer(1))
    buttons[2].config(command=lambda: answer(2))
    buttons[3].config(command=lambda: answer(3))    

# --------------
# result
# --------------

    result1 = Label(screen2,text="",font=("Arial", 13),wraplength=580,bg="#1E293B",fg="white")
    result1.pack(pady=15)

# --------------
# buttons
# --------------

    next_button = Button(screen2,text="Next Question",font=("Arial", 13),bg="#3B82F6",fg="white",command=next_question,state=DISABLED)
    next_button.pack(pady=5)

    restart_button = Button(screen2,text="Restart",font=("Arial", 13),bg="#F59E0B",fg="white",command=restart)
    restart_button.pack(pady=5)

    menu_button2=Button(screen2,text="⋮",font=("Arial",18),bg="#3B82F6",fg="white",width=3,height=1,command=show_menu2)    
    menu_button2.place(x=550,y=10)

# --------------
# Menu
# --------------

    menu2=Menu(screen2,tearoff=0)
    menu2.add_command(label="Root",command=mainscreen)
    menu2.add_command(label="Draw",command=go_draw)
    menu2.add_command(label="RPS",command=go_rps)

    show_question()

# -------------------------
# Draw's function
# -------------------------

def draw():
    root.withdraw()
    screen3=Toplevel(root)
    screen3.title("Draw")
    screen3.geometry("600x700")
    screen3.configure(bg="#1E293B")

# ------------
# functions
# ------------
    
    def start_draw(event):
        x[0]=event.x
        y[0]=event.y

    def draw(event):
        ca.create_line(x[0],y[0],event.x,event.y,fill=color[0],width=size[0])
        x[0]=event.x
        y[0]=event.y

        if event.x > canvas_width[0] - 100:
            canvas_width[0] += 100

        if event.y > canvas_height[0] - 100:
            canvas_height[0] += 1000

        ca.configure(scrollregion=(0,0,canvas_width[0],canvas_height[0]))

    def save():
        file=filedialog.asksaveasfilename(defaultextension=".ps",filetypes=[("PostScript files", "*.ps")])

        if file:
            ca.postscript(file=file)

    def back():
        screen3.destroy()
        root.deiconify()

    def show_menu():
        menu.post(520,50)

    def go_to_rps():
        screen3.destroy()
        Rps()

    def go_to_py():
        screen3.destroy()
        pythons_Quiz()
    
    def black():
        color[0]="black"

    def red():
        color[0]="red"

    def blue():
        color[0]="blue"

    def purple():
        color[0]="purple"

    def yellow():
        color[0]="yellow"

    def pink():
        color[0]="pink"

    def brown():
        color[0]="brown"

    def gray():
        color[0]="gray"

    def green():
        color[0]="green"

    def eraser():
        color[0]="white"

    def small():
        size[0]=2

    def medium():
        size[0]=5

    def big():
        size[0]=10

    def clear():
        answer=messagebox.askyesno("warning","Do you want to clear everything ")

        if answer:   
            ca.delete("all")
        
# ------------
# label
# ------------

    la2=Label(screen3,text="Draw anything",font=("algerian",15),fg="#FFFFFF",bg="#1E293B")
    la2.pack(pady=10)

# ------------
# Frame
# ------------

    frame2=Frame(screen3,bg="#334155")
    frame2.pack(pady=5)

    
    drawing_frame=Frame(screen3)
    drawing_frame.pack(fill="both", expand=True)

    drawing_frame.grid_rowconfigure(0, weight=1)
    drawing_frame.grid_columnconfigure(0, weight=1)

# ------------
# canvas
# ------------

    ca=Canvas(drawing_frame,bg="#FFFFFF")
    ca.grid(row=0, column=0, sticky="nsew")


# ------------
# The color
# ------------

    color=["black"]
    size=[5]

    x=[0]
    y=[0]

    canvas_width = [1000]
    canvas_height = [1000]

# --------------- 
# scrollbar
# ---------------
    
    scrollbar_y = Scrollbar(drawing_frame,orient="vertical",command=ca.yview)
    scrollbar_y.grid(row=0, column=1, sticky="ns")

    scrollbar_x = Scrollbar(drawing_frame,orient="horizontal",command=ca.xview)
    scrollbar_x.grid(row=1, column=0, sticky="ew")
    
    ca.configure(xscrollcommand=scrollbar_x.set,yscrollcommand=scrollbar_y.set)


# ---------------
# buttons
# ---------------

    black1=Button(frame2,text="Black",font=("arial",7),bg="#111827",fg="white",width=10,height=2,command=black)
    black1.grid(pady=5,padx=5,row=0,column=0)

    red1=Button(frame2,text="red",font=("arial",7),bg="#EF4444",fg="white",width=10,height=2,command=red)
    red1.grid(pady=5,padx=5,row=0,column=2)

    blue1=Button(frame2,text="Blue",font=("arial",7),bg="#3B82F6",fg="white",width=10,height=2,command=blue)
    blue1.grid(pady=5,padx=5,row=0,column=4)

    purple1=Button(frame2,text="purple",font=("arial",7),bg="#8B5CF6",fg="white",width=10,height=2,command=purple)
    purple1.grid(pady=5,padx=5,row=0,column=6)

    yellow1=Button(frame2,text="yellow",font=("arial",7),bg="#FACC15",fg="black",width=10,height=2,command=yellow)
    yellow1.grid(pady=5,padx=5,row=0,column=8)

    pink1=Button(frame2,text="pink",font=("arial",7),bg="pink",fg="#00FFDA",width=10,height=2,command=pink)
    pink1.grid(pady=5,padx=5,row=0,column=10)

    brown1=Button(frame2,text="brown",font=("arial",7),bg="brown",fg="#00FFDA",width=10,height=2,command=brown)
    brown1.grid(pady=5,padx=5,row=0,column=12)

    gray1=Button(frame2,text="gray",font=("arial",7),bg="gray",fg="#00FFDA",width=10,height=2,command=gray)
    gray1.grid(pady=5,padx=5,row=2,column=0)

    green1=Button(frame2,text="green",font=("arial",7),bg="#22C55E",fg="white",width=10,height=2,command=green)
    green1.grid(pady=5,padx=5,row=2,column=2)

    eraser1=Button(frame2,text="eraser",font=("arial",7),bg="#E5E7EB",fg="black",width=10,height=2,command=eraser)
    eraser1.grid(pady=5,padx=5,row=2,column=4)

    clear1=Button(frame2,text="clear",font=("arial",7),bg="#EF4444",fg="white",width=10,height=2,command=clear)
    clear1.grid(pady=5,padx=5,row=2,column=6)

    small1=Button(frame2,text="small",font=("arial",7),bg="#F59E0B",fg="white",width=10,height=2,command=small)
    small1.grid(pady=5,padx=5,row=2,column=8)

    medium1=Button(frame2,text="medium",font=("arial",7),bg="#F59E0B",fg="white",width=10,height=2,command=medium)
    medium1.grid(pady=5,padx=5,row=2,column=10)

    big1=Button(frame2,text="big",font=("arial",7),bg="#F59E0B",fg="white",width=10,height=2,command=big)
    big1.grid(pady=5,padx=5,row=2,column=12)

    menu_button=Button(screen3,text="⋮",font=("Arial",18),bg="#3B82F6",fg="white",width=3,height=1,command=show_menu)    
    menu_button.place(x=550,y=10)

# --------------
# Menu
# --------------

    menu=Menu(screen3,tearoff=0)
    menu.add_command(label="Save", command=save)
    menu.add_command(label="Root", command=back)
    menu.add_command(label="Py",command=go_to_py)
    menu.add_command(label="RPS", command=go_to_rps)


    ca.bind("<Button-1>", start_draw)
    ca.bind("<B1-Motion>", draw)


    screen3.protocol("WM_DELETE_WINDOW",back)

# -----------------------
# rock,paper and scissor
# -----------------------

def Rps():
    root.withdraw()
    screen4=Toplevel(root)
    screen4.title("Rock,paper and scissors")
    screen4.geometry("600x600")
    screen4.configure(bg="#1E293B")

# ---------------
# functions
# ---------------
    def back_to_mainscreen():
        screen4.destroy()
        root.deiconify()

    def go_to_draw():
        screen4.destroy()
        draw()

    def go_to_PY1():
        screen4.destroy()
        pythons_Quiz()

    def show_menu1():
        menu1.post(520,50)       

    def rock():
        computer=random.choice(choices)

        if computer == "rock":
            result.config(text="Tie")

        elif computer == "scissors":
            result.config(text="You win")

        else:
            result.config(text="computer win")  

        label2.config(text=f"you : rock \n computer : {computer}")  

    def paper():
        computer=random.choice(choices)

        if computer == "paper":
            result.config(text="Tie")

        elif computer == "rock":
            result.config(text="You win")

        else:
            result.config(text="computer win")

        label2.config(text=f"you : paper \n computer : {computer}")     

    def scissor():
        computer=random.choice(choices)

        if computer == "scissors":
            result.config(text="Tie")

        elif computer == "paper":
            result.config(text="You win")

        else:
            result.config(text="computer win") 

        label2.config(text=f"you : scissor \n computer : {computer}")     

# ---------------
# choices
# ---------------

    choices=["rock","paper","scissors"]

# --------------
# Labels
# --------------

    result=Label(screen4,text="Choose",font=("algerian",20),bg="#1E293B",fg="white")
    result.pack(pady=30)

# --------------
# frame
# --------------

    frame2=Frame(screen4,bg="#334155")
    frame2.pack(pady=40)

# --------------
# button
# --------------

    rock1=Button(frame2,text="Rock",font=("Algerian",15),bg="#EF4444",fg="white",command=rock)
    rock1.grid(row=0,column=0,padx=10,pady=10)

    paper1=Button(frame2,text="Paper",font=("Algerian",15),bg="#EF4444",fg="white",command=paper)
    paper1.grid(row=0,column=2,padx=10,pady=10)

    scissor1=Button(frame2,text="scissor",font=("Algerian",15),bg="#EF4444",fg="white",command=scissor)
    scissor1.grid(row=0,column=4,padx=10,pady=10)

    menu_button1=Button(screen4,text="⋮",font=("Arial",18),bg="#3B82F6",fg="white",width=3,height=1,command=show_menu1)    
    menu_button1.place(x=550,y=10)
    
# ----------------
# label
# ----------------
    
    label2=Label(screen4,text="",font=("algerian",15),fg="white",bg="#1E293B")
    label2.pack(pady=15)

# ----------------
# Menu
# ----------------

    menu1=Menu(screen4,tearoff=0)
    menu1.add_command(label="Root", command=back_to_mainscreen)
    menu1.add_command(label="Py",command=go_to_PY1)
    menu1.add_command(label="Draw", command=go_to_draw)


    screen4.protocol("WM_DELETE_WINDOW",back_to_mainscreen)
# -----------------
# Titles
# -----------------

Title=Label(root,text="Welcome to the world of games",font=("Algerian",20),bg="#1E293B",fg="#FFFFFF")
Title.pack(pady=15)

# -----------------
# frame
# -----------------

frame1=Frame(root,bg="#D1c9c9")
frame1.pack(pady=20)

# --------------------------
# Button's and label's Frame
# --------------------------

py=Button(frame1,text="Python's Quiz",font=("Algerian",20),bg="#9E2626",fg="#000000",command=pythons_Quiz)
py.grid(row=0,column=0,padx=5,pady=10)

l1=Label(frame1,text="__________________________________________",fg="black",bg="#D1C9C9")
l1.grid(row=1,column=0,pady=10)

draw2=Button(frame1,text="Draw",font=("Algerian",20),bg="#9E2626",fg="#000000",command=draw)
draw2.grid(row=2,column=0,padx=5,pady=10)

l2=Label(frame1,text="__________________________________________",fg="black",bg="#D1C9C9")
l2.grid(row=3,column=0,pady=10)

rps=Button(frame1,text="Rock,paper and scissors",font=("Algerian",20),bg="#9E2626",fg="#000000",command=Rps)
rps.grid(row=4,column=0,padx=5,pady=15)

root.mainloop()