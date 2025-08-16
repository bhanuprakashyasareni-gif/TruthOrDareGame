# ============================== IMPORTS =======================================
from tkinter import *
from PIL import Image ,ImageTk
import random
import pygame.mixer
import os

# ============================== GLOBAL SETUP ==================================
pygame.mixer.init()

# --- Colors ---
BG_COLOR       = "#2E0854"   # Deep purple
BUTTON_COLOR   = "#FF6B6B"   # Coral red
TEXT_COLOR     = "#FFFFFF"   # White
ACCENT_COLOR   = "#FFD700"   # Gold

# --- Paths ---
script_dir = os.path.dirname(os.path.abspath(__file__))
background_music_path = os.path.join(script_dir, "background_music.mp3")
click_sound_path      = os.path.join(script_dir, "computer-mouse-click-352734.mp3")

# --- Sound flags ---
SOUND_ENABLED = True
click_sound   = None

# ============================== LOAD CLICK SOUND ==============================
try:
    if os.path.exists(click_sound_path):
        click_sound = pygame.mixer.Sound(click_sound_path)
    else:
        print(f"Click sound file not found at: {click_sound_path}")
except Exception as e:
    print(f"Could not load sound effects: {e}")


# ================================ FUNCTIONS ===================================
def play_sound(sound):
    if SOUND_ENABLED and sound:
        try:
            sound.play()
        except Exception as e:
            print(f"Error playing sound: {e}")

def play_background_music():
    if SOUND_ENABLED and background_music_path and os.path.exists(background_music_path):
        try:
            pygame.mixer.music.load(background_music_path)
            pygame.mixer.music.play(-1)
        except Exception as e:
            print(f"Could not load or play background music: {e}")
    elif SOUND_ENABLED:
        print(f"Background music file not found: {background_music_path}")

button_style = {
    "bg": BUTTON_COLOR,
    "fg": TEXT_COLOR,
    "font": ("Arial", 14, "bold"),
    "borderwidth": 0,
    "relief": "flat",
    "padx": 20,
    "pady": 10,
    "activebackground": "#FF8E8E",
    "activeforeground": TEXT_COLOR
}

def fade_in(widget, duration=1000):
    start_color = BG_COLOR
    end_color   = ACCENT_COLOR
    steps       = 20
    delay       = duration // steps

    def hex_to_rgb(color):
        color = color.lstrip('#')
        return tuple(int(color[i:i+2], 16) for i in (0, 2, 4))

    start_rgb = hex_to_rgb(start_color)
    end_rgb   = hex_to_rgb(end_color)

    r_step = (end_rgb[0] - start_rgb[0]) / steps
    g_step = (end_rgb[1] - start_rgb[1]) / steps
    b_step = (end_rgb[2] - start_rgb[2]) / steps

    r, g, b = start_rgb

    def update(step):
        nonlocal r, g, b
        r += r_step; g += g_step; b += b_step
        current_color = f'#{int(max(0,min(255,r))):02x}{int(max(0,min(255,g))):02x}{int(max(0,min(255,b))):02x}'
        widget.config(fg=current_color)
        if step < steps:
            root.after(delay, update, step + 1)

    root.after(0, update, 0)


# ============================== TK INTERFACE SETUP ============================
root = Tk()
root.title("Truth Or Dare")
root.geometry("1000x500")
root.iconbitmap("favicon.ico")
root.configure(bg=BG_COLOR)

# ============================ SINGLE PLAYER MODE (RANDOM) =====================
def Truth_fun():
    play_sound(click_sound)
    with open("Truths.txt","r") as file:
        global y
        y = file.readlines()
        a = random.choice(y)
        label2.config(text=a)

def Dare_fun():
    play_sound(click_sound)
    with open("Dares.txt") as file :
        global r
        r = file.readlines()
        b = random.choice(r)
        label2.config(text=b)

def Done_fun():
    play_sound(click_sound)
    label2.config(text="")
    label1.config(text="")
    Start_game()

def Exit_fun():
    play_sound(click_sound)
    def Yes_fun():
        play_sound(click_sound)
        def submit(e,f):
            play_sound(click_sound)
            if str(e.get()) not in Y:
                with open("Truths.txt","a") as file :
                    file.write("\n"+e.get())
                    m = Label(root,text="Truth added successfully",fg="green",font=("Arial",15))
                    m.grid(row="10",column="0")
            with open("Dares.txt") as file :
                global r
                r = file.readlines()
                if str(f.get()) not in r :
                    with open("Dares.txt","a") as file :
                        file.write("\n"+f.get())
                        m = Label(root,text="Dare added successfully",fg="green",font=("Arial",15))
                        m.grid(row="11",column="0")

        label4 = Label(root,text="Enter your Truth ?",font=("Bold",15),fg="White",bg=BG_COLOR)
        e = Entry(root,font=("Arial",15))
        label5 = Label(root,text="Enter your Dare ?",font=("Bold",15),fg="White",bg=BG_COLOR)
        f = Entry(root,font=("Arial",15))
        button = Button(root,text="Submit",command=lambda:submit(e,f),**button_style)

        No_button.grid(row="9",column="1")
        Yes_button.config(state=DISABLED)
        label4.grid(row="5",column="0",pady=10)
        e.grid(row="6",column="0",pady=10)
        label5.grid(row="7",column="0",pady=10)
        f.grid(row="8",column="0",pady=10)
        button.grid(row="9",column="0",pady=10)

    def No_fun():
        play_sound(click_sound)
        root.quit()

    label1.config(text="")
    label2.config(text="")
    Truth_button.config(state=DISABLED)
    Dare_button.config(state=DISABLED)
    Done_button.config(state=DISABLED)
    Exit_button.config(state=DISABLED)

    global label3
    label3 = Label(root,text="If you want to add any truths or dares ?",font=("Bold",20),fg="White",bg=BG_COLOR)
    global Yes_button
    Yes_button = Button(root,text="Yes",command=Yes_fun,**button_style)
    global No_button
    No_button= Button(root,text="Exit",command=No_fun,**button_style)

    label3.grid(row="3", column="0")
    Yes_button.grid(row="4",column="1",padx=5)
    No_button.grid(row="4",column="3",padx=5)


# ============================ START RANDOM METHOD =============================
players  = []
variable = 0

def display_gif():
    try:
        img = Image.open("sand-clock.gif")
    except FileNotFoundError:
        print("Error: 'bottle.gif' not found.")
        return

    frames = []
    try:
        while True:
            frames.append(ImageTk.PhotoImage(img.copy()))
            img.seek(len(frames))
    except EOFError:
        pass

    gif_label = Label(root, width=400, height=400)
    gif_label.grid(row="0", column="2")

    def update(ind):
        frame = frames[ind]
        ind = (ind + 1) % len(frames)
        gif_label.configure(image=frame)
        gif_label.image = frame
        root.after(100, update, ind)

    def stop_gif():
        gif_label.destroy()
        x = random.choice(players)
        label1.config(text=f"{x.title()} Truth or Dare ?")
        label1.grid(row="0",column="2",pady=15)
        label2.grid(row="1",column="2",pady=10)
        Truth_button.grid(row="2",column="0",padx=5,pady=10)
        Dare_button.grid(row="2",column="1",padx=5,pady=10)
        Done_button.grid(row="2",column="3",padx=5,pady=10)
        Exit_button.grid(row="2",column="4",padx=5,pady=10)

    root.after(0, update, 0)
    root.after(10000, stop_gif)

def random_function():
    play_sound(click_sound)
    Random_button.destroy()
    Group_button.destroy()

    def add():
        play_sound(click_sound)
        x = name.get()
        players.append(x)
        name.delete(0,END)

    global Start_game
    def Start_game():
        play_sound(click_sound)
        if len(players) < 2 :
            l = Label(root,text="Two players are Required for this game.",fg="red")
            l.grid(row="5",column="5")
        else:
            name.destroy(); head1.destroy(); add.destroy(); startgame.destroy(); heading.destroy()
            global label1;   label1 = Label(root,text="",fg="White",bg=BG_COLOR,font=("Bold",30))
            global label2;   label2 = Label(root,text="",fg="White",bg=BG_COLOR,font=("Arial",20))
            global Truth_button; Truth_button = Button(root,text="Truth",command=Truth_fun,**button_style)
            global Dare_button; Dare_button  = Button(root,text="Dare",command=Dare_fun,**button_style)
            global Done_button; Done_button  = Button(root,text="Done",command=Done_fun,**button_style)
            global Exit_button; Exit_button  = Button(root,text="Exit", command=Exit_fun, **button_style)
            for btn in [Truth_button, Dare_button, Done_button, Exit_button]:
                btn.bind("<Enter>",on_enter)
                btn.bind("<Leave>",on_leave)
            display_gif()

    head1 = Label(root,text="Enter the player name : ",fg="White",font=("Bold",20),bg=BG_COLOR)
    name  = Entry(root,font=("Arial",20),relief="solid")
    add   = Button(root,text="add",command=add,**button_style)
    startgame = Button(root,text="Start Game",command=Start_game,**button_style)

    for btn in [add,startgame]:
        btn.bind("<Enter>",on_enter)
        btn.bind("<Leave>",on_leave)

    head1.grid(row="1",column="5",pady=10)
    name.grid(row="2",column="5",pady=10)
    add.grid(row="3",column="5",pady=10)
    startgame.grid(row="4",column="5",pady=10)


# ============================ GROUP METHOD ====================================
def gf():
    play_sound(click_sound)
    global variable
    if variable < len(players):
        labela.config(text=f"{players[variable]} Truth or Dare ? ")
    labela.grid(row="0",column="2")
    labelb.grid(row="1",column="2")
    Truth_but.grid(row="2",column="0",padx=5)
    Dare_but.grid(row="2",column="1",padx=5)
    Done_but.grid(row="2",column="3",padx=5)
    Exit_but.grid(row="2",column="4",padx=5)

def next_player_group():
    global variable
    variable += 1
    if variable >= len(players):
        variable = 0
    labelb.config(text="")
    gf()

def Truth_fun1():
    play_sound(click_sound)
    with open("Truths.txt","r") as file :
        global a
        a = file.readlines()
        z = random.choice(a)
        labelb.config(text=z)

def Dare_fun1():
    play_sound(click_sound)
    with open("Dares.txt") as file :
        global b
        b = file.readlines()
        y = random.choice(b)
        labelb.config(text=y)

def exit():
    play_sound(click_sound)
    def Yes_fun():
        play_sound(click_sound)
        def submit(e,f):
            play_sound(click_sound)
            if str(e.get()) not in Y:
                with open("Truths.txt","a") as file :
                    file.write("\n"+e.get())
                    m = Label(root,text="Truth added successfully",fg="green",font=("Arial",15))
                    m.grid(row="10",column="0")
            with open("Dares.txt") as file :
                global r
                r = file.readlines()
                if str(f.get()) not in r :
                    with open("Dares.txt","a") as file :
                        file.write("\n"+f.get())
                        m = Label(root,text="Dare added successfully",fg="green",font=("Arial",15))
                        m.grid(row="11",column="0")

        label4 = Label(root,text="Enter your Truth ?",font=("Arial",15),fg="White",bg=BG_COLOR)
        e = Entry(root,font=("Arial",15))
        label5 = Label(root,text="Enter your Dare ?",font=("Arial",15),fg="White",bg=BG_COLOR)
        f = Entry(root,font=("Arial",15))
        button = Button(root,text="Submit",command=lambda:submit(e,f),**button_style)

        Yes_button.config(state=DISABLED)
        label4.grid(row="5",column="0",pady=5)
        e.grid(row="6",column="0",pady=5)
        label5.grid(row="7",column="0",pady=5)
        f.grid(row="8",column="0",pady=5)
        button.grid(row="9",column="0",pady=5)
        No_button.grid(row="9",column="1",pady=5)

    def No_fun():
        play_sound(click_sound)
        root.quit()

    labela.config(text="")
    labelb.config(text="")
    Truth_but.config(state=DISABLED)
    Dare_but.config(state=DISABLED)
    Done_but.config(state=DISABLED)
    Exit_but.config(state=DISABLED)

    global label3
    label3 = Label(root,text="If you want to add any truths or dares ?",font=("Bold",20),fg="White",bg=BG_COLOR)
    global Yes_button
    Yes_button= Button(root,text="Yes",command=Yes_fun,**button_style)
    global No_button
    No_button= Button(root,text="Exit",command=No_fun,**button_style)

    label3.grid(row="3",column="0")
    Yes_button.grid(row="4",column="0")
    No_button.grid(row="4",column="1")

def group_function():
    play_sound(click_sound)
    Random_button.destroy()
    Group_button.destroy()

    def add():
        play_sound(click_sound)
        x = name.get()
        players.append(x)
        name.delete(0,END)

    global Start_game1
    def Start_game1():
        play_sound(click_sound)
        if len(players) < 2:
            l = Label(root,text="Two players are Required for this game.",fg="red")
            l.grid(row="5",column="5")
        else:
            name.destroy(); head1.destroy(); add.destroy(); startgame.destroy()
            global labela;   labela = Label(root,text="",fg="White",bg=BG_COLOR,font=("Bold",30))
            global labelb;   labelb = Label(root,text="",fg="White",bg=BG_COLOR,font=("Arial",20))
            global Truth_but; Truth_but= Button(root,text="Truth",command=Truth_fun1,**button_style)
            global Dare_but;  Dare_but = Button(root,text="Dare", command=Dare_fun1, **button_style)
            global Done_but;  Done_but = Button(root,text="Done", command=next_player_group, **button_style)
            global Exit_but;  Exit_but = Button(root,text="Exit", command=exit, **button_style)

            global variable
            variable = 0
            heading.destroy()
            for btn in [Truth_but, Dare_but, Done_but, Exit_but]:
                btn.bind("<Enter>",on_enter)
                btn.bind("<Leave>",on_leave)
            gf()

    head1 = Label(root,text="Enter the player name : ",fg="#E6E6FA",bg=BG_COLOR,font=("Bold",20))
    name  = Entry(root,font=("Arial",20),relief="solid")
    add   = Button(root,text="add",command=add,**button_style)
    startgame = Button(root,text="Start Game",command =Start_game1,**button_style)

    for btn in [add,startgame]:
        btn.bind("<Enter>",on_enter)
        btn.bind("<Leave>",on_leave)

    head1.grid(row="1",column="5",pady=10)

    name.grid(row="2",column="5",pady=10)
    add.grid(row="3",column="5",pady=10)
    startgame.grid(row="4",column="5",pady=10)

# ============================== HEADING + MAIN BUTTONS ========================
heading = Label(root,text="TRUTH OR DARE",fg=ACCENT_COLOR,bg=BG_COLOR,
                 font=("Impact",70,"bold"),pady=20)

Random_button = Button(root,text="Random Method",command=random_function,**button_style)
Group_button  = Button(root,text="Group Method", command=group_function,**button_style)

heading.grid(row="0",column="5",padx=360,pady=20)
fade_in(heading)
Random_button.grid(row="1",column="5",pady=10)
Group_button.grid(row="2",column="5",pady=10)

# ============================== BUTTON HOVER EFFECT ===========================
def on_enter(e):
    e.widget.config(bg="#FF8E8E", relief="raised")

def on_leave(e):
    e.widget.config(bg=BUTTON_COLOR, relief="flat")

for btn in [Random_button,Group_button]:
    btn.bind("<Enter>",on_enter)
    btn.bind("<Leave>",on_leave)

# ============================== START PROGRAM =================================
play_background_music()
root.mainloop()
