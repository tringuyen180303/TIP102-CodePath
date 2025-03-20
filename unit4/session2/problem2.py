def find_most_frequent_keywords(scenes):
    counts = {}
    for scene in scenes.values():
        for value in scene:
            if value not in counts:
                counts[value] = 0
            counts[value] +=1
    answer = []
    max_value = max(counts.values())
    for key, val in counts.items():
        if val == max_value:
            answer.append(key)
    return answer


scenes = {
    "Scene 1": ["action", "hero", "battle"],
    "Scene 2": ["hero", "action", "quest"],
    "Scene 3": ["battle", "strategy", "hero"],
    "Scene 4": ["action", "strategy"]
}
print(find_most_frequent_keywords(scenes))

scenes = {
    "Scene A": ["love", "drama"],
    "Scene B": ["drama", "love"],
    "Scene C": ["comedy", "love"],
    "Scene D": ["comedy", "drama"]
}
print(find_most_frequent_keywords(scenes)) 