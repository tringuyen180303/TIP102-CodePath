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

def delete_dupes(head):
    # nums = set()

    # current = head
    # temp_head = Node(-1)
    # temp_head.head = head
    # while current:
    #     # if current.value not in nums:
    #     #     nums.add(current.value)
    #     # elif current.next.value in nums:
    #     if current
    if not head or not head.next:
        return head
    
    current = head
    temp_head = Node(0)
    temp_head.next = head
    prev = temp_head
  
    
    while current and current.next:
        print("prev", prev.value)
        duplicate = False
        while current.value == current.next.value:
            #prev.next = current.next
            current = current.next
            duplicate = True

            print("moving", current.value)
        if duplicate:
            current = current.next
        prev.next = current
        prev = current
        current = current.next
        

    return temp_head.next




#head = Node(1, Node(2, Node(3, Node(3, Node(4, Node(5))))))
head = Node(1, Node(2, Node(3, Node(3, Node(3,Node(4, Node(5)))))))
# Linked List: 1 -> 2 -> 3 -> 3 -> 4 -> 5
print_linked_list(delete_dupes(head))


