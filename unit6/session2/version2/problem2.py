class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

import random
# For testing
def print_linked_list(head):
    current = head
    while current:
        print(current.value, end=" -> " if current.next else "")
        current = current.next
    print()

def get_random(playlist):
    count = 0
    curr = playlist
    while curr:
        count += 1
        curr = curr.next
    random_number = random.randint(0, count-1)
    
    curr = playlist
    index = 0
    print(random_number)
    while index < random_number:
        curr = curr.next
        index += 1
    return curr.value
catalogue = Node(('Homegoing', 'Yaa Gyasi'), 
                Node(('Pachinko', 'Min Jin Lee'),
                         Node(('The Night Watchman', 'Louise Erdrich'))))

print(get_random(catalogue))