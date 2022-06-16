
# Python code to demonstrate the application of
# zip()
 
# initializing list of players.

players = ["Sachin", "Sehwag", "Gambhir", "Dravid", "Raina"]
 
# initializing their scores

scores = [100, 15, 17, 28, 43]
 
# printing players and scores.

for pl, sc in zip(players, scores):
  print(f"player: {pl}, scores : {sc}")
