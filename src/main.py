def tower(n,start, end, middle):
  #tower of Hanoi using recursion
  if n == 1:
    print(f"move {n},from tower {start} to tower {end}")
  
  else:
    tower(n-1,start,middle,end)
    # move from start to end using middle
    print(f"move {n},from tower {start} to tower {end}")
    tower(n-1, middle, end, start)
tower(4,"A","C","B")