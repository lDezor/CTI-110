#Andres Felipe Lezcano
#11/14/2003
#We are working with if/esle statements

def get_year():
    year = int(input("Enter a year to dertermine if its a leap year: "))
    return  year

def divide_by_4(year):
    if year % 4 == 0:
        return True
    else:
        return False

def divide_by_100(year):
    if year % 100== 0:
        return True
    else:
        return False

def divide_by_400(year):
    if year % 400 == 0:
        return True
    else:
        return False

def output_results(is_leap, year):
    if is_leap == True:
        print(f"The year {year} is a leap year")
    else:
        print(f"The year {year} is NOT a leap year")


def main():
    is_leap= False               #A boolean variable
    year = get_year()
    
    if divide_by_4(year):           #Does year divide by 4/100/400
         if divide_by_100(year):
            if divide_by_400(year):
                is_leap = True
            else:
             is_leap = False        #Does not divide by 400
         else:
          is_leap = True         #Does not divide by 100
    else:
      is_leap = False         #Does not divide by 4
     
    #Print output to user
    output_results(is_leap, year)
    

#Call the main fuction
main()


            
