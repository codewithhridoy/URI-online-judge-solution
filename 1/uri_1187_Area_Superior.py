O = input()
add = 0
other = 1
top = 10

count = 0
other_count = other
top_count = top

for item in range(144):
	N = float(input())

	if(other_count + top_count == 0):
		other += 2
		top -= 2
		other_count = other
		top_count = top

	if (other_count > 0):
		other_count -= 1
		continue

	if (top_count > 0):
		top_count -= 1
		add += N
		count += 1
		continue

if(O == 'S'):
	print('%.1f' %add)
elif(O == 'M'):
	print('%.1f' %(add/float(count)))
