fruits = ["apples","oranges","bananas","melons"]
prices = [20,10,5,15]
quantities = [5,7,3,4]

for fruit, price, quantity in zip(fruits,prices,quantities):
  print(f"You bought {quantity} {fruit} for ${price*quantity}")
  