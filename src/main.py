import random
print("xxxxxxxxxxxxxxxxxxx")
print("Guessing Game!")
print("xxxxxxxxxxxxxxxxxxx")
print("Guess the secret number: it has two digits")
secret_num = str(random.randint(10,99))
remaining_try = 7
while remaining_try > 0:
  guess = (input("Guess the secret number: "))

  if secret_num == guess:
    print("Congratulations guessed the number correctly!")
    print("You Win\nGame over")
    break
  else:
    bull = 0
    cow = 0
    if secret_num[0] == guess[0]:
      bull+=1
    
    if secret_num[1] == guess[1]:
      bull += 1
    
    if secret_num[1] == guess[0]:
      cow += 1
    
    if secret_num[0] == guess[1]:
      cow += 1
    print("Bulls ",bull)
    print("Cows",cow)
    remaining_try -= 1
    if remaining_try <= 1:
       print("You lost the Game")
       print("the secret number is ",secret_num)
       break
     
    
    
        
    
  
