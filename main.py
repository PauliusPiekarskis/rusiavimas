data = []
elm = int(input("kiek elementų sekoje?"))

for i in range(0,elm):
    a = int(input())
    data.append(a)

print("Jūsų seka:", data)

def swap (data, i):
    temp = data[i]
    data[i] = data[i + 1]
    data[i + 1] = temp

for i in range(len(data) - 1):
    for j in range(len(data) - 1):
        if data[j] > data[j + 1]:
            swap(data, j)


print("Surušiuota seka:", data)