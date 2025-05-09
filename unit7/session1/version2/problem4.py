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

def merge_missions(mission1, mission2):
    if not mission1:
        return mission2
    if not mission2:
        return mission1
    
    temp1 = mission1.next
    temp2 = mission2.next

    if mission1.value <= mission2.value:
        mission1.next = mission2
        mission2.next = merge_missions(temp1, temp2)
    else:
        mission2.next = mission1
        mission1.next = merge_missions(temp1, temp2)
    
    return mission2


mission1 = Node(2, Node(2, Node(4)))
mission2 = Node(1, Node(3, Node(4)))

print_linked_list(merge_missions(mission1, mission2))