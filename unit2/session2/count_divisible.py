def count_divisible_collections(collection_sizes, k):
    prefix_sum = 0
    count = 0
    prefix_count = {0: 1}  # Initialize with 0: 1 to handle cases where the prefix sum itself is divisible by k
    
    for size in collection_sizes:
        prefix_sum += size
        mod = prefix_sum % k
        
        if mod in prefix_count:
            count += prefix_count[mod]
            prefix_count[mod] += 1
        else:
            prefix_count[mod] = 1
    
    return count

nums1 = [4, 5, 0, -2, -3, 1]
k1 = 5
nums2 = [5]
k2 = 9

print(count_divisible_collections(nums1, k1))  
print(count_divisible_collections(nums2, k2))  