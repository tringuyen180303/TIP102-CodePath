def map_chambers(sections):
    if len(sections) == 1:
        return sections[0]
    
    return {sections[0] : map_chambers(sections[1:])}

sections = ["Atlantis", ["Coral Cave", ["Pearl Chamber"]]]
#{'Atlantis': {'Coral Cave': 'Pearl Chamber'}}
print(map_chambers(sections))