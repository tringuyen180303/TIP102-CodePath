class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next

# For testing
def print_linked_list(head):
    current = head
    while current:
        print(current.value, end=" -> " if current.next else "\n")
        current = current.next

# Function with a bug!
def remove_by_value(head, val):
    if not head:
        return None
    if head.value == val:
        return head.next  

    current = head
    while current is not None:
        if current.next.value == val:
            current.next = current.next.next  
            return head  
        current = current.next
        print("current updated", current.value)

    return head

head = Node("Daisy", Node("Mario", Node("Waluigi", Node("Baby Peach"))))

print_linked_list(remove_by_value(head, "Waluigi"))