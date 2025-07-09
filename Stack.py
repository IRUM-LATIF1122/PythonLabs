 # implementation of Stack
class Stack:
    def __init__(self):
        self.stack = []

    # Push element to the stack
    def push(self, item):
        self.stack.append(item)

    # Pop element from the stack
    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            return "Stack is empty"

    # Peek the top element of the stack
    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            return "Stack is empty"

    # Check if the stack is empty
    def is_empty(self):
        return len(self.stack) == 0

    # Get the size of the stack
    def size(self):
        return len(self.stack)

    # Display the stack
    def display(self):
        print("Stack (top -> bottom):", self.stack[::-1])

# Example usage
s = Stack()
s.push(10)
s.push(20)
s.push(30)
s.push("irum")
s.display()

# print("Top Element:", s.peek())
print("Popped:", s.pop())
s.display()

