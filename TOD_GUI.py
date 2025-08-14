from tkinter import *
from PIL import Image ,ImageTk
import random

#creating the window
root = Tk()

#adding title to the window
root.title("Truth Or Dare")

#width and heght of the window before full screen
root.geometry("500x500")

#adding icon to the window
root.iconbitmap(r"c:\Users\Bhanu\Downloads\favicon.ico")

#creating the function that calls when click the truth button(in random method)
def Truth_fun():
    
    #reading Truths from Truths.txt file 
    with open("Truths.txt","r") as file :
        global y
        y = file.readlines()

        a = random.choice(y)  
        label2.config(text=a) 


#creating the function that calls when click the Dares button(in random method)
def Dare_fun():
    
    #reading Dare from Dares.txt file
    with open("Dares.txt") as file :

        global r
        r = file.readlines()

        b = random.choice(r)
        label2.config(text=b)
    

#creating the function that calls when click the Done button (in random method)
def Done_fun():
    label2.config(text="")
    label1.config(text="")
    Start_game()


#creating the funtcion that calls when click the Exit button (in random method)
def Exit_fun():
    
    #this funtion add to truths or dares
    def Yes_fun():
    
     def submit(e,f):

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


     #creating widgets when click on yes button inside exit 
     label4 = Label(root,text="Enter your Truth ? .",font=("Arial",15))
     e = Entry(root,font=("Arial",15))
     label5 = Label(root,text="Enter your Dare ? . ",font=("Arial",15))
     f = Entry(root,font=("Arial",15))
     button = Button(root,text="Submit",command=lambda:submit(e,f),fg="white",bg="red",relief="solid")
     No_button.grid(row="9",column="1")
     
     #adding to the screen 
     Yes_button.config(state=DISABLED)
     label4.grid(row="5",column="0",pady=10)
     e.grid(row="6",column="0",pady=10)
     label5.grid(row="7",column="0",pady=10)
     f.grid(row="8",column="0",pady=10)
     button.grid(row="9",column="0",pady=10)
    
    #This funtion direct exits the program
    def No_fun():
      root.quit()
    
    #diableing the all buttons
    label1.config(text="")
    label2.config(text="")
    Truth_button.config(state=DISABLED)
    Dare_button.config(state=DISABLED)
    Done_button.config(state=DISABLED)
    Exit_button.config(state=DISABLED)
    
    #creting widgets for when click the exit button
    global label3
    label3 = Label(root,text="If you want to add any truths or dares ?",font=("Arial",20))
    global Yes_button
    Yes_button = Button(root,text="Yes",command=Yes_fun,fg="white",bg="green",padx=15,pady=15,font=("Arial",10))
    global No_button
    No_button= Button(root,text="Exit",command=No_fun,fg="white",bg="red",padx=15,pady=15,font=("Arial",10))
    
    #adding to the window
    label3.grid(row="3",column="0")
    Yes_button.grid(row="4",column="1",padx=5)
    No_button.grid(row="4",column="3",padx=5)


players = []   #storing players name here
variable = 0   #variable for group method

#This funtion displays the sand-colock gif time when game was started 
def display_gif():
    """Displays a GIF for a set duration without blocking the main loop."""
    try:
        img = Image.open("sand-clock.gif")
    except FileNotFoundError:
        print("Error: 'bottle.gif' not found. Please ensure the GIF is in the correct path.")
        return

    frames = []
    try:
        while True:
            frames.append(ImageTk.PhotoImage(img.copy()))
            img.seek(len(frames))  # Move to the next frame
    except EOFError:
        pass  # End of sequence

    if not frames:
        print("Error: Could not load frames from GIF.")
        return

    gif_label = Label(root, width=400, height=400)
    gif_label.grid(row="1", column="1")

    def update(ind):
        """Updates the GIF frame."""
        frame = frames[ind]
        ind = (ind + 1) % len(frames)
        gif_label.configure(image=frame)
        gif_label.image = frame  # Keep a reference to avoid garbage collection
        root.after(100, update, ind)

    def stop_gif():
        """Stops the GIF and destroys the label."""
        gif_label.destroy()
        
        #choosing the rondom players from players
        x = random.choice(players)
        label1.config(text=f"{x.title()} Truth or Dare ?")

        #Adding game controll buttons here
        label1.grid(row="0",column="0",pady=15)
        label2.grid(row="1",column="0",pady=10)
        Truth_button.grid(row="2",column="1",padx=5,pady=10)
        Dare_button.grid(row="2",column="2",padx=5,pady=10)
        Done_button.grid(row="2",column="3",padx=5,pady=10)
        Exit_button.grid(row="2",column="4",padx=5,pady=10)


    root.after(0, update, 0)
    root.after(10000, stop_gif)  # Destroy the label after 10 seconds (10000 ms)
    

#This function is calls when click the random method in the main window 
def random_function():
    
    #removing two buttons
    Random_button.destroy()
    Group_button.destroy()
    
    #adding players names
    def add():
        x = name.get()
        players.append(x)
        name.delete(0,END)
        print(players)

    #game function start here
    global Start_game
    def Start_game():

        #checking the players minimum two members or not
        if len(players) < 2 :
            l = Label(root,text="Two players are Required for this game.",fg="red")
            l.grid(row="5",column="5")
        
        else:
          
          #removing the buttons
          name.destroy()
          head1.destroy()
          add.destroy()
          startgame.destroy()
          heading.destroy()
          
          #creating widgets 
          global label1
          label1 = Label(root,text="",fg="Red",bg="Yellow",font=("Arial",30))
          global label2
          label2 = Label(root,text="",fg="Blue",bg="Yellow",font=("Arial",20))
          global Truth_button
          Truth_button = Button(root,text="Truth",command=Truth_fun,fg="White",bg="blue",font=("Arial",15),padx=10,pady=10)
          global Dare_button
          Dare_button = Button(root,text="Dare",command=Dare_fun,fg="White",bg="blue",font=("Arial",15),padx=10,pady=10)
          global Done_button
          Done_button = Button(root,text="Done",command=Done_fun,fg="White",bg="blue",font=("Arial",15),padx=10,pady=10)
          global Exit_button
          Exit_button = Button(root,text="Exit",command=Exit_fun,fg="White",bg="red",font=("Arial",15),padx=10,pady=10)
          
          #calling the display_gif function
          display_gif()
        
   
    #adding players here
    head1 = Label(root,text="Enter the player name : ",fg="Black",font=("Arial",20))
    name = Entry(root,font=("Arial",20),relief="solid")
    add = Button(root,text="add",command=add,fg="White",bg="blue",padx=15,pady=15,font=("Arial",20))
    startgame= Button(root,text="Start Game",command=Start_game,fg="White",bg="Green",padx=20,pady=20,font=("Arial",20))

    
    #adding widgets to the screen
    head1.grid(row="1",column="5",pady=10)
    name.grid(row="2",column="5",pady=10)
    add.grid(row="3",column="5",pady=10)
    startgame.grid(row="4",column="5",pady=10)
         

#this function main funtion in group method
def gf():
    global variable
    if variable < len(players):
        labela.config(text=f"{players[variable]} Truth or Dare ? ")
    else:
        # This part will now be handled by next_player_group
        pass
    
    #adding buttons to the window
    labela.grid(row="0",column="0")
    labelb.grid(row="1",column="0")
    Truth_but.grid(row="2",column="1")
    Dare_but.grid(row="2",column="2")
    Done_but.grid(row="2",column="3")
    Exit_but.grid(row="2",column="4")

def next_player_group():
    """Cycles to the next player in the group."""
    global variable
    variable += 1
    if variable >= len(players):
        variable = 0  # Go back to the first player
    
    # Clear the previous truth/dare text
    labelb.config(text="")
    
    # Update the label for the new player
    gf()

#This function is called when truth clicked
def Truth_fun1():
    
    #read the truths from truths.txt
    with open("Truths.txt","r") as file :
        global a
        a = file.readlines()

        z = random.choice(a)
        labelb.config(text=z)

#This function is called when dare clicked
def Dare_fun1():
    
    #read the Dare from dares.txt
    with open("Dares.txt") as file :

        global b
        b = file.readlines()

        y = random.choice(b)
        labelb.config(text=y)


#this  function called when exit button clicked
def exit():
    
    #yes button function
    def Yes_fun():
    
     def submit(e,f):

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


     label4 = Label(root,text="Enter your Truth ? .",font=("Arial",15))
     e = Entry(root,font=("Arial",15))
     label5 = Label(root,text="Enter your Dare ? . ",font=("Arial",15))
     f = Entry(root,font=("Arial",15))
     button = Button(root,text="Submit",command=lambda:submit(e,f),fg="white",bg="red",relief="solid")

     Yes_button.config(state=DISABLED)
     label4.grid(row="5",column="0")
     e.grid(row="6",column="0")
     label5.grid(row="7",column="0")
     f.grid(row="8",column="0")
     button.grid(row="9",column="0")
     No_button.grid(row="9",column="1")
    
    #no button function
    def No_fun():
      root.quit()

    #disableing the all buttons
    labela.config(text="")
    labelb.config(text="")
    Truth_but.config(state=DISABLED)
    Dare_but.config(state=DISABLED)
    Done_but.config(state=DISABLED)
    Exit_but.config(state=DISABLED)

    #creating the buttons
    global label3
    label3 = Label(root,text="If you want to add any truths or dares ?",font=("Arial",20))
    global Yes_button
    Yes_button = Button(root,text="Yes",command=Yes_fun,fg="white",bg="green",padx=15,pady=15,font=("Arial",10))
    global No_button
    No_button= Button(root,text="Exit",command=No_fun,fg="white",bg="Red",padx=15,pady=15,font=("Arial",10))
    
    #adding the buttons
    label3.grid(row="3",column="0")
    Yes_button.grid(row="4",column="0")
    No_button.grid(row="4",column="1")


#this funtion is called when the clicked to the group method
def group_function():

    #removing buttons
    Random_button.destroy()
    Group_button.destroy()
    
    #adding players names
    def add():
        x = name.get()
        players.append(x)
        name.delete(0,END)
        print(players)
    
    #game starts here
    global Start_game1
    def Start_game1():

        if len(players) < 2 :
            l = Label(root,text="Two players are Required for this game.",fg="red")
            l.grid(row="5",column="5")

        else:
            
          name.destroy()
          head1.destroy()
          add.destroy()
          startgame.destroy()
          
          
          #creating controls to the window
          global labela
          labela = Label(root,text="",fg="Red",bg="Yellow",font=("Arial",30))
          global labelb
          labelb = Label(root,text="",fg="Blue",bg="Yellow",font=("Arial",20))
          global Truth_but
          Truth_but = Button(root,text="Truth",command=Truth_fun1,fg="White",bg="blue",font=("Arial",15),padx=10,pady=10)
          global Dare_but
          Dare_but = Button(root,text="Dare",command=Dare_fun1,fg="White",bg="blue",font=("Arial",15),padx=10,pady=10)
          global Done_but
          Done_but = Button(root,text="Done",command=next_player_group,fg="White",bg="blue",font=("Arial",15),padx=10,pady=10)
          global Exit_but
          Exit_but = Button(root,text="Exit",command=exit,fg="White",bg="red",font=("Arial",15),padx=10,pady=10)

          global variable
          variable = 0
          heading.destroy()
          gf()


    #adding players here
    head1 = Label(root,text="Enter the player name : ",fg="Black",font=("Arial",20))
    name = Entry(root,font=("Arial",20),relief="solid")
    add = Button(root,text="add",command=add,fg="White",bg="blue",padx=15,pady=15,font=("Arial",20))
    startgame= Button(root,text="Start Game",command =Start_game1,fg="White",bg="Green",padx=20,pady=20,font=("Arial",20))

    
    #adding widgets to the screen
    head1.grid(row="1",column="5",pady=10)
    name.grid(row="2",column="5",pady=10)
    add.grid(row="3",column="5",pady=10)
    startgame.grid(row="4",column="5",pady=10)


#Adding the heading
heading = Label(root,text="Truth Or Dare",fg="White",bg="green",relief="solid",borderwidth=5,padx=20,pady=20,font=("Bold",75))

#creating two buttons
Random_button =Button(root,text="Random Method",font=("Arial",25),bg="Yellow" ,command=random_function)
Group_button = Button(root,text="Group Method",font=("Arial",25),bg="Yellow",padx=15,command=group_function)

#Adding widgets to the root
heading.grid(row="0",column="5",padx=300,pady=20)
Random_button.grid(row="1",column="5",pady=10)
Group_button.grid(row="2",column="5",pady=10)

root.mainloop()