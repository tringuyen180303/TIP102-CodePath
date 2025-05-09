def is_strongly_connected(celebrities):
    dictionary = {
    }

    for celeb, like in celebrities.items():
        seen = set()
        for one in like:
            if one != celeb and one not in seen and one in celebrities:
                seen.add(one)
        dictionary[celeb] = len(seen)

    for key, val in dictionary.items():
        if val != len(celebrities) - 1:
            return False
    return True
    



celebrities1 = {
    "Dev Patel": ["Meryl Streep", "Viola Davis"],
    "Meryl Streep": ["Dev Patel", "Viola Davis"],
    "Viola Davis": ["Meryl Streep", "Dev Patel"]
}

celebrities2 = {
    "John Cho": ["Rami Malek", "Zoe Saldana", "Meryl Streep"],
    "Rami Malek": ["John Cho", "Zoe Saldana", "Meryl Streep"],
    "Zoe Saldana": ["Rami Malek", "John Cho", "Meryl Streep"],
    "Meryl Streep": []
}


print(is_strongly_connected(celebrities1))
print(is_strongly_connected(celebrities2))