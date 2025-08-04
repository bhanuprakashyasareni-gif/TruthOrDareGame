#Truth or Dare 

print("\n","*"*20,"\n    Truth or Dare ","\n","*"*20,"\n")

players = []   #storing players here 
with open("My_frist_project(TOD)/Truths.txt","r") as file:  #reading truths from truths.txt file.
    y = file.readlines()
    k = set(y)
    y = list(k)

with open("My_frist_project(TOD)/Dares.txt","r") as file:  ##reading dares from dares.txt file.
    d = file.readlines()
    k = set(d)
    d = list(k)

x = True

#game start here 

while x:
    print()
    print("_"*50)
    print()

    #ASKING HOW MANY PLAYERS ARE PLAYING

    try:
        number_of_players = int(input("how many members are playing the game (min:2): "))
    except ValueError :
        
        number_of_players = int(input("Enter only number : "))
    
    #VALIDATING THE USER INPUT

    if number_of_players < 2 :
        print("The game minimum players are two ")
    else:
        print("1.Random \n2.Group can decide")
        try:
            choice = int(input("Enter your choice : "))
        except ValueError:
            choice = int(input("Enter only number : "))

        #PERFORMING THE OPERATION BY USER CHOICE

        match choice:
            
            #THE RONDOM METHOD STARTS HERE

            case 1 :
                
                #TAKING PLAYERS NAMES

                for i in range(number_of_players):
                    player_name = input(f"Enter player{i+1} name : ")
                    if player_name not in players :
                        players.append(player_name)
                    else:
                        print("This player name is allready entered.")
                        break
                
                #GIVEING INSTRUCTIONS ABOUT GAME

                print()
                print("Note:(T/D/E/P/D) is equal to (Truth,Dare,Exit,provide,done)")
                print()

                #STARTING THE RANDOM METHOD

                while x :
                    print()
                    print("-"*40)
                    print()
                    import time
                    print("bottle rotating.....😥")   #printing the bottle rotating
                    z = time.sleep(5)                 #the program resume after 5s
                    import random
                    o = random.choice(players)        #chossing random player from playes
                    l = input(f"{o} Truth or Dare?(T/D/E): ") #taking user input
                    match l :
                            case "T":
                                u = input(f"if you don't have i will provide (P,D): ")
                                if u == "P":
                                    try:
                                            x = y.pop(0)
                                            print(x)
                                    except FileNotFoundError :
                                        print("File not found .")
                                    except PermissionError:
                                        print("Permission Not given . ")
                                else:
                                    print("(Questions should be fun, personal, or revealing — but not harmful or inappropriate.\nIf the player refuses to answer, you can give a penalty or let them pick a Dare instead.)")
                            case "D":
                                u = input(f"if you don't have i will provide (P,D): ")
                                if u == "P":
                                    try:
                                            J = d.pop(0)
                                            print(J)
                                    except FileNotFoundError :
                                        print("File not found .")
                                    except PermissionError:
                                        print("Permission Not given . ")
                                else:
                                    print("(Dares should be safe, legal, and not force anyone to do something they are uncomfortable with.\nIf a player refuses, they might have to answer a Truth instead, or get a silly penalty.)")
                            case "E":
                                 c = input("If you want to any Truths or Dares (T/D/E) : ")
                                 if c == "T":
                                    x = input("Enter your Truth : ")
                                    if x in y :
                                        print("This truth is already in the data.")
                                    else:
                                        with open("Truths.txt","a") as file :
                                            file.write("\n"+x)  
                                 elif c == "D":
                                    x = input("Enter your Dare : ")
                                    if x in d :
                                        print("This dare is already in the data.")
                                    else:
                                        with open("Dares.txt","a") as file :
                                            file.write("\n"+x)
                                 elif c == "E":
                                    print("Thanks for playing Truth or dare game.")
                                 else:
                                    print("Enter these three vlaues only T or D or E . ")
                                 x = False
                                 break
                            case _ :
                                print("Enter these three vlaues only T or D or E . ")
            case 2 :
                for i in range(number_of_players):
                    player_name = input(f"Enter player{i+1} name : ")
                    if player_name not in players :
                        players.append(player_name)
                    else:
                        print("This player name is allready entered.")
                        break
                print()
                print("Note:(T/D/E/P/D) is equal to (Truth,Dare,Exit,provide,done)")
                print()
                while x :
                    print()
                    print("-"*40)
                    print()
                    for i in players:
                        x = input(f"{i} Truth or Dare?(T/D/E): ")
                        match x :
                            case "T":
                                u = input(f"if you don't have i will provide (P,D): ")
                                if u == "P":
                                    try:
                                            x = y.pop(0)
                                            print(x)   
                                    except FileNotFoundError :
                                        print("File not found .")
                                    except PermissionError:
                                        print("Permission Not given . ")
                                else:
                                    print("(Questions should be fun, personal, or revealing — but not harmful or inappropriate.\nIf the player refuses to answer, you can give a penalty or let them pick a Dare instead.)")
                            case "D":
                                u = input(f"if you don't have i will provide (P,D): ")
                                if u == "P":
                                    try:
                                            J = d.pop(0)
                                            print(J)
                                    except FileNotFoundError :
                                        print("File not found .")
                                    except PermissionError:
                                        print("Permission Not given . ")
                                else:
                                    print("(Dares should be safe, legal, and not force anyone to do something they are uncomfortable with.\nIf a player refuses, they might have to answer a Truth instead, or get a silly penalty.)")
                            case "E":
                                
                                c = input("If you want to any Truths or Dares (T/D/E) : ")
                                if c == "T":
                                    x = input("Enter your Truth : ")
                                    if x in y :
                                        print("This truth is already in the data.")
                                    else:
                                        with open("Truths.txt","a") as file :
                                            file.write("\n"+x)  
                                elif c == "D":
                                    x = input("Enter your Dare : ")
                                    if x in d :
                                        print("This dare is already in the data.")
                                    else:
                                        with open("Dares.txt","a") as file :
                                            file.write("\n"+x)
                                elif c == "E":
                                    print("Thanks for playing Truth or dare game.")
                                else:
                                    print("Enter these three vlaues only T or D or E . ")
                                x = False
                                
                                break
                            case _ :
                                print("Enter these three vlaues only T or D or E . ")         
            case _ :
                print("please select from above options only . ")
        
    