import os
import math
import numpy as np

r, w = os.pipe()
r1, w1 = os.pipe()

pid = os.fork()

def isprime(num):
    a=2
    while a<=math.sqrt(num):
        if num%a<1:
            return False
        a=a+1
    return num>1

if pid:
	os.close(r)
	os.close(w1)
	w = os.fdopen(w, 'w')
	n = int(input("Parent >> Enter value of n : "))
	x = []
	print(f"Parent >> Enter {n} numbers")
	for i in range(0,n):
		x.append(int(input(f"#{i+1} : ")))
	z = np.array(x)
	y = str(z)
	w.write(y)
	print("Parent >> Sent the numbers to child.")
	w.close()
	r1 = os.fdopen(r1)
	s = r1.read()
	if s:
		print("Parent >> Prime numbers are : ")
		print(s)
	r1.close()

else :
	os.close(w)
	os.close(r1)
	r = os.fdopen(r)
	nums = r.read()
	d = ''
	for i in nums:
		for j in i:
			if j not in '[]':
				d += j
	arr = []
	for z in d.split(' '):
		if z != '':
			if isprime(int(z)):
				arr.append(int(z))
	r.close()
	w1 = os.fdopen(w1,'w')
	primes = str(arr)
	if primes != '[]':
		w1.write(primes)
		print('Child >> Sent Primes to parent.')
	else:
		print('Child >> No prime numbers to send.')
	w1.close()
