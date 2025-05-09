
def decode_scroll(scroll):
    stack = []
    current_string = ""
    current_num = 0
    
    for char in scroll:
        if char.isdigit():
            # Build the number (could be more than one digit)
            current_num = current_num * 10 + int(char)
        elif char == '[':
            # Push the current number and current string to the stack
            stack.append((current_string, current_num))
            # Reset the current string and number
            current_string = ""
            current_num = 0
        elif char == ']':
            # Pop the last string and number from the stack
            prev_string, num = stack.pop()
            # Repeat the current string num times and add it to the previous string
            current_string = prev_string + current_string * num
        else:
            # Regular character, just add it to the current string
            current_string += char
    
    return current_string

def decode_scroll_recursive(scroll):
    return decode_partition(scroll, [], "", 0)

def decode_partition(scroll, stack, curr_str, curr_num):
    print("scroll", scroll[1:])
    if len(scroll) == 0:
        return curr_str
    if scroll[0] == "]":
        prev_str, num = stack.pop()
        curr_str = prev_str + curr_str * num
        
    elif scroll[0] == "[":
        stack.append((curr_str, curr_num))
        print("stack", stack)
        curr_str = ""
        curr_num = 0
    

    elif scroll[0].isdigit():
        curr_num = curr_num * 10 + int(scroll[0])
        #print("curr num" ,curr_num)
    else:
        curr_str += scroll[0]
        #print("curr str", curr_str)

    
    return decode_partition(scroll[1:], stack, curr_str, curr_num)



scroll = "3[Coral2[Shell]]"
print(decode_scroll_recursive(scroll))

scroll = "2[Poseidon3[Sea]]"
print(decode_scroll_recursive(scroll))