while True:
    N = int(input())

    if (N == 0):
        break

    item_list =  []

    for item in range(1,(N+1)):
        temp = []
        count = item
        for item2 in range(N):
            temp.append(abs(count))
            if(count == 1):
                count -= 3
            else:
                count -= 1
        item_list.append(temp)

    for row in range(N):
        result = ''
        for col in range(N):
            result += ' %3d' %item_list[row][col]
        print(result[1:])
    print('')
