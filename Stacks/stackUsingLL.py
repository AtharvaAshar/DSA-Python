class ListNode:
    def __init__(self,x):
        self.value = x
        self.next=None 
class Stack:
    def __init__(self):
        self.__head = None 
        self.__count=0 

    def push(self,item):
        new_node = ListNode(item)
        new_node.next=self.__head
        self.__head = new_node
        self.__count += 1
    def pop(self):
        if self.isEmpty():
            print("empty Stack")
        else:
            data=self.__head.value
            self.__head=self.__head.next
            self.__count -= 1
            return data
    def top(self):
        if self.isEmpty():
            return print("Empty stack")
        else:
            return self.__head.value
    def isEmpty(self):
        if self.size() == 0:
            return True
        return False
    def size(self):
        return self.__count
    
s=Stack()
s.push(10)
s.push(12)
s.push(11)
print(s.top())
while s.isEmpty() is False:
    print(s.pop())