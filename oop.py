class CustomQueue:
    queue = []

    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        return self.queue.pop()
    
    def display_queue(self):
        print(self.queue)
    
sample_queue = CustomQueue()
sample_queue.enqueue("nick")
sample_queue.enqueue("jo")
sample_queue.enqueue("ras")
sample_queue.dequeue()
sample_queue.enqueue(1)
sample_queue.enqueue(2)
sample_queue.display_queue()
