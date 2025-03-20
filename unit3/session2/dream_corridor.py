def max_corridor_area(segments):
    left, right = 0, len(segments) - 1
    max_area = 0
    while left < right:
        width = right - left
        height = min(segments[left], segments[right])
        area = width * height
        if area > max_area:
            max_area = area
        if segments[left] < segments[right]:
            left += 1
        else:
            right -= 1
    return max_area
print(max_corridor_area([1, 8, 6, 2, 5, 4, 8, 3, 7])) 
print(max_corridor_area([1, 1])) 