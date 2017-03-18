from random import randint
import hashlib
import sys

n = 8 # Length of string to md5()
letter = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789=/+'
letter = list(letter)
print(len(letter))
match = False

def genRandomString(length):
	rs=''
	for i in range(length):
		rs += letter[randint(0,64)]
	return rs	
	
while not match:
	src = genRandomString(n)
	m=hashlib.md5(src.encode()).hexdigest()
	
	if sys.argv[1] is m[:6]:
		print(m ,'|',src,' |Matched!!')
		sys.exit()
	else:
		print(sys.argv[1],'|',m[:6],' |Not match')
