#!/usr/bin/env python
# coding: utf-8

# In[8]:



import random

rock = '''
    ***
    ROCK
    ***
'''

paper = '''
    ***
    PAPER
    ***
'''

scissors = '''
   ***
    SCISSORS
    ***
'''

game_images = [rock, paper, scissors]

user_selection = int(input("What number do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
print(game_images[user_selection])

computer_selection = random.randint(0, 2)
print("Computer selection:")
#print(game_images[computer_selection])

if user_selection >= 3 or user_selection < 0: 
  print("You typed an invalid number, you lose!") 
elif user_selection == 0 and computer_selection == 2:
  print("You win!")
elif computer_selection == 0 and user_selection == 2:
  print("You lose")
elif computer_selection > user_selection:
  print("You lose")
elif user_selection > computer_selection:
  print("You win!")
elif computer_selection == user_selection:
  print("It's a draw")


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




