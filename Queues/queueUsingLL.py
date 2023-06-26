class ListNode:
    def __init__(self,x):
        self.value = x
        self.next=None 

class Queue:
    def __init__(self):
        self.__head=None
        self.__count=0
        self.__tail=None
    def enqueue(self,item):
        new_node = ListNode(item)
        if self.__head is None:
            self.__head = new_node
            self.__tail = new_node
            self.__count+=1
        else:
            self.__tail.next=new_node
            self.__count+=1
            self.__tail=self.__tail.next
    
    def dequeue(self):
        if self.__head is None:
            return -1
        elem=self.__head.value
        self.__head=self.__head.next
        self.__count-=1
        return elem
    def size(self):
        return self.__count
    def isEmpty(self):
        return self.size() == 0
    def getFront(self):
        if self.__head is None:
            return -1
        return self.__head.value

q=Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
while q.isEmpty() is False:
    print(q.getFront())
    q.dequeue()
print(q.size())

        


