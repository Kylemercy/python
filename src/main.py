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
    print( total)
  def display(self):
    elem = []
    cur = self.head
    while cur.next != None:
      cur = cur.next
      elem.append(cur.data)
    print(elem)

n1= linked()
n1.display()
n1.append("egg")
n1.append("fish")
n1.append("bread")
n1.append("milk")
n1.display()
n1.length()
  
    
  

  

    
  
   
    
  
  

  
