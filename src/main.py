#linked list
class node:
  def __init__(self,data = None):
    self.data = data
    self.next = None
class linked:
  def __init__(self):
    self.head = node()  
  def append(self,data):
    new_node = node(data)
    # calling the class node and assigning
   # it to a newnode
    cur_node = self.head
    while cur_node.next != None:
      cur_node = cur_node.next   
    cur_node.next = new_node
    # here we traverse the list till our curr_node
# becomes none meaning we are at the end of the
#list we then append our new node
  def length(self):
    cur_node = self.head
    total = 0
    while cur_node.next != None:
      cur_node = cur_node.next
      total += 1
    return ( total)
  def display(self):
    elem = []
    cur = self.head
    while cur.next != None:
      cur = cur.next
      elem.append(cur.data)
    print(elem)
  def get(self, index):
    if index >= self.length():
      print("Error 'Get ' index is out of range")
      return None
    cur_index = 0
    curr_node = self.head
    while True:
      curr_node = curr_node.next
      if cur_index == index:
        return curr_node.data
      
      cur_index += 1
  def erase(self,index):
    if index >= self.length():
      print("Error 'Get' index out of range")
      return# this returns all the items
      # after raising an error
    cur_indx = 0
    cur_node = self.head
    while True:
      last_node = cur_node
    
      cur_node = cur_node.next
      if cur_indx == index:
        
         last_node.next = cur_node.next
         return
      
      cur_indx += 1
  
n1= linked()
n1.display()
n1.append("egg")
n1.append("fish")
n1.append("bread")
n1.append("milk")
n1.display()
print( n1.length())
print(n1.get(2) ) 
n1.erase(2)
n1.display()
n1.erase(5)
n1.display()
  

    
  
   
    
  
  

  
