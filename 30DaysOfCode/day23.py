inp = [3,5,4,7,2,1]
T = 6

import sys
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

    # display = []
    
    # def levelOrder(self, root):
    #     self.breadthSearch(root)
    #     print ' '.join(str(i) for i in self.display)

    # def childernList(self, parentList):
    #     for i in parentList:
            

    # def breadthSearch(self, root):
    #     parentList = []
    #     childernList = []
    #     parentList.append(root)
    #     childernList = getChildernList(root)

    def levelOrder(self,root):
        ls = []
        ls.append(root)
        # print root.data
        for i in ls:
            if i.left != None:
                # print i.left.data
                ls.append(i.left)
            if i.right != None:
                # print i.right.data
                ls.append(i.right)
        print " ".join(str(node.data) for node in ls)

T=6
myTree=Solution()
root=None
for i in inp:
    data=i
    root=myTree.insert(root,data)
myTree.levelOrder(root)