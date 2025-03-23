class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def has_cycle(head):
    fast = head
    slow = head
    current = head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
        if fast == slow:
            return True
        
    return False

peach = Node("Peach", Node("Luigi", Node("Mario", Node("Toad", Node("Luigi")))))
# Create nodes manually
node4 = Node("Toad")
node3 = Node("Mario", node4)
node2 = Node("Luigi", node3)
node1 = Node("Peach", node2)

# Create the cycle
node4.next = node2

print(has_cycle(node1))  # Output: True

print(has_cycle(peach))