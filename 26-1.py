with open("26-1.txt") as file:
    number = sum(list(map(int, file.readlines()))[1:])
    day = 0
    while number >= 300:
        number -= 300
        day += 1
        if day % 4 == 0 and day != 0:
            number += 500

    print(day, 300 - number)