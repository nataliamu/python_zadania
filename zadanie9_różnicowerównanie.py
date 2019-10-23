print("podaj a")
a= int (input())
print("podaj b")
b= int (input())
print("podaj c")
c= int (input())
d = b**2 - 4*a*c

if d >= 0 :
	e = d**0.5	
	if (b-e/2*a) == (b+e/2*a):
		print("x0=" + str(b-e/2*a))
	else :	
		print("x1=" + str(b+e/2*a))
		print("x2=" + str(b-e/2*a))
else:
	print("delta ujemna")
