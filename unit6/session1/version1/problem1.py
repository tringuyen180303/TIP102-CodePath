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

def edit_dna_sequence(dna_strand, m, n):
    
    #curr_m = 0
    curr = dna_strand
    while curr:
        
        for j in range(1, m):
            curr = curr.next
        if not curr:
            break
        temp_head = curr
        print("temp hed", temp_head.value)
        for i in range(n):
            if temp_head:
                temp_head = temp_head.next
            else:
                break
        
        
        curr.next = temp_head
        
        curr = temp_head

    return dna_strand




dna_strand = Node(1, Node(2, Node(3, Node(4, Node(5, Node(6, Node(7, Node(8, Node(9, Node(10, Node(11, Node(12, Node(13)))))))))))))

print_linked_list(edit_dna_sequence(dna_strand, 2, 3))