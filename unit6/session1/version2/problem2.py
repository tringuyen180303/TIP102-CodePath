class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def cycle_start(path_start):
    slow = path_start
    fast = path_start
    has_cycle = False
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next

        if fast == slow:
            has_cycle = True
            break
    
    slow = path_start
    while slow != fast :
        slow = slow.next
        fast = fast.next
    return slow.value
path_start = Node('Start', Node('Point 1', Node('Point 2', Node('Point 3', Node("Point 4")))))
path_start.next.next.next.next.next = path_start.next.next
print(cycle_start(path_start))