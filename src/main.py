# creating a singly linked lists
class linked_list:

  def __init__(self, data, nextnode = None):
    self.data = data
    self.nextnode = nextnode
  

n1 = linked_list("fish")
n2 = linked_list("egg")
n3 = linked_list("bread")
n4 = linked_list("butter")
n1.nextnode = n2
n2.nextnode = n3
#adding a new item
n3.nextnode = n4
current_node = n1
while current_node:#or use while true
  print(current_node.data,end = " > ")
  if current_node.nextnode == None:
    print("None")
    break
  current_node = current_node.nextnode
#butter is then added to the list 