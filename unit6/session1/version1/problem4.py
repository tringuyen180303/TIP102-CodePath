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

# def max_protein_pair_stability(head):
#     values = []
#     curr = head

#     while curr:
#         values.append(curr.value)
#         curr = curr.next
#     print(values)
#     max_sum = 0
#     n = len(values)
#     for i in range(len(values) // 2):
#         pair_sum = values[i] + values[n-i-1]
#         if pair_sum > max_sum:
#             max_sum = pair_sum
#     return max_sum
        
def max_protein_pair_stability(head):
    if not head:
        return 0

    # Step 1: Find the middle of the linked list using slow and fast pointers.
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    
    prev = None
    curr = slow
    while curr:
        nextNode = curr.next
        curr.next = prev
        prev = curr
        curr = nextNode
    
    max_sum = 0
    first = head
    second = prev

    while second:
        sum = first.value + second.value
        if sum > max_sum:
            max_sum = sum
        second = second.next
        first = first.next
    
    return max_sum

    print(slow.value)
head1 = Node(5, Node(4, Node(2, Node(1))))
head2 = Node(4, Node(2, Node(2, Node(3))))

print(max_protein_pair_stability(head1))
print(max_protein_pair_stability(head2))