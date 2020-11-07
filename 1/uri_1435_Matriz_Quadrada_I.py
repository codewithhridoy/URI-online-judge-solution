while True:
    N = int(input())

    if (N == 0):
        break

    item_list =  []

    for item in range(N):
        temp = []
        for item2 in range(N):
            temp.append(1)
        item_list.append(temp)

    value = 1
    a = 0
    b = 0
    c = N - 1
    d = N - 1

    if (N % 2 == 0):
        avg = N / 2

    else:
        avg = (N + 1) / 2


    while (value <= avg):
        i = b
        while (i <= d):
            item_list[a][i] = value
            item_list[c][i] = value
            i+=1

        i = (a + 1)
        while ( i < c):
            item_list[i][b] = value
            item_list[i][d] = value
            i+=1

        value += 1
        a += 1
        b += 1
        c -= 1
        d -= 1

    for item in range(N):
        result = ''
        for item2 in range(N):
            result += " %3i" %item_list[item][item2]
        print(result[1:])
    print("")
