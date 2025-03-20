# def find_travelers(anamolies):
#     dictionary = {}
#     for traveler, anamoly in anamolies:
#         if traveler in dictionary:
#             dictionary[traveler] += 1
#         else:
#             dictionary[traveler] = 1
#     zero_anamoly = []
#     one_anamoly = []
#     for traveler, count in dictionary.items():
#         if count == 1:
#             one_anamoly.append(traveler)
#         elif count == 0:
#             zero_anamoly.append(traveler)
#     return [sorted(zero_anamoly), sorted(one_anamoly)]


def find_travelers(anomalies):
    # Dictionary to store the count of anomalies for each traveler
    anomaly_count = {}
    
    for traveler, anomaly in anomalies:
        if traveler in anomaly_count:
            anomaly_count[traveler] += 1
        else:
            anomaly_count[traveler] = 1
    
    # Lists to store travelers with zero and exactly one anomaly
    no_anomalies = []
    one_anomaly = []
    
    # Consider only travelers that have experienced at least one anomaly
    for traveler, count in anomaly_count.items():
        if count == 1:
            one_anomaly.append(traveler)
        elif count == 0:
            no_anomalies.append(traveler)
    
    # Sort the lists
    no_anomalies.sort()
    one_anomaly.sort()
    
    return [no_anomalies, one_anomaly]

anomalies1 = [[1,3],[2,3],[3,6],[5,6],[5,7],[4,5],[4,8],[4,9],[10,4],[10,9]]
anomalies2 = [[2,3],[1,3],[5,4],[6,4]]

print(find_travelers(anomalies1)) 
print(find_travelers(anomalies2))