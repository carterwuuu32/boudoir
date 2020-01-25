

def is_leap(year=0):
	if year % 4 > 0:
		return False
	elif year % 4 == 0 and year % 100 > 0:
		return True
	elif year % 100 == 0 and year % 400 > 0:
		return False
	elif year % 400 == 0 and year % 3200 > 0:
		return True

while True:
	a = input('請輸入年分:')
	if a == 'q':
		break
	else:
		if is_leap(int(a)):
			print(a, '是閨年')
		else:
			print(a, '是平年')

		
