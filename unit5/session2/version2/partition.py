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

def partition(head, val):
    small_dummy = Node(0)
    large_dummy = Node(0)

    small = small_dummy
    large = large_dummy

    curr = head

    while curr:
        if curr.value < val:
            small.next = curr
            small = small.next
        else:
            large.next = curr
            large = large.next
        curr = curr.next
    small.next = large_dummy.next
    large.next = None
    return small_dummy.next
head = Node(1, Node(4, Node(3, Node(2, Node(5, Node(2))))))

print_linked_list(partition(head, 4))