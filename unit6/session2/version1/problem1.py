class Node:
	def __init__(self, value, next=None):
		self.value = value
		self.next = next

# For testing
def print_queue(head):
    current = head.front
    while current:
        print(current.value, end=" -> " if current.next else "")
        current = current.next
    print()

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
    
    def is_empty(self):
        if self.front is None:
             return True
        return False

    def enqueue(self, value):
        if self.is_empty():
             self.front = Node(value)
             self.rear = Node(value)
        else:
            curr = self.front

            while curr.next:
                curr = curr.next
            curr.next = Node(value)
            self.rear = curr.next
    
    def dequeue(self):
        if self.is_empty():
            return None
        dummy = Node(0)
        dummy.next = self.front
        nextNode = self.front.next
        self.front = nextNode
        return dummy.next.value
    
    def peek(self):
         if self.is_empty():
              return None
         return self.front.value
        

q = Queue()

# Add elements to the queue
q.enqueue(('Love Song', 'Sara Bareilles'))
q.enqueue(('Ballad of Big Nothing', 'Elliot Smith'))
q.enqueue(('Hug from a Dinosaur', 'Torres'))
print_queue(q)

# View the front element
print("Peek: ", q.peek()) 

# Remove elements from the queue
print("Dequeue: ", q.dequeue()) 
print("Dequeue: ", q.dequeue()) 

# Check if the queue is empty
print("Is Empty: ", q.is_empty()) 

# Remove the last element
print("Dequeue: ", q.dequeue()) 

# Check if the queue is empty
print("Is Empty:", q.is_empty()) 