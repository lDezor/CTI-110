#Andres Felipe Lezcano 
#10/26/2023
#Branches

employee_name = input("Enter employee's name: \n")
num_employees = 0
total = 0


while employee_name != "Done":

    num_employees = num_employees + 1
    #Get number of hours from user '

    hours_worked = int(input("How many hours did you work?: \n"))

    #Get payrate per hour '

    payrate = float(input("How much you earn per hour?: \n"))

    #Determine if employee worked more than 40 houres '

    if hours_worked > 40:
        overtime =  hours_worked - 40
        regular = 40
        print(f"Overtime Hours:            |{overtime}")
    else:
        overtime = 0
        regular = hours_worked
        print("No overtime")

    ot_pay= overtime * (payrate * 1.5)
    reg_pay= regular * payrate

     #Total of gross pay
    grossPay = reg_pay + ot_pay
    total += grossPay


    #play name, payrate, reg hours, OT hours, OT pay, gross pay.

    print(f"Employee name:             |{employee_name}")

    print(f"Hour worked:               |{hours_worked}")

    print(f"Pay Rate:                  |{payrate}")

    print(f"Overtime Pay:              |{ot_pay}")

    print(f"RegHour Pay:               |{reg_pay}")

    print(f"Gross Pay:                 |{ot_pay + reg_pay}")

    
    employee_name =input("Enter employee's name: \n")


 
print(f'Total of employees entered:      |{num_employees}')
print(f'Total of amount paid in gross:   |{total}')



