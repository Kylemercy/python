import random
while True:
  user_action = input("Enter a choice:\nrock\npaper\nscissors.\n")
  possible_action = ["rock","paper","scissors"]
  comp_action = random.choice(possible_action)
  print(f"you choose {user_action} and computer choose {comp_action}")
  
  if user_action == comp_action:
    print(f"Both players selected {user_action}. it's a tie")
  
  elif user_action == "paper":
    if comp_action == "rock":
      print("you win.\n paper cover's rock")
    else:
      print("you lose.\n scissors cuts paper")
  
  elif user_action == "rock":
    if comp_action == "scissors":
      print("you win!\n rock smaches scissors.")
    
    else:
      print("you lose!\npaper covers rock")
 
  elif user_action == "scissors":
    if comp_action == "paper":
      print("you win!\n scissors cuts paper")
    
    else:
      print("you lose!\n rock smaches scissors")
  
  play_again = input("To play again enter: yes or no\n")
  if play_again.lower() != "yes":
    break
  
    
    
  
    
    
  
    
    
  