def add(x,y):
	return x+y

def subtract(x,y):
	return x-y

def multiply(x,y):
	return x*y

def divide(x,y):
	return x/y

print("Select operation :")
print("1.add")
print("2.sub")
print("3.mult")
print("4.div")


while True:
	choice=input("1/2/3/4 : ")
	if choice in ('1','2','3','4'):
		try:
			num1=float(input())
			num2=float(input())
		except ValueError:
			continue
		
		if choice=='1':
			print(add(num1,num2))

		elif choice=='2':
			print(subtract(num1,num2))

		elif choice=='3':
			print(multiply(num1,num2))

		elif choice=='4':
			print(divide(num1,num2))

		n=input("do you want to continue")
		if n=='n':
			break
	else:
		print("invalid")



###### OUTPUT #################
Select operation :
1.add
2.sub
3.mult
4.div
1/2/3/4 : 1
2
3
5.0
do you want to continuey
1/2/3/4 : 2
56
50
6.0
do you want to continuey
1/2/3/4 : 3
4
4
16.0
do you want to continuey
1/2/3/4 : 4
16
5
3.2
do you want to continuen
