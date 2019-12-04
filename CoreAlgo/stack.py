# This is a Stack in Python

class Stack:

    def __init__(self):
        self.items = []
    
    def isEmpty(self):
        return self.items == []
    
    def push(self,item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()
    
    def peek(self):
        # should show the last item in the stack
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)

s = Stack()
s.push('cat')
s.push('zebra')
s.push('dog')
s.push('Elmo')
s.push('rat')
s.peek()
s.size()
s.pop()
s.size()
#should return False
s.isEmpty()
