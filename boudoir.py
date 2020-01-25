

def boudoir(year=0):
	if year % 4 == 0 and year % 100 > 0:
		print(year, '是閨年')
	else:
		print(year, '是平年')

while True:
	a = input('請輸入年分: ')
	if a == 'q':
		break
	boudoir(int(a))
