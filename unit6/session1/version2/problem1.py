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

def game_result(head):
    odd_points = even_points = 0
    curr = head
    while curr and curr.next:
        even = curr.value
        odd = curr.next.value
		
        if even < odd:
            odd_points += 1
        else:
            even_points += 1
        
        curr = curr.next.next

    if odd_points > even_points:
          return "Odd"
    elif even_points > odd_points:
          return "Even"
    else:
          return "Tie"
	

game1 = Node(2, Node(1))
game2 = Node(2, Node(5, Node(4, Node(7, Node(20, Node(5))))))
game3 = Node(4, Node(5, Node(2, Node(1))))

print(game_result(game1))
print(game_result(game2))
print(game_result(game3))