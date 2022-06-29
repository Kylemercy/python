#recursion
def russian_doll(doll):
  if doll == 1:
    print("All the dolls are opened")
    return
  
  else:
    russian_doll(doll-1)
    return None

russian_doll(1)
   
  
  
