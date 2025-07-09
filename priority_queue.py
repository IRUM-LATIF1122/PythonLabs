class priority_queue:
    def __init__(self):
        self.p_l = []  # priority list
        self.d_l = []  # data list

    def enqueue(self, d, p):
        self.p_l.append(p)
        self.d_l.append(d)

    def dequeue(self):
        if not  self.d_l:
            return None

        minim = self.p_l[0]
        index = 0
        for i in range(len(self.p_l)):
            if minim > self.p_l[i]:
                minim = self.p_l[i]
                index = i

        self.p_l.pop(index)
        return self.d_l.pop(index)

    def display(self):
        print(self.d_l)


pq = priority_queue()
pq.enqueue(10, 3)
pq.enqueue(20, 1)
pq.enqueue(300, 2)

pq.display()
print(pq.dequeue())

pq.display()