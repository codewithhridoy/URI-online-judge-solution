O = input()
add = 0
white = 9
green = 2

count = 0
white_count = white
green_count = green

for item in range(144):
	N = float(input())

	if item < 89:
		continue

	if(white_count + entra == 0):
		white -= 2
		green += 2
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

if(O == 'S'):
	print('%.1f' %add)
elif(O == 'M'):
	print('%.1f' %(add/float(count)))
