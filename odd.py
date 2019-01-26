a=input ("enter the no.")
try:
	a=int(a)
	if a%2==0:

		print(a,"is even")

	else:
		print(a,"is odd")
except ValueError:
	print("pls enter no.")

