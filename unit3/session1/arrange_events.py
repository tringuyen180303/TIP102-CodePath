def arrange_attendees_by_priority(attendees, priority):
    priority_values = 0
    stack = []
    for num in attendees:
        if num == priority:
            priority_values += 1
        if num > priority:
            
print(arrange_attendees_by_priority([9,12,5,10,14,3,10], 10)) 
print(arrange_attendees_by_priority([-3,4,3,2], 2)) 