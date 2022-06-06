#program for Rock,Paper, Scissors
from random import choice

#Available choices
options= ["R","P","S"]

print("This is a Rock, Paper, Scissors Game\n\n")
print("INSTRUCTION\n")
print("Enter R for Rock, P for Paper or S for Scissors\n")

#Game loop
while True:
    user_input = input("What will you choose? R/P/S or Q to Quit \n").upper().strip()
    if user_input == "Q":
        break
    if user_input not in options:
        print("Error! Invalid Selection!\n")
        continue

        #Randomize CPU choice
    computer_pick = choice(options)

    #chane cpu and user input from abbr. to full word
    if user_input == "R":
        user_input = "Rock"
    elif user_input == "P":
        user_input = "Paper"
    elif user_input == "S":
        user_input = "Scissors"

    if computer_pick == "R":
        computer_pick = "Rock"
    elif computer_pick == "P":
        computer_pick = "Paper"
    elif computer_pick == "S":
        computer_pick = "Scissors"

    print("Player(",user_input,")",":","CPU","(",computer_pick,")")

#Game Logic
    if user_input == ("Rock") and computer_pick == ("Scissors"):
        print ("Yay! You Won!\n")
        print ("The winner is Player\n")
        

    elif user_input == ("Paper") and computer_pick == ("Rock"):
        print ("Yay! You Won!\n")
        print ("The winner is Player\n")
        

    elif user_input == ("Scissors") and computer_pick == ("Paper"):
        print ("Yay! You Won!\n ")
        print ("The winner is Player\n")
        

    elif user_input == computer_pick:
        print ("It is a tie! \n")
        continue 


    else:
        print ("Noooo! You Lost! \n")
        print ("The winner is Computer\n")
    
    continuation=input("Game is over! Do you want to continue?Y/N\n").upper().strip()
    if continuation==("Y"):
        continue
    elif continuation==("N"):
        break
    else:
        print("Invalid Selection!")
        
print("Goodbye,Thank you for playing! ")
