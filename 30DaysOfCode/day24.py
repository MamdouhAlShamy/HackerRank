# inp = [1,1,1,1,2, 2]
inp = [1,2,2,3,3,4]


class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class Solution:
    def insert(self,head,data):
        p = Node(data)        
        if head==None:
            head=p
        elif head.next==None:
            head.next=p
        else:
            start=head
            while(start.next!=None):
                 start=start.next
            start.next=p
        return head 

    def display(self,head):
        current = head
        while current:
            print current.data,
            current = current.next	


    def removeDuplicates(self,head):
        # if head.data == 
        prevNode = None
        current = head
        ls = []
        while current:
            # print head.data
            if current.data in ls:
                # print "removing"
                # self.removeNode(current, prevNode)
                prevNode.next = current.next
                current = current.next
            else:
                ls.append(current.data)
                prevNode = current
                current = current.next
        return head

        
        
mylist= Solution()
T = 6

head=None
for i in inp:
    head=mylist.insert(head,i)   
# mylist.display(head)
head=mylist.removeDuplicates(head)
mylist.display(head)