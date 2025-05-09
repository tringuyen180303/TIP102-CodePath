def concert_playlists(song_durations, concert_limits):
    song_durations.sort()

    prefix_sums = []
    total = 0
    for duration in song_durations:
        total += duration
        prefix_sums.append(total)

    def binary_search(prefix_sums, limit):
        low = 0
        high = len(prefix_sums)

        while low <= high:
            mid = (low+high) // 2
            if prefix_sums[mid] == limit:
                return mid + 1
            elif prefix_sums[mid] < limit:
                low = mid + 1
            else:
                high = mid - 1
        return high + 1
    print(prefix_sums)
    # print(binary_search(prefix_sums, 1))
    res = []
    for limit in concert_limits:
        max_song = binary_search(prefix_sums, limit)
        res.append(max_song)
    return res
song_durations1 = [4, 3, 1, 2, 3, 2]
concert_limits1 = [5, 10, 15]

song_durations2 = [2, 3, 4, 5]
concert_limits2 = [1]

print(concert_playlists(song_durations1, concert_limits1))
#print(concert_playlists(song_durations2, concert_limits2))