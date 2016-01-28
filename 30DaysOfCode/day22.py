T = 7
inp = [3,5,2,1,4,6,7]

class Node:
    def __init__(self,data):
        self.right=self.left=None
        self.data = data
class Solution:
    def insert(self,root,data):
        if root==None:
            return Node(data)
        else:
            if data<=root.data:
                cur=self.insert(root.left,data)
                root.left=cur
            else:
                cur=self.insert(root.right,data)
                root.right=cur
        return root

    def isItLeaf(self, node):
        if node.right == None and node.left == None:
            return True
        else:
            return False
    height = []
    def getHeight(self,root):
        self.depth(root)
        # print "max: " , max(self.height)
        return max(self.height)

    def depth(self, root, count=0):
        # print root.data
        count += 1
        if self.isItLeaf(root):
            # print "count:", count
            self.height .append(count)
        else:
            if root.right != None:
                self.depth(root.right, count)
            if root.left != None:
                self.depth(root.left, count)

myTree=Solution()

root=None

for i in inp:
    data=i
    root=myTree.insert(root,data)
height=myTree.getHeight(root)
print "height: ", height      

# print root.data