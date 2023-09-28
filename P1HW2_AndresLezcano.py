#Andres Felipe Lezcano
#9/28/2023
#Traveling expenses


budget = int(input("Enter Budget:"))
dest = input("Where are you traveling:")

gas = int(input("Enter gas Budget:"))
food = int(input("Enter food Budget:"))
hotel = int(input("Enter hotel Budget:"))


expenses = gas+food+hotel

print("------------Traveling expenses----------")
print("Location: ", dest)
print("initial Budget", budget)

print()
print("Gas cost", gas)
print("Gas Food", food)
print("Gas Hotel", hotel)
print(budget-expenses)
