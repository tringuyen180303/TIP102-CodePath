
def find_closest_planets(planets, target_distance, k):
    results = []

    position = binary_closest_index(planets, target_distance)
    left, right = position, position + 1
    print(left, right)
    for _ in range(k):
        if left < 0:
            results.append(planets[right])
            right += 1
        elif right >= len(planets):
            results.append(planets[left])
            left -= 1
        else:
            left_diff = abs(planets[left] - target_distance)
            right_diff = abs(planets[right] - target_distance)

            if left_diff < right_diff:
                results.append(planets[left])
                left -= 1
            elif left_diff > right_diff:
                results.append(planets[right])
                right += 1
            else:
                results.append(planets[left])
                left -= 1
    return sorted(results)

def binary_closest_index(planets, target_distance):
    low = 0
    high = len(planets) - 1
    best_diff = 1000000
    best_idx = 0
    while low <= high:
        mid = (low+high) // 2
        diff = abs(planets[mid] - target_distance)
        if diff < best_diff or (diff == best_diff and planets[mid] < planets[best_idx]):
            best_diff = diff
            best_idx = mid

        if planets[mid] == target_distance:
            return mid
        elif planets[mid] < target_distance:
            low = mid + 1
        else:
            high = mid - 1
    return best_idx

planets1 = [100, 200, 300, 400, 500]
planets2 = [10, 20, 30, 40, 50]

#print(find_closest_planets(planets1, 350, 3))
print(find_closest_planets(planets2, 25, 2))