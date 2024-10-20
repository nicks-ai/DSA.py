class stack:
    stack = []

    def __init__(self):
        self.stack = []
    def put (self, name):
        self.stack.append(name)

    def remove (self):
        self.stack.pop()

    def peek (self):
        print(self.stack[-1])
    
    def display(self):
        stack = [i for i in self.stack]
        print(stack)
        


sample_stack = stack()
sample_stack.put(1)
sample_stack.put(2)
sample_stack.put(3)
sample_stack.put("nick")
sample_stack.put("jo")
sample_stack.put("rash")
sample_stack.remove()
sample_stack.peek()
sample_stack.display()
