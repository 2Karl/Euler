with open("p067_triangle.txt", "r") as file:
    data = [[int(x) for x in x.split(" ")] for x in file.read().split("\n")]

for i in range(len(data)-2, -1, -1):
    for j in range(len(data[i])):
        data[i][j] += max(data[i+1][j:j+2])
print(data[0][0])