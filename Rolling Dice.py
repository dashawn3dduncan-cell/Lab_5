"""
Program Name: Rolling Dice
Name: Dashawn Duncan
Purpose: Write a program that simulates rolling two dice. 
Date: 2/13/2026
"""

import random

def roll_dice():
    print("--- Dice Rolling Terms ---")
    
    while True:
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        total = die1 + die2
        
        print(f"\nYou rolled: {die1} and {die2}")
        print(f"Total: {total}")
        
        if (die1 == 1 and die2 == 1):
            term = "Snake Eyes"
        elif (die1 == 1 and die2 == 2) or (die1 == 2 and die2 == 1):
            term = "Ace Caught a Deuce"
        elif (die1 == 2 and die2 == 2):
            term = "Little Joe from Kokomo"
        elif (die1 == 1 and die2 == 4) or (die1 == 4 and die2 == 1) or \
             (die1 == 2 and die2 == 3) or (die1 == 3 and die2 == 2):
            term = "Little Phoebe"
        elif (die1 == 3 and die2 == 3):
            term = "Jimmy Hicks from the Sticks"
        elif (die1 == 6 and die2 == 1) or (die1 == 1 and die2 == 6):
            term = "Six Ace"
        elif (die1 == 4 and die2 == 4): 
            term = "Eighter from Decatur"
        elif (die1 == 3 and die2 == 6) or (die1 == 6 and die2 == 3) or \
             (die1 == 4 and die2 == 5) or (die1 == 5 and die2 == 4):
            term = "Nina from Pasadena"
        elif (die1 == 5 and die2 == 5):
            term = "Puppy Paws"
        elif (die1 == 6 and die2 == 5) or (die1 == 5 and die2 == 6):
            term = "Six Five no Jive"
        elif (die1 == 6 and die2 == 6):
            term = "Boxcars"
        else:
            term = "Just a normal roll"

        print(f"Term: {term}")
        
        quit_choice = input("Press enter to roll again or 'q' to quit: ")
        if quit_choice.lower() == 'q':
            print("Goodbye!")
            break



