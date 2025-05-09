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

def odd_even_experiments(exp_results):
    odd = exp_results
    even  = exp_results.next

    even_head = even

    while even_head and even_head.next:
        nextOdd = even_head.next
        odd.next = even_head.next
        odd = nextOdd

        nextEven = odd.next
        even_head.next = nextEven
        even_head = nextEven
    odd.next = even
    return exp_results

experiment_results1 = Node(1, Node(2, Node(3, Node(4, Node(5)))))
experiment_results2 = Node(2, Node(1, Node(3, Node(5, Node(6, Node(4, Node(7)))))))

print_linked_list(odd_even_experiments(experiment_results1))
print_linked_list(odd_even_experiments(experiment_results2))