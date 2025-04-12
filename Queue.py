class Queue:
    def __init__(self):
        self.queue = []


    def enqueue(self,item):
        self.queue.append(item)


    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)
        else:
            print("queue is empty")


    def peek(self):
        if not self.is_empty():
            return self.queue[0]
        else:
            print("queue is empty")


    def size(self):
        return len(self.queue)


    def is_empty(self):
        return len(self.queue) == 0


    def display(self):
        print("Queue contains top to bottom " , self.queue[::-1])     # print from top to botom
        print("bottom to top ",self.queue)  # it will print list as it is from bottom  to top


q = Queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.enqueue(40)
q.dequeue()
q.display()

print("top of queue :", q.peek())
print("size of queue : ", q.size())

q2 = Queue()
print(q2.size())
q2.dequeue()