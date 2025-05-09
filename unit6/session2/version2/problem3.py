class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

# For testing
def print_linked_list(head):
    current = head
    while current:
        print(current.value, end=" -> " if current.next else "")
        current = current.next
    print()

def swap_books(shelf, k):
    curr = shelf
    fast = slow = shelf
    count = 0
    for i in range(k):
        count += 1
        fast = fast.next
    #print(fast.value)

    while fast and fast.next:
        count += 1
        slow = slow.next
        fast = fast.next
    print(count)
    print(slow.next.value)
shelf = Node('Book 1', Node('Book 2', Node('Book 3', Node('Book 4', Node('Book 5')))))

print_linked_list(swap_books(shelf, 2))