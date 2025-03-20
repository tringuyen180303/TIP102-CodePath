def display_time_portal_usage(usage_records):
    dictionary = {}
    unique_time = set()

    for name, portal, time in usage_records:
        if portal not in dictionary:
            dictionary[portal] = {}
        unique_time.add(time)
        if time not in dictionary[portal]:
            dictionary[portal][time] = 1
        else:
            dictionary[portal][time] += 1
    #dictionary = dict(sorted(dictionary.items()))

    sorted_dict = {int(k): v for k, v in dictionary.items()}  # Convert to int for sorting
    sorted_dict = dict(sorted(sorted_dict.items()))

    display_table = []
    unique_time = sorted(list(unique_time))
    display_table.append(["Portal"] + unique_time)
    
    #print(dictionary)
    for portal in sorted_dict:
        row = [portal]
        for time in unique_time:
            if time not in dictionary[portal]:
                row += "0"
            else:
                row += str(dictionary[portal][time])
        display_table.append(row)
    return display_table
                
# def display_time_portal_usage(usage_records):
#     dictionary = {}
#     unique_time = set()

#     # Populate the dictionary and collect unique times
#     for name, portal, time in usage_records:
#         if portal not in dictionary:
#             dictionary[portal] = {}
#         unique_time.add(time)
#         dictionary[portal][time] = dictionary[portal].get(time, 0) + 1

#     # Sort dictionary keys numerically (assuming portals are strings representing numbers)
#     sorted_dict = {int(k): v for k, v in dictionary.items()}  # Convert to int for sorting
#     sorted_dict = dict(sorted(sorted_dict.items()))  # Sort numerically

#     # Sort times in chronological order
#     sorted_times = sorted(unique_time)

#     # Construct the display table
#     display_table = []
#     display_table.append(["Portal"] + sorted_times)

#     for portal in sorted_dict:
#         row = [str(portal)]  # Convert back to string for display
#         for time in sorted_times:
#             row.append(str(sorted_dict[portal].get(time, 0)))  # Append as string
#         display_table.append(row)

#     return display_table



usage_records1 = [["David","3","10:00"],
                  ["Corina","10","10:15"],
                  ["David","3","10:30"],
                  ["Carla","5","11:00"],
                  ["Carla","5","10:00"],
                  ["Rous","3","10:00"]]
usage_records2 = [["James","12","11:00"],
                  ["Ratesh","12","11:00"],
                  ["Amadeus","12","11:00"],
                  ["Adam","1","09:00"],
                  ["Brianna","1","09:00"]]
usage_records3 = [["Laura","2","08:00"],
                  ["Jhon","2","08:15"],
                  ["Melissa","2","08:30"]]

print(display_time_portal_usage(usage_records1))
print(display_time_portal_usage(usage_records2))
print(display_time_portal_usage(usage_records3))