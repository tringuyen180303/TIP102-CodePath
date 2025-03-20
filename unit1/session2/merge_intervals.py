def merge_intervals(intervals):
    i = 0
    j = i + 1
    while j < len(intervals):
        if intervals[i][1] >= intervals[j][0]:
            intervals[i][1] = max(intervals[i][1], intervals[j][1])
            del intervals[j]
        i += 1
        j += 1
    return intervals
intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
merge_intervals(intervals)
print(intervals)