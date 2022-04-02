# Parent sends string to child, child says if it is palindrome or not

import os

def palindrome(text):
	return text == text[::-1]

r, w = os.pipe()
r1, w1 = os.pipe()
 
pid = os.fork()

if pid:
	os.close(r)
	os.close(w1)
	w = os.fdopen(w, 'w')
	string = str(input("Parent >> Enter a string : "))
	w.write(string)
	print("Parent >> String sent to child.")
	w.close()
	r1 = os.fdopen(r1)
	s = r1.read()
	if s == 'True':
		print("Parent >> It is a palindrome.")
	else:
		print("Parent >> It is not a palindrome.")
	r1.close()

else:
	os.close(w)
	os.close(r1)
	r = os.fdopen(r)
	s = r.read()
	print("Child  >> Received string from parent.")
	r.close()
	w1 = os.fdopen(w1,'w')
	w1.write(str(palindrome(s)))
	print("Child  >> Sent result to parent.")
	w1.close()
