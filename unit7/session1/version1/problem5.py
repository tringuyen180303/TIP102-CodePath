def evaluate_ternary_expression_recursive(expression):
    if len(expression) == 1:
        return expression
    
    boolean = expression[0]
    count =0 
    colon_idx = None
    for idx in range(2, len(expression)):
        if expression[idx] == "?":
            count += 1
        elif expression[idx] == ":":
            if count == 0:
                colon_idx = idx
                break
            else:
                count -= 1
    
    true_part = expression[2:colon_idx]
    false_part = expression[colon_idx+1:]

    if boolean == "T":
        return evaluate_ternary_expression_recursive(true_part)
    else:
        return evaluate_ternary_expression_recursive(false_part)
    


print(evaluate_ternary_expression_recursive("T?2:3"))
print(evaluate_ternary_expression_recursive("F?1:T?4:5"))
print(evaluate_ternary_expression_recursive("T?T?F:5:3"))