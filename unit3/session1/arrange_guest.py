def arrange_guest_arrival_order(arrival_pattern):
    guest_order = ""
    stack = []
    for i in range(len(arrival_pattern)):
        if i == 0 and arrival_pattern[i] == "D":
            stack.append(i+1)
        if arrival_pattern[i] == "I":
            stack.append(i+1)
            #stack.append(i+2)
        elif arrival_pattern[i] == "D":
            stack.append(i+2)
            #stack.append(i+1)
    while stack:
        guest_order += str(stack.pop())
    return guest_order

def arrange_guest_arrival_order(arrival_pattern):
    n = len(arrival_pattern)
    result = []
    stack = []
    
    for i in range(n + 1):
        stack.append(str(i + 1))  # Push next available number onto the stack
        print("stack",stack)
        if i == n or arrival_pattern[i] == 'I':
            while stack:
                result.append(stack.pop())  # Pop all elements when 'I' is encountered or at the end
                print(result)
    #print(stack)
    return "".join(result)

print(arrange_guest_arrival_order("IIIDIDDD"))  
print(arrange_guest_arrival_order("DDD"))  