class Node:
	def __init__(self, value, next=None):
		self.value = value
		self.next = next

# For testing
def print_linked_list(head):
    current = head
    while current:
        print(current.value, end=" -> " if current.next else "\n")
        current = current.next
        
def reverse_first_k(head, k):
    if head is None:
        return None
    
    count = 1
    curr = head
    prev = None
    slow = head
    while count <= k and curr:
        nextNode = curr.next

        curr.next = prev
        prev = curr
        curr = nextNode
        count += 1
    head.next = curr
    
    
    
    return prev



head = Node("apple", Node("cherry", Node("orange", Node("peach", Node("pear")))))

print_linked_list(reverse_first_k(head, 3))