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


def reverse(head):
     current = head
     prev = None
     while current:
        nextNode = current.next

        current.next = prev
        prev = current
        current = nextNode
        
    
     return prev

kart_choices = Node("Bullet Bike", Node("Wild Wing", Node("Pirahna Prowler")))

print_linked_list(reverse(kart_choices))