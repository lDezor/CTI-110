# Andres Lezcano
# 10/10/2023
# Working with list 

# Create variables
module1 = int(input("Enter your grade for module 1: "))
module2 = int(input("Enter your grade for module 2: "))
module3 = int(input("Enter your grade for module 3: "))
module4 = int(input("Enter your grade for module 4: "))
module5 = int(input("Enter your grade for module 5: "))
module6 = int(input("Enter your grade for module 6: "))

#Create empty list
#Example_list(module1, module2, module3, module4, module5, module6)
module_list = [ ]

# Add a list
module_list.append(module1)
module_list.append(module2)
module_list.append(module3)
module_list.append(module4)
module_list.append(module5)
module_list.append(module6)

# Calcule min/max/sum/ average and assingn to variables
max_value = max(module_list)
min_value = min(module_list)
suma = sum(module_list)
final_grade =(sum(module_list)/len(module_list))

#Show to the user
print("Your Highest grade: ", max_value)
print("Your Lowest grade:" ,min_value)
print("Sum of Grades: ", suma)
print("Final Grade: ", final_grade)
