class MapNode:
    def __init__(self,key,value):
        self.key = key
        self.value = value
        self.next=None


class Map:
    def __init__(self):
        self.bucketSize=10
        self.buckets=[None for _ in range(self.bucketSize)]
        self.count=0
    def size(self):
        return self.count
    def rehash(self):
        temp=self.buckets
        self.buckets=[None for _ in range(2*self.bucketSize)]
        self.bucketSize*=2
        self.count=0
        for head in temp:
            while head is not None:
                self.insert(head.key,head.value)
                head=head.next
    def insert(self, key, value):
        hc=abs(hash(key))
        i=hc%self.bucketSize
        head=self.buckets[i]
        while head is not None:
            if head.key==key:
                head.value=value
                return
            head=head.next
        head=self.buckets[i]
        newNode=MapNode(key,value)
        newNode.next=head
        self.buckets[i]=newNode
        self.count+=1
        loadFactor=self.count/self.bucketSize
        if loadFactor>=0.7:
            self.rehash()
    def getValue(self,key):
        hc=abs(hash(key))
        i=hc%self.bucketSize
        head=self.buckets[i]
        while head is not None:
            if head.key==key:
                return head.value
            head=head.next
        return None
    def remove(self,key):
        hc=abs(hash(key))
        i=hc%self.bucketSize
        prev=None
        head=self.buckets[i]
        while head is not None:
            if head.key==key:
                if prev is None:
                    self.buckets[i] = head.next
                else:
                    prev.next=head.next
                self.count-=1
                return head.value
            prev=head
            head=head.next
        return None
    
    
m=Map()
m.insert("atharva",5)
m.insert("deep",2)
m.insert("maths",8)
print(m.getValue("maths"))
print(m.size())
m.remove("maths")
print(m.getValue("maths"))
