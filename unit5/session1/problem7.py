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

def last_place(head):
      if head is None:
        return None
      if head.next is None:
        return head.player_name
      if head.next:
        return last_place(head.next)


     
racers1 = Node("Mario", Node("Peach", Node("Luigi", Node("Daisy"))))
racers2 = Node("Mario")

print(last_place(racers1)) 
print(last_place(racers2)) 
print(last_place(None))