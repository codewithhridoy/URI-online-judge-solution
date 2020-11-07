O = input()
add = 0
white = 12
green = 0
max = False

count = 0
white_count = white
green_count = green


for item in range(144):
	N = float(input())

	if (max):
		if(white_count + entra == 0):
			white += 1
			green -= 1
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
	else:
		if(white_count + green_count == 0):
			white -= 1
			green += 1
			white_count = white
			green_count = green

		if (green_count > 0):
			if(green_count == 6):
				max = True
				green_count -= 1
				white_count += 1
				green -= 1
				white += 1

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
