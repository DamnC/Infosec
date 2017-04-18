from itertools import takewhile
from math import floor, sqrt
import subprocess
from time import gmtime, strftime
import sys

def _prime_numbers_helper():
    yield 2
    yield 3
    i = 1
    while True:
        yield 6 * i - 1
        yield 6 * i + 1
        i += 1

def prime_numbers(ceiling=None):
    if ceiling is None:
	for x in _prime_numbers_helper():
		yield x
    else:
        for y in takewhile(lambda number: number <= ceiling, _prime_numbers_helper()):
		yield y

def largest_prime_factor(number):
    if number < 2:
	return 0

    if number % int(number) != 0:
        raise ValueError('The number must be an integer.')

    while True:
        for i in prime_numbers(floor(sqrt(abs(number)))):
            if number % i == 0:
                number //= i
                break
        else:
            return number

to_check = range(-5, 1000)
to_check.append(sys.maxint)
to_check.append(-sys.maxint - 1)
error = False
for i in to_check:
	if error:	
		break
	p = subprocess.Popen(["./q1", str(i)], stdout=subprocess.PIPE)
	while True:
		ln = p.stdout.readline()

		if '' == ln:
			break

		c_result = int(ln)
		p_result = largest_prime_factor(i)
		print "i=%d \t largest prime factor: %d" % (i, c_result)
		if c_result != p_result:
			print "ERROR!!"
			error = True
			break

if not error:
	print "you deserve a cookie!"