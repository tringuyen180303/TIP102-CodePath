import math
def min_distribution_rate(booths, h):
    def possible_dis(r):
        hours_needed = sum(math.ceil(b / r)for b in booths)
        #print(hours_needed)
        return hours_needed <= h
    #return possible_dis(8)

    low, high = 1, max(booths)
    res = high
    while low <= high:
        mid = (low + high) // 2
        if possible_dis(mid):
            res = mid
            high = mid - 1
        else:
            low = mid + 1
    return res

print(min_distribution_rate([3, 6, 7, 11], 8))
print(min_distribution_rate([30,11,23,4,20], 5))
print(min_distribution_rate([30,11,23,4,20], 6))