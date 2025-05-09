class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def cycle_length(protein):
    slow = protein
    fast = protein
    has_cycle = False

    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
       
        if fast == slow:
            has_cycle = True
            break
    
    if not has_cycle:
        return []
    
    slow = protein
    while slow != fast:
        print("slow")
        slow = slow.next
        fast = fast.next

    cycle_start = slow
    print(cycle_start.value)

    cycle_nodes = [cycle_start.value]
    current = cycle_start.next
    while current != cycle_start:
        cycle_nodes.append(current.value)
        current = current.next
    
    return cycle_nodes
            

protein_head = Node('Ala', Node('Gly', Node('Leu', Node('Val'))))
protein_head.next.next.next.next = protein_head.next 

print(cycle_length(protein_head))