class Queue:
    def __init__(self):
        self.__queue = []
        self.__front=0
        self.__count=0
    
    def enqueue(self,item):
        self.__queue.append(item)
        self.__count+=1
    
    def dequeue(self):
        if self.__count==0:
             return "Empty queue"
        elem=self.__queue[self.__front]
        self.__front+=1
        self.__count-=1
        return elem
    def getFront(self):
        if self.__count == 0:
            return "Empty queue"
        return self.__queue[self.__front]
    def size(self):
            return self.__count
    def isEmpty(self):
         return self.size() == 0
    
        
q=Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.dequeue()
print(q.getFront())
print(q.size())
print(q.isEmpty())

