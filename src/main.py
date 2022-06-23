class Node:
  def __init__(self,data = None,next= None):
    self.data = data
    self.next = next
  
class Linked:
  def __init__(self):
    self.head = None
    
  
  def insert_begining(self,data):
    new_node = Node(data, self.head)
    self.head = new_node
 
  def print(self):
    if self.head is None:
        print("list is empty")
        return
    itr = self.head
    str_itr = ' '
    while itr:
      str_itr += str(itr.data) + ' >> '
      itr = itr.next
    print(str_itr)
  def insert_end(self,data):
    if self.head is None:
      self.head = Node(data,None)
      return
 # this checks if the lsit is empty,if so
# the new node becomes the head,and the next,node
# is node    
    itr = self.head
    while itr.next:
      itr = itr.next
# incase where the list is not empty,it iterates
# until the next node is none then append the new
# node at none
    itr.next = Node(data,None)
    # the new node(data) is added and the nxt node 
    # become none
  
  def get_length(self):
    itr = self.head
    count = 0
    while itr:
      count += 1
      itr = itr.next
    return count
  def remove(self,index):
    if index< 0 or index >= self.get_length():
      print(" invalid index ")
      return
    
    if index == 0:
      self.head = self.head.next
      return
    count = 0
    itr = self.head
    while itr:
      if count == index - 1:   
# this stops at the previous index of the element
# of the element we want to remove
        itr.next = itr.next.next
        break
        # here the element we went to remove now
# links the previous element we its next element
    
      itr.next 
      count += 1
  def insert_data_at(self,index,data):
      if index< 0 or index >= self.get_length():
        print(" invalid index ")
        return
      if index == 0:
        self.insert_begining(data)
        return
      count = 0
      cur = self.head
      while cur:
        if count == index -1:
          new_node = Node(data,cur.next)
       #note index - 1,means previous node
          cur.next = new_node
          break
        
        cur.next
  
      count += 1
   
  def insert_value(self,data_list):
     self.head = None
     for data in data_list:
       self.insert_end(data)
         
    
  
  def insert_value_after(self,data_after,data_insert):
     if self.head is None:
       return
     if self.head.data == data_after:
       self.head.next = Node( data_insert,self.head.next)
       return
     
     itr = self.head
     while itr:
       if itr.data == data_after:
         itr.next = Node(data_insert,itr.next)
         break
       itr = itr.next
  def remove_value(self,data):
    if self.head == None:
      return
    if self.head.data == data:
      self.head = self.head.next
      return
    
    itr = self.head
    while itr.next:
      if itr.next.data == data:
        itr.next = itr.next.next
        break
      itr = itr.next
      
    
    
    
  
   
  
if __name__ == '__main__':
  

  ll = Linked()
  ll.insert_value(["banana","mango","grapes","orange"])
  ll.print()
  print("\n")
  ll.insert_begining("fish")
  ll.insert_end("potato")
  ll.insert_data_at(1,"grape")
  ll.insert_value_after("mango","apple")
  ll.remove_value("grapes")
  ll.print()
  print("length:",ll.get_length())
  
  
  
  
 

 

  

 
  
