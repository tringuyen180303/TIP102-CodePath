def reverse_orders(orders):
    #print(orders)
    words = orders.split(" ")
    if len(words) == 1:
        return words[0]
    
    return reverse_orders(" ".join(words[1:]))  +  " " + words[0]
print(reverse_orders("Bagel Sandwich Coffee"))