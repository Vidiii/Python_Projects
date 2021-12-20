import random
#from random import randint
def play_game():
  if(comp == user):
    return None
  elif(user=="r"):
    if(comp=="s"):
      return True
    elif(comp=="p"):
      return False
  elif(user=="p"):
    if(comp=="s"):
      return False
    elif(comp=="r"):
      return True
  elif(user=="s"):
    if(comp=="p"):
      return True
    elif(comp=="r"):
      return False

print("                    Welcome to the ROCK PAPER SCISSOR game.  ")
print("Rules for a fair play: ")
print("rock - paper ---> PAPER winner\nrock - scissor ---> ROCK winner\npaper - scissor ---> SCISSOR winner")
print("   type r -> rock\n   type s -> scissor \n   type p -> paper")
print("\nLets begin !!")

play=True
while(play):
  user = input("Enter your choice: \n")
  comp_values = ['r','s','p']
  comp = random.choice(comp_values)
  result=play_game()
  if(user=="r"):
    user="rock"
  elif(user=="p"):
    user="paper"
  elif(user=="s"):
    user="scissor"
    
  if(comp=="r"):
    comp="rock"
  elif(comp=="p"):
    comp="paper"
  elif(comp=="s"):
    comp="scissor"
  print("You: ", user)
  print("Computer: ",comp)  
  if(result==None):
    print("Its a TIE.")
  elif(result==True):
    print("You WIN.")
  else:
    print("You LOSE.")
  ch=input("Press 'y' to continue playing else press 'n'.\n")
  if(ch=='n'):
    print("Thank you for playing.")
    play=False