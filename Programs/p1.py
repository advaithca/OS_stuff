import os

r, w = os.pipe()

pid = os.fork()

if pid > 0:
	os.close(r)
	w = os.fdopen(w,'w')
	print("Parent process began.")
	n = int(input("Enter number of entries :: "))
	x  = []
	for i in range(0,n):
		x.append(int(input(f"Entry #{i+1} : ")))
	y = ''
	for z in x:
		y += str(x) + ' '
	os.write(w, y)
	print(f"Parent wrote {x}")
	w.close()
else:
	os.close(w)
	print("Child process began.")
	r = os.fdopen(r)
	print(f"Read {r.read()} from parent")
	r.close()
