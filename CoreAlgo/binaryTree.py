# Implementing a Binary Tree Class

class BinaryTree:
    def __init__(self,rootObj):
        self.key = rootObj
        self.leftChild = None
        self.rightChild = None

    def insertLeft(self, newNode):
        if self.leftChild == None:
            self.leftChild = BinaryTree(newNode)
        else:
            temp = BinaryTree(newNode)
            temp.leftChild = self.leftChild
            self.leftChild = temp

    def insertRight(self, newNode):
        if self.rightChild == None:
            self.rightChild = BinaryTree(newNode)
        else:
            temp = BinaryTree(newNode)
            temp.rightChild = self.rightChild
            self.rightChild = temp
    
    def getRightChild(self):
        return self.rightChild

    def getLeftChild(self):
        return self.leftChild

    def setRootVal(self,obj):
        self.key = obj

    def getRootVal(self):
        return self.key

b = BinaryTree('apple')
print(b.getRootVal())
print(b.getLeftChild())
b.insertLeft('banana')
print(b.getLeftChild())
print(b.getLeftChild().getRootVal())
b.insertRight('cantaloupe')
print(b.getRightChild())
print(b.getRightChild().getRootVal())
b.getRightChild().setRootVal('hello')
print(b.getRightChild().getRootVal())

