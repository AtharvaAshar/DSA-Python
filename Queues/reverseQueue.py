from queue import Queue
q=Queue()

q.put('a')
q.put('b')
q.put('c')
q.put('d')

def reverseQueue(q):
    if q.qsize()==0:
        return 
    fr=q.get()

    reverseQueue(q)
    q.put(fr)

reverseQueue(q)
print(list(q.queue))
