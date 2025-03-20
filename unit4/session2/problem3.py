def track_scene_transitions(scenes):
    if not scenes:
        return None
    i = 0
    while i < len(scenes)-1:
        #print(i)
        print(f"Transition from {scenes[i]} to {scenes[i+1]}")
        i += 1
scenes = ["Opening", "Rising Action", "Climax", "Falling Action", "Resolution"]
track_scene_transitions(scenes)
print("---------------")
scenes = ["Introduction", "Conflict", "Climax", "Denouement"]
track_scene_transitions(scenes)