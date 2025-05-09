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

def sort_list(head):
	dummy = Node(0)
	curr = head
	while curr:
		dummy_temp = dummy
		while dummy_temp.next and dummy_temp.next.value < curr.value:
			dummy_temp = dummy_temp.next
		nextNode = curr.next
		curr.next = dummy_temp.next
		dummy_temp.next = curr
		curr = nextNode
	return dummy.next
        

head1 = Node(4, Node(2, Node(1, Node(3))))
head2 = Node(-1, Node(5, Node(3, Node(4, Node(0)))))

print_linked_list(sort_list(head1))
#print_linked_list(sort_list(head2))