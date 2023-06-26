from queue import Queue
q = Queue()

q.put('a')
q.put('b')
q.put('c')
q.put('d')
def reverseFirstK(q,k):
    stack=[]
    for i in range(k):
        stack.append(q.get())
    while len(stack)!=0:
        q.put(stack.pop())
    for i in range(q.qsize()-k):
        q.put(q.get())
    
reverseFirstK(q,2)
print(list(q.queue))