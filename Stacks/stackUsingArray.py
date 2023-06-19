class Stack:
    def __init__(self):
        self.__stack = []
    
    def push(self,item):
        self.__stack.append(item)
    def pop(self):
        if self.isEmpty():
            return print("Empty stack")
        else:
            return self.__stack.pop()
    def top(self):
        if self.isEmpty():
            return print("Empty stack")
        else:
            return self.__stack[-1]
    def isEmpty(self):
        if self.size() == 0:
            return True
        return False
    def size(self):
        return len(self.__stack)
    

s=Stack()
s.push(10)
s.push(12)
s.push(11)
print(s.top())
while s.isEmpty() is False:
    print(s.pop())
# print(s.top())