data = [1,5,10,55,3,9]

def swap (data, i):
    temp = data[i]
    data[i] = data[i + 1]
    data[i + 1] = temp

for i in range(len(data) - 1):
    for j in range(len(data) - 1):
        if data[j] > data[j + 1]:
            swap(data, j)


print(data)