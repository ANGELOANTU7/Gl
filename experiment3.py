

import math



def equationroots( a, b, c):
	dis = b * b - 4 * a * c
	sqrt_val = math.sqrt(abs(dis))

	if dis > 0:
		print("real and different roots")
		print((-b+sqrt_val)/(2*a))
		print((-b-sqrt_val)/(2*a))
	elif dis == 0:
		print("real and same roots")
		print(-b / (2 * a))
	else:
		print("Complex Roots")
		print(-b/(2*a), "+ i", sqrt_val)
		print(-b/(2*a),"- i", sqrt_val)



def main():
	while(True):
		p2=int(input("x^2"))
		p1=int(input("x"))
		p0=int(input("*1"))
		if(p2!=0):
			equationroots(p2,p1,p0)
		else:
			print("incorrect values")
main()
