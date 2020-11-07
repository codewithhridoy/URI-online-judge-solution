O = input()
add = 0
white = 10
green = 1
max = False

count = 0
white_count = white
green_count = green


for item in range(144):
	N = float(input())

	if(item < 23):
		continue

	if (max):
		if(white_count + green_count == 0):
			white += 1
			green -= 1

			if(item == 79):
				green = 5

			white_count = white
			green_count = green

		if (green_count > 0):
			green_count -= 1
			add += N
			count += 1
			continue

		if (white_count > 0):
			white_count -= 1
			continue

		break
	else:
		if(white_count + green_count == 0):
			white -= 1
			green += 1
			white_count = white
			green_count = green

		if (green_count > 0):
			if(green_count == 5):
				max = True
				green = 5
				white = 7
				white_count = white

			green_count -= 1
			add += N
			count += 1
			continue

		if (white_count > 0):
			white_count -= 1
			continue

if(O == 'S'):
	print('%.1f' %add)
elif(O == 'M'):
	print('%.1f' %(add/float(count)))
