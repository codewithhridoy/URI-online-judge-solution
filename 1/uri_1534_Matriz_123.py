while True:
    try:
        N = int(input())

        item_list = []

        col2 = N - 1
        for item in range(N):
            temp = []
            for item2 in range(N):
                if(item2 == col2):
                    temp.append(2)
                    col2 -= 1
                else:
                    if(item == item2):
                        temp.append(1)
                    else:
                        temp.append(3)
            item_list.append(temp)

        for row in range(N):
            result = ''
            for col in range(N):
                result += str(item_list[row][col])
            print(result)
    except EOFError:
        break
