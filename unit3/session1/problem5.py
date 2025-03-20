def min_changes_to_make_balanced(schedule):
    stack = []
    error = 0
    for char in schedule:
        if char == "(":
            stack.append(char)
        elif char == "C":
            if stack:
                stack.pop()
            else:
                error += 1
    return error + len(stack)

print(min_changes_to_make_balanced("())"))
print(min_changes_to_make_balanced("(((")) 