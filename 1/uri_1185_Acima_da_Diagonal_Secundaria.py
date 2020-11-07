O = input()
add = 0
bottom = 1
top = 11
count = 0
bottom_count = bottom
top_count = top

for item in range(144):
	N = float(input())

	if (top_count > 0):
		top_count -= 1
		add += N
		count += 1
		continue

	if (bottom_count > 0):
		bottom_count -= 1
		continue

	if(bottom_count + top_count == 0):
		bottom += 1
		top -= 1
		bottom_count = bottom
		top_count = top

if(O == 'S'):
	print('%.1f' %add)
elif(O == 'M'):
	print('%.1f' %(add/float(count)))
