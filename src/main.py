'''using another method of creating a singly
 linked lists'''
class linked:

  def __init__(self, value, nextnode = None):
    self.value = value
    self.nextnode = nextnode  
class single_list:
  def __init__(self, head = None):
    #this help keep track of the head of the list
    self.head = head
  
  def insert(self, value):
      node = linked(value)
      
      if self.head is None:
        self.head = node
        return
      current_node =  self.head
        # value i the element we want to insert
  
    # we create a node with the value we
#want to insert     
#here it checks if the node is none,if so the
#the value inserted becomes our head     
      while True:
        if current_node.nextnode is None:
          current_node.nextnode = node
          break
        current_node = current_node.nextnode
# this traverse through the list if incase
#when the node points to a none value we 
#are at the till then node is then inserted there
        
  def printlist(self):
     current_node = self.head
     while current_node is not None:
       print(current_node.value,end =  " > ")
       current_node = current_node.nextnode
     
     print("None")

ll = single_list()
ll.printlist()
ll.insert(8)
ll.printlist()
ll.insert(3)
ll.printlist()
