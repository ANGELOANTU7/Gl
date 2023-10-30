low=100
medium=200
medium_high=300
high=350

low_rate=1.5
medium_rate=2
medium_high_rate=2.5
high_rate=3



def main():
	while(True):
		units=int(input("Units consumed per month :"))
		if(units<=low):
		    payAmount=units*low_rate
		    fixedcharge=25.00
		elif(units<=medium):
		    payAmount=(low*low_rate)+(units-low)*medium_rate
		    fixedcharge=50.00
		elif(units<=medium_high):
		    payAmount=(low*low_rate)+(medium-low)*medium_rate+(units-medium)*medium_high_rate
		    fixedcharge=75.00
		elif(units<=high):
		    payAmount=(low*low_rate)+(medium-low)*medium_rate+(medium_high-medium)*medium_high_rate+(units-medium_high)*high_rate
		    fixedcharge=100.00
		else:
		    payAmount=0
		    fixedcharge=1500.00

		Total=payAmount+fixedcharge;
		print("\nElecticity bill=%.2f" %Total)

main()
