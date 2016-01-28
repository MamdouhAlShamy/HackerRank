class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class Solution:
    def display(self,head):
        current = head
        while current:
            print current.data,
            current = current.next
    def insert(self,head,data):
        if not isinstance(head, Node):
            n = Node(data)
            return n
        else:
            current = head
            while True:
                if current.next == None:
                    break
                else:
                    current = current.next
            n = Node(data)
            current.next = n
            return head


mylist= Solution()
T = 4
inp = [2, 3, 4, 1]
head=None
for i in range(T):
    data=inp[i]
    head=mylist.insert(head, data)    
mylist.display(head);