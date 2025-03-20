def rearrange_guests(guests):
    positive_array = []
    negative_array = []
    for i in range(len(guests)):
        if guests[i] > 0:
            positive_array.append(guests[i])
        else:
            negative_array.append(guests[i])
    print("positive", positive_array)
    print(negative_array)
    return_array = []
    while positive_array and negative_array:
        return_array.append(positive_array.pop(0))
        return_array.append(negative_array.pop(0))
    return return_array
    

print(rearrange_guests([3,1,-2,-5,2,-4]))  
print(rearrange_guests([-1,1])) 