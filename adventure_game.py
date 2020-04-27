# Ayse Sapmaz
# 04.15.2020
# Adventure Game Project

import time
import random


def print_pause(sentence):
    print(sentence)
    time.sleep(0.5)

def valid_input(prompt, option1, option2):  # input validation
    while True:
        response = input(prompt)
        if option1 in response:
            break
        elif option2 in response:
            break
        else:
            print_pause("Sorry, I don't understand.")
    return response  

list=["Stegosaurus", "Triceratops", "Velociraptor", "Tyrannosaurus Rex", "Spinasaurus", "Pterenadon", "Plesiasauros"]
dinasours = random.choice(list)


def intro():
    print_pause("You find yourself in a dark dungeon.")
    print_pause("Rumor has it that a " + dinasours + " is somewhere around here, and has been terrifying the near by dungeon.")
    print_pause("In front of you, there are two passageways.")
    print_pause("Which way do you want to go?")


def first_way(item):
    print_pause("You chose the first door. ")
    print_pause("This is the way of " + dinasours + " house.")
    print_pause("The " + dinasours + " attacks you.")
    print_pause("You feel you are underprepared for a fight with only having a spoon.")
    response = valid_input("Would you like to (1) fight or (2) run away?\n", '1' , '2' )
    if response == '1':
       print_pause("You do your best.")
       print_pause("Your spoon against " + dinasours+"'s paws, no wayyyy....")
       print_pause("Your have been DEFEATED!!!")
       play_again()
    elif  response == '2' :
          print_pause("You run back into the dungeon luckily.\n"
          "You do not seem to have been followed.")  
          field(item)      


def second_way(item):
          print_pause("You chose the second door.")
          print_pause("This goes to a very small room.")
          print_pause("Your eye catches a glint of metal near the right side wall.")
          print_pause("You have found a  magical sword.")
          print_pause("You get rid of your silly spoon and take the sword with you.")
          print_pause("You walked back to the dungeon.")
          secondtimesecond(item) 



def field(item):
    while True:
          response = valid_input("Enter 1 to go on the first door.\n"
                 "Enter 2 to go on the second door.\n", '1' , '2' )
          if   response == '1' :
               first_way(item)
          elif response == '2':
               second_way(item)
    


def secondtimesecond(item):
    response = valid_input("Enter 1 to go on the first door.\n"
                 "Enter 2 to go on the second door.\n", '1' , '2' )
    if response == '1':
       print_pause("As the " + dinasours+ " start to attack, you unsheath your new sword....")
       print_pause("The " + dinasours + " takes one look at your shiny new sword and runs away.")
       print_pause("You get rid of the " + dinasours+". You are  VICTORIOUS!!!")
       play_again(item)
    elif response == '2': 
         print_pause("You chose the second door before and got the sword from the small room.")
         print_pause("You walk back to the dungeon")   
         field(item)       
                          
                              
def play_again(item):
    response = valid_input("Would you like to play again 'y' or 'n' \n", "y", "n" )
    if "n" in response:
           print_pause("Thanks for playing. See you again.")
    elif "y" in response:
             print_pause("Wonderful! Restarting the game")
             field(item)                                           
         


    
def adventure_game():
    item=[]
    intro()
    field(item)

if __name__ == "__main__":
     adventure_game()







# def choosePath(): # input validation second way
#   response = "" 
#   while response ! = "1" and response ! = "2":
#         print_pause("Sorry, I don't understand.")   
#         response = valid_input("Enter 1 to knock on the door of the house.\n"
#                  "Enter 2 to peer into the cave.\n", '1' , '2' )

#   return response  







