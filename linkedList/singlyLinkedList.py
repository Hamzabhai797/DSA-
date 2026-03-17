# class Node:
#   def __init__(self, info, next = None):
#     self.info = info
#     self.next = next

# class singlyLinkedList:
#   def __init__(self, head = None):
#     self.head = head

#   def insertAtEnd(self, value):
#     temp = Node(value)
#     if(self.head != None):
#         t1 = self.head
#         while(t1.next != None):
#             t1 = t1.next
#         t1.next = temp
#     else:
#         self.head = temp

#   def printLL(self):
#       t1 = self.head
#       while(t1.next != None):
#          print(t1.info)
#          t1 = t1.next
#       print(t1.info)
    
# sll = singlyLinkedList()
# sll.insertAtEnd(10)
# sll.insertAtEnd(20)
# sll.insertAtEnd(30)
# sll.printLL()

      # insertion at the beg
# class Node:
#   def __init__(self, info, next = None):
#     self.info = info
#     self.next = next

# class singlyLinkedList:
#   def __init__(self, head = None):
#     self.head = head

#   def insertAtEnd(self, value):
#     temp = Node(value)
#     if(self.head != None):
#         t1 = self.head
#         while(t1.next != None):
#             t1 = t1.next
#         t1.next = temp
#     else:
#         self.head = temp

#   def insertAtBeg(self, value):
#      temp = Node(value)
#      temp.next = self.head
#      self.head = temp


#   def printLL(self):
#       t1 = self.head
#       while(t1.next != None):
#          print(t1.info)
#          t1 = t1.next
#       print(t1.info)
    
# sll = singlyLinkedList()
# sll.insertAtEnd(10)
# sll.insertAtEnd(20)
# sll.insertAtEnd(30)
# sll.insertAtBeg(5)
# sll.printLL()


                # insertion at the middle
# class Node:
#   def __init__(self, info, next = None):
#     self.info = info
#     self.next = next

# class singlyLinkedList:
#   def __init__(self, head = None):
#     self.head = head

#   def insertAtEnd(self, value):
#     temp = Node(value)
#     if(self.head != None):
#         t1 = self.head
#         while(t1.next != None):
#             t1 = t1.next
#         t1.next = temp
#     else:
#         self.head = temp

#   def insertAtBeg(self, value):
#      temp = Node(value)
#      temp.next = self.head
#      self.head = temp


#   def insertAtMid(self, value, x):
#      temp = Node(value)
#      t1 = self.head
#      while(t1 != None):
#         if(t1.info == x):
#            temp.next = t1.next
#            t1.next = temp
#         t1 = t1.next

#   def printLL(self):
#       t1 = self.head
#       while(t1.next != None):
#          print(t1.info)
#          t1 = t1.next
#       print(t1.info)
    
# sll = singlyLinkedList()
# sll.insertAtEnd(10)
# sll.insertAtEnd(20)
# sll.insertAtEnd(30)
# sll.insertAtBeg(5)
# sll.insertAtMid(60, 20)    # 20 ke bad 60 aei ga
# sll.printLL()


      #  delete
class Node:
  def __init__(self, info, next = None):
    self.info = info
    self.next = next

class singlyLinkedList:
  def __init__(self, head = None):
    self.head = head

  def insertAtEnd(self, value):
    temp = Node(value)
    if(self.head != None):
        t1 = self.head
        while(t1.next != None):
            t1 = t1.next
        t1.next = temp
    else:
        self.head = temp

  def insertAtBeg(self, value):
     temp = Node(value)
     temp.next = self.head
     self.head = temp


  def insertAtMid(self, value, x):
     temp = Node(value)
     t1 = self.head
     while(t1 != None):
        if(t1.info == x):
           temp.next = t1.next
           t1.next = temp
        t1 = t1.next

  def printLL(self):
      t1 = self.head
      while(t1.next != None):
         print(t1.info)
         t1 = t1.next
      print(t1.info)
    
sll = singlyLinkedList()
sll.insertAtEnd(10)
sll.insertAtEnd(20)
sll.insertAtEnd(30)
sll.insertAtBeg(5)
sll.insertAtMid(60, 20)
sll.printLL()