ix = 0 
fruit = input("name a fruit: ")
while ix < len(fruit):
 letter = fruit[ix]
 print(letter)
 ix += 1
prefixes = "JKLMNOPQ"
suffix = "ack" 
for p in prefixes: 
  print(p + suffix)