with open("p022_names.txt", "r") as file:
    data = sorted(file.read().replace("\"", "").split(","))
print(sum(sum(" ABCDEFGHIJKLMNOPQRSTUVWXYZ".index(i) for i in data[j]) * (j + 1) for j in range(len(data))))
