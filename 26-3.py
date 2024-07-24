with open("26-3.txt") as file:
    number = sorted(list(map(int, file.readlines()))[1:], reverse=True)
    light = sorted([number[0], number[1], number[2]])
    number = number[3:]
    day = 0
    while len(number) > 0:
        for i in range(len(light)):
            if light[i] < 100:
                search = 100 - light[i]
                while search not in number and search <= 100:
                    search += 1
                if search in number:
                    light[i] += search
                    number.remove(search)
                else:
                    if len(number) != 0:

                        light[i] += number[0]
                        number.pop(0)
        if light[0] >= 100 and light[1] >= 100 and light[2] >= 100:
            light[0] -= 100
            light[1] -= 100
            light[2] -= 100
            day += 1
        if day % 4 == 0 and day != 0:
            day += 1
            number.append(100)
            number.append(100)
result = sum([100 - i for i in light if i <= 100])
print(day, result)