f = open('26-2.txt')
n = int(f.readline())
count = 0
number = [[], [], [], [], []]
for z in f:
    x, y = map(int, z.split())
    if y < 3:
        count += 1
    number[x-1].append(y)
k1, k2, k3, k4, k5 = len(number[0]), len(number[1]), len(number[2]), len(number[3]), len(number[4])
print(k1, k2, k3, k4, k5)
#x - номер породы собаки
#print(int((sum(number[x-1]))/kx,count)