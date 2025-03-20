from collections import deque

def reveal_attendee_list_in_order(attendees):
    new_attendees = sorted(attendees, reverse=True)
    print(new_attendees)

    queue = deque()

    for attendee in new_attendees:
        if queue:
            queue.appendleft(queue.pop())
        
        queue.appendleft(attendee)
            
    return list(queue)

print(reveal_attendee_list_in_order([17,13,11,2,3,5,7])) 
print(reveal_attendee_list_in_order([1,1000]))