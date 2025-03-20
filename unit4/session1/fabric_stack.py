def organize_fabrics(fabrics):
    fabrics.sort(key = lambda x: x[1])
    #print(fabrics)
    answers_stack = []
    for i in range(len(fabrics)):
        answers_stack.append(fabrics.pop()[0])
    return answers_stack
fabrics = [("Organic Cotton", 8), ("Recycled Polyester", 6), ("Bamboo", 7), ("Hemp", 9)]
fabrics_2 = [("Linen", 5), ("Recycled Wool", 9), ("Tencel", 7), ("Organic Cotton", 6)]
fabrics_3 = [("Linen", 4), ("Hemp", 8), ("Recycled Polyester", 5), ("Bamboo", 7)]

print(organize_fabrics(fabrics))
print(organize_fabrics(fabrics_2))
print(organize_fabrics(fabrics_3))