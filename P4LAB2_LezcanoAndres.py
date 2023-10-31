#Andres Felipe Lezcano
#10/31/2023
#Loops

#Get input from the user

num_1 =int(input("Enter an integer: "))
num_2 =int(input("Enter another integer: "))

if num_1 <= num_2:
    for item in range(num_1,num_2 + 1,5):
        print(item)

else:
    print("Rerun the program with the first the smaller") 
