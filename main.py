a = open("C:\\Users\\Twwan\\Desktop\\24.txt")
b = a.readlines()
maximum = 0
k = 0
j = 0
for i in range(len(b)):
    k += 1
    if b[i] == "D":
        j += 1
        if j == 2:
            k -= 1
            maximum = max(maximum, k)
print(maximum)