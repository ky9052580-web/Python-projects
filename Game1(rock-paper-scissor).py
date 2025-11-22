# Rock Paper Scissor Game
import os
import random
print("".center(40,'-'))
print("Rock/Paper/Scissor Game".center(40,))
print("".center(40,'-'))

print("Let's start the game")
name = input("UserName : ")
print("Select one : ('Rock','Paper','Scissor')")

choices = ['Rock','Paper','Scissor']

ans = int(input("How many matches do you want to play?"))
i =  1
your_score = 0
computer_score = 0
end = 1
while(i <=  ans): 
    print(f"Match -> {i}:")
    your_choice = input("Enter your choice : ".title())
    computer_choice = random.choice(["Rock","Paper","Scissor"])
    print(f"Computer choice : {computer_choice}")
    print("".center(40,'-'))
    if your_choice == computer_choice:
        print("It is a tie.")
        
    elif (your_choice == 'Rock' and computer_choice == 'Scissor'):
        print("You win.")
        your_score = your_score+1    
            
    elif (your_choice == 'Scissor' and computer_choice == 'Paper'):
        print("You win.")
        your_score = your_score+1
        
    elif (your_choice == 'Paper' and computer_choice == 'Rock'):
        print("You win.")
        your_score = your_score+1
        
    else:
        print("Computer wins.")
        computer_score = computer_score+1

    print(f"Scores are : \n {name} Score : {your_score} \n Computer Score : {computer_score}")
    print("".center(40,'-'))
    i = i + 1

if computer_score > your_score:
    print(f"\nComputer Wins by : {computer_score - your_score}\n")
elif your_score > computer_score:
    print(f"\n{name} Wins by : {your_score - computer_score}\n")
else:
    print("\nIt is a Tie.\n")

os.system("cls")



    