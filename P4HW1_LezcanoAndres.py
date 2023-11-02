# Andres Lezcano
# 10/10/2023
# Working with list

num_grades =int(input("How many grades will you enter: "))

grade_list =[]
                      
for grade in range (num_grades):
    this_grade =int(input("Enter a grade: "))

    while this_grade < 0 or this_grade > 100:
        print("Invalid grade entered.")
        this_grade = int(input("Enter a grade: "))

    grade_list.append(this_grade)
    print(f'{this_grade} has been added to the list')

for grade in grade_list:
    print(grade)

# Calcule min/max/sum/ average and assingn to variables
max_value = max(grade_list)
min_value = min(grade_list)
suma = sum(grade_list)
final_grade =(sum(grade_list)/len(grade_list))

#Show to the user
print(f"Your Highest grade:    |{max_value}")
print(f"Your Lowest grade:     |{min_value}")
print(f"Sum of Grades:         |{suma}")
print(f"Final Grade:           |{final_grade}")

if  final_grade > 60:
    print("Good Job"," \N{grinning face}")
else:
    print("Better next time","\U0001f614")
   
 
