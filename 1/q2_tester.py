from math import sqrt
import subprocess

def F(n):
	if n <= 0:
		return 0
	return int(((1+sqrt(5))**n-(1-sqrt(5))**n)/(2**n*sqrt(5)))

error = False
for i in range(-5, 40):
	if error:	
		break
	p = subprocess.Popen(["./q2a", str(i)], stdout=subprocess.PIPE)
	while True:
		ln = p.stdout.readline()

		if '' == ln:
			break

		c_result = int(ln)
		p_result = F(i)
		print "i=%d \t fib num: %d" % (i, c_result)
		if c_result != p_result:
			print "q2a ERROR!! py: %d" % p_result
			error = True
			break
if not error:
	print "q2a is OK! you deserve a cookie!"

error = False
for i in range(-5, 40):
	if error:	
		break
	p = subprocess.Popen(["./q2b", str(i)], stdout=subprocess.PIPE)
	while True:
		ln = p.stdout.readline()

		if '' == ln:
			break

		c_result = int(ln)
		p_result = F(i)
		print "i=%d \t fib num: %d" % (i, c_result)
		if c_result != p_result:
			print "q2b ERROR!! py: %d" % p_result
			error = True
			break
if not error:
	print "q2b is OK! you deserve a cookie!"