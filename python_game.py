# Stacey A, Jason Lee

# Cool_Room - you will need to rename this function.
def Cool_room():

  # some prompts
  # '\n' is to print the line in a new line
    print("\nNow you entered the room of a monster!")
    print("The monster is sleeping.\nBehind it, there is another door. What would you do? (1 or 2)")
    print("1). Moonwalk your way through the door silently.")
    print("2). Kill the monster and flex your courage!")

  # get user input take input()
    answer = input(">")
    if answer =="1":
        print ("You live to see yourself once more.")
        Cool_room2()
    elif answer =="2":
        print("Suddenly, you feel a sharp pain in your skull. The huge red monster grabs you and lifts you up by your neck. You can't breath. You can see the world fading to black. You die from sudden skull pain.")
        game_over("")
        alive = False
    else:
        print("Suddenly, you feel a sharp pain in your leg and you look down to see that your leg is now possessed by an evil spirit. You attempt to kick at the spirit, but only succeed in kicking yourself in the face and falling to the floor.")
        game_over("You die of sudden leg pain.")
        alive = False

def Cool_room2():
  # some prompts
  # '\n' is to print the line in a new line
    print("\nNow you entered the room of the room. The room walls are covered by a forest of wires.")
    print("In the middle of the room a small metal object is on top of something else, you can't make out what it is. What would you do? (1 or 2)")
    print("1). Touch the metal object")
    print("2). Meditate")

  # get user input take input()
    answer = input(">")
    if answer =="1":
        print("You teleport to some room!")
        Cool_room3()
    elif answer =="2":
        print("Suddenly, you feel a sharp pain in your back, and then the smell of smoke fills your nostrils. You have been slain by the hands of carbon monoxide!")
        game_over("")
        alive = False
    else:
        game_over("Suddenly, you feel a sharp pain in your foot and you look down to see a little frog has leaped on to your foot, and given you a good bite in the big toe. But the pain is so sharp, and you die of sudden foot pain.")
        alive = False

def Cool_room3():
  # some prompts
  # '\n' is to print the line in a new line
    print("\nNow you entered the strange room of Count Grey, the one and only plot derailer! He gives you 2 choices:")
    print("1). Nuke the universe")
    print("2). Erase him")

  # get user input take input()
    answer = input(">")
   
    if answer == "1":
        print("You are not a hero. You are not a villian. You are an IDIOT.")
        game_over("You Died")
        alive = False
    elif answer =="2":
        print("After 30 minutes of hard work, you kill Count Gray twice, did some unspeakable things in his house, so even if he could come back to life the third time, he is too embarrassed to do so.")
        print("You are so happy that he is dead...")
        play_again()
    else:
        print("Suddenly, you feel a sharp pain in your ankle. You fall to the floor in agony and can't move.  It feels as if your ankle has been set alight and an axe has been hacked off it. You try to scream but are unable to and lapse into unconsciousness.")
        game_over("You die from sudden ankle pain.")
        alive = False

# function to ask play again or not
def play_again():
    print(" Do you want to play again? y/n")
  # get input
    answer = input(">").lower()
  # evaluate input using conditional 
    if answer == "y":
        alive = True
        start()
        
    else:
    # if user types anything besides "yes" or "y", exit() the program
        exit()

# game_over function accepts an argument called "reason"
def game_over(reason):
  # print the "reason" in a new line (\n)
    print("\n" + reason)
    print("Game Over!")
  # STRETCH: maybe ask player to play again or not. 
    play_again()


def start():

  # have some introductory text printed like: ("\nYou are standing in a dark room.")
    print("\nYou are standing in some room.")
    print("This room has an exit, what do you do? (1 or 2)")
    print("1). Exit.")
    print("2). Don't.")
    alive = True
  # get user input using input() and save 
    answer = input(">")

  # use a loop to manage game -- 
    while alive:
            
 # if x in input:
        if answer == "1":
    #go to a function()
            print("You live to breathe another moment.")
            Cool_room()
 # elif  in input:
        elif answer == "2":
            print("Suddenly, you feel a sharp pain in your chest. You die of sudden chest pain.")
            game_over("")
            alive = False
  # else:
    # else go to game over function because wrong input - game over
        else: 
            print("Suddenly, you feel a sharp pain in your back. You have died from sudden back pain.")
            game_over("You died.")

start()
# calling start function. 

#cr


