def detect_temporal_anomaly(time_points, k):
    dictionary = {}

    for i, time in enumerate(time_points):
        if time in dictionary and i - dictionary[time] <= k:
            return True
        dictionary[time] = i
    return False



time_points1 = [1, 2, 3, 1]
k1 = 3

time_points2 = [1, 0, 1, 1]
k2 = 1

time_points3 = [1, 2, 3, 1, 2, 3]
k3 = 2

print(detect_temporal_anomaly(time_points1, k1))  
print(detect_temporal_anomaly(time_points2, k2)) 
print(detect_temporal_anomaly(time_points3, k3)) 