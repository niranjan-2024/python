class node:
   def __init__(self,item):
      self.item = item
      self.next = None
      
class Linked_list:
   def __init__(self):
      self.head = None
      
if __name__ == "__main__":
   ll = Linked_list()
   
   ll.head = node(1)
   second = node(2)
   third = node(3)
   fourth = node(4)
   fifth = node(5)
   sixth = node(6)
   seventh = node(7)
   eigth = node(8)
   ninth = node(9)
   tenth = node(10)
   
   ll.head.next = second
   second.next = third
   third.next = fourth
   fourth.next = fifth
   fifth.next = sixth
   sixth.next = seventh
   seventh.next = eigth
   eigth.next = ninth
   ninth.next = tenth
   
   while ll.head != None:
        print(ll.head.item, end=" ")
        ll.head = ll.head.next
