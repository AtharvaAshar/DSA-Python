class Queue:
    def __init__(self):
        self.__stack1=[]
        self.__stack2=[]
    
    def enqueue(self,item):
        self.__stack1.append(item)
    def dequeue(self):
        if self.size==0:
            return -1
        if self.size==1:
            return self.__stack1.pop()
        while len(self.__stack1)>1:
            self.__stack2.append(self.__stack1.pop())
        self.__stack1.pop()
        while(len(self.__stack2)>0):
            self.__stack1.append(self.__stack2.pop())
    def size(self):
        return len(self.__stack1)
    def getFront(self):
        return self.__stack1[0]
    def isEmpty(self):
        return self.size() == 0

q=Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.dequeue()
print(q.size())
print(q.isEmpty())
print(q.getFront())
