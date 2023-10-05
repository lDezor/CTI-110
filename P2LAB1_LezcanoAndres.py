#Andres Lezcano
#10/3/2023
#Use floats and exprestions to calculate gas cost.

#Creable Variables
mpg = float(input("Enter the car's mpg: "))
cost_per_gallon = float(input("How much does a gallon of gas cost: "))


#Caculate gas cost basef off gallons needed price per gallon
#Calculate for 20 miles,75, 500 miles

cost_20 = (20/mpg) * cost_per_gallon
cost_75 = (75/mpg) * cost_per_gallon
cost_500 = (500/mpg) * cost_per_gallon


#Output values f-string and formt floats
print(f"{cost_20:.2f} {cost_75:.2f} {cost_500:.2f}")
