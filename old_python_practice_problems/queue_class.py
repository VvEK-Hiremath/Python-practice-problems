class queue:
    def __init__(self):
        self.q = list()

    def insert(self,a):
        self.q.append(a)

    def pop(self):
        self.q.pop(0)

    def front(self):
        if(len(self.q) == 0):
            return "queue is empty"
        else:
            return self.q[0]
        
    def isempty(self):
        if(len(self.q) == 0):
            return True
        else:
            return False
        
q1 = queue()
for i in range(1,5):
    q1.insert(i*i)

while(not q1.isempty()):
    print(q1.front(),end="\n")
    t = q1.front()
    print("{} removed".format(t))
    q1.pop()
    print(len(q1.q),end = "\n\n")

