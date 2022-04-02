# Parent sends n numbers to child

import os

r, w = os.pipe()
pid = os.fork()

if pid:
	os.close(r)
	w = os.fdopen(w,'w')
	x = []
	n = int(input("Enter value of n : "))
	print(f"Enter {n} numbers :")
	for i in range(0,n):
		x.append(int(input(f"Entry #{i+1} : ")))
	w.write(str(x))
	print(f"Parent wrote : {x}")
	w.close()
else:
	os.close(w)
	r = os.fdopen(r)
	y = r.read()
	y = y.split(", ")
	print(f"Child read :")
	for z in y:
		s = ''
		for i in z:
			if i not in '[]':
				s += i
		print(int(s))
	r.close()
