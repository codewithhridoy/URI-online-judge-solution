O = input()
add = 0
below_dg = 1
above_dg = 11
count = 0
below_dg_count = below_dg
above_dg_count = above_dg


for item in range(144):
	N = float(input())

	if(below_dg_count + above_dg_count == 0):
		below_dg += 1
		above_dg -= 1
		below_dg_count = below_dg
		above_dg_count = above_dg

	if (below_dg_count > 0):
		below_dg_count -= 1
		continue

	if (above_dg_count > 0):
		above_dg_count -= 1
		add += N
		count += 1
		continue

if(O == 'S'):
	print('%.1f' %add)
elif(O == 'M'):
	print('%.1f' %(add/float(count)))
