O = input()
add = 0
top = 10
bottom = 1
count = 0
top_count = top
bottom_count = bottom
temp = 23

for item in range(144):
	N = float(input())

	if(temp > 0):
		temp -= 1
		continue

	if(top_count + bottom_count == 0):
		top -= 1
		bottom += 1
		top_count = top
		bottom_count = bottom

	if (bottom_count > 0):
		bottom_count -= 1
		add += N
		count += 1
		continue

	if (top_count > 0):
		top_count -= 1
		continue


if(O == 'S'):
	print('%.1f' %add)
elif(O == 'M'):
	print('%.1f' %(add/float(count)))
