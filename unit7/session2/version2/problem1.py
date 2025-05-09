def find_affordable_ticket(prices, budget):
    low = 0
    high = len(prices) - 1
    best_diff = 10000
    best_idx = -1
    while low <= high:
        mid = (low + high) // 2
        diff = budget - prices[mid]
        if diff > 0 and best_diff > diff:
            best_diff = diff
            best_idx = mid
        if prices[mid] == budget:
            return mid
        elif prices[mid] > budget:
            high = mid - 1
        else:
            low = mid + 1
    
    return best_idx
print(find_affordable_ticket([50, 60, 65 ,75,80, 85 ,100, 150], 90))