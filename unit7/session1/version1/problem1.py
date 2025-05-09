def count_layers(sandwich):
    print("length:",len(sandwich))
    print("sandwich next", sandwich[1:])
    if len(sandwich) == 1:
        return 1
    return 1 + count_layers(sandwich[1:][0])
sandwich1 = ["bread", ["lettuce", ["tomato", ["bread"]]]]
sandwich2 = ["bread", ["cheese", ["ham", ["mustard", ["bread"]]]]]

print(count_layers(sandwich1))
print(count_layers(sandwich2))