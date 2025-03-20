class Node:
    def __init__(self, player, next=None):
        self.player_name = player
        self.next = next

# For testing
def print_linked_list(head):
    current = head
    while current:
        print(current.player_name, end=" -> " if current.next else "\n")
        current = current.next

def increment_rank(head, target):
    if head is None:
        return head
    
    if target == 1:
        return head
    
    current_target = 0
    current = head
    while current and current_target < target - 1:
        current_target += 1
        if current_target == target - 2:
            first = current.next
            second = first.next

            first.next = second.next
            second.next = first
            current.next = second
        current = current.next
    return head



racers1 = Node("Mario", Node("Peach", Node("Luigi", Node("Daisy"))))
racers2 = Node("Mario", Node("Luigi"))

print_linked_list(increment_rank(racers1, 3))
print_linked_list(increment_rank(racers2, 1)) 
print_linked_list(increment_rank(None, 1)) 