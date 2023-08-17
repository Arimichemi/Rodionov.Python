massive = [1, 9, 7, 12, 27]
list_massive = []
for i in range(len(massive)):
    if int(massive[i]) % 3 == 0:
        list_massive.append(massive[i])
print(*list_massive, sep=', ')