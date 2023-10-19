#Andres Felipe Lezcano
#10/19/2003
#We are working with if/esle statements 


#Create a boolean variable to hold leap year status

is_leap= False

#Get year from user
year = int(input("Enter a year to dertermine if its a leap year: "))

#Does year divide by 4/100/400
if year % 4 == 0:
    if year % 100== 0:
        if year % 400 == 0:
            is_leap = True
        else:
         is_leap = False    #Does not divide by 400
    else:
      is_leap = True      #Does not divide by 100
else:
  is_leap = False         #Does not divide by 4
 
#Print output to user
if is_leap == True:
 print(f"The year {year} is a leap year")
else:
    print(f"The year {year} is NOT a leap year")
        
