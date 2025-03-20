def shuffle(message, indices):
    str = ""
    for i in indices:
        str += message[i]
    return str

print(shuffle("hello", [4, 3, 2, 1, 0]))
message = "evil"
indices = [3, 1, 2, 0]
print(shuffle(message, indices))

message = "findme"
indices = [0, 1, 2, 3, 4, 5]
print(shuffle(message, indices))