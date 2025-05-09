def find_itinerary(boarding_passes):
    mapping = {dep: arr for dep, arr in boarding_passes}
    print(mapping)
    arrivals = mapping.values()
    departures = mapping.keys()
    node = departures - arrivals
    start = node.pop()
    res = [start]
    while start in mapping:
        next_des = mapping[start]
        res.append(next_des)
        start = next_des
    return res

boarding_passes_1 = [
                    ("JFK", "ATL"),
                    ("SFO", "JFK"),
                    ("ATL", "ORD"),
                    ("LAX", "SFO")]

boarding_passes_2 = [
                    ("LAX", "DXB"),
                    ("DFW", "JFK"),
                    ("LHR", "DFW"),
                    ("JFK", "LAX")]

print(find_itinerary(boarding_passes_1))
print(find_itinerary(boarding_passes_2))