def get_adj_matrix(clients):
    dictionary = {}
    idx = 0
    for client in clients:
        celebA, celebB = client[0], client[1]
        if celebA not in dictionary:
            dictionary[celebA] = idx
            idx += 1
        if celebB not in dictionary:
            dictionary[celebB] = idx
            idx += 1
    print(dictionary)

    matrix = [[0 for i in range(len(dictionary))] for j in range(len(dictionary))]
    for client in clients:
        celebA_pos, celebB_pos = dictionary.get(client[0]), dictionary.get(client[1])
        matrix[celebA_pos][celebB_pos] = 1
        matrix[celebB_pos][celebA_pos] = 1
    
    return dictionary, matrix
clients = [
            ["Yalitza Aparicio", "Julio Torres"], 
            ["Julio Torres", "Fred Armisen"], 
            ["Bowen Yang", "Julio Torres"],
            ["Bowen Yang", "Margaret Cho"],
            ["Margaret Cho", "Ali Wong"],
            ["Ali Wong", "Fred Armisen"], 
            ["Ali Wong", "Bowen Yang"]]

id_map, adj_matrix = get_adj_matrix(clients)
print(id_map)
print(adj_matrix)

"""
Example Output:

{
  'Fred Armisen': 0,
  'Yalitza Aparicio': 1,
  'Margaret Cho': 2,
  'Bowen Yang': 3,
  'Ali Wong': 4,
  'Julio Torres': 5
}

[
  [0, 0, 0, 0, 1, 1],  # Fred Armisen
  [0, 0, 0, 0, 0, 1],  # Yalitza Aparicio
  [0, 0, 0, 1, 1, 0],  # Margaret Cho
  [0, 0, 1, 0, 1, 1],  # Bowen Yang
  [1, 0, 1, 1, 0, 0],  # Ali Wong
  [1, 1, 0, 1, 0, 0]   # Julio Torres
]

Note: The order in which you assign IDs and consequently your adjacency matrix may look different
"""