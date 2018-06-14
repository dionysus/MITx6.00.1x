testList = open('test', 'w')

def isIn(char, aStr):

	mid = len(aStr)//2
	if len(aStr) < 1:
		return False
	if char == aStr[mid]:
		return True

	if char < aStr[mid]:
		testList.write(aStr[:mid] + '\n')
		return isIn(char, aStr[:mid])
	else:
		testList.write(aStr[mid + 1:]  + '\n')
		return isIn(char, aStr[mid + 1:])

print isIn('f', 'bcdefghijklmnopqrstuv')
testList.close()