#Andres Felipe Lezcano
#11/16/2023
#Using if/esle, loop, fuctions, and ramdon numbers.

import random

def show_menu():
    print("Welcome to the Match Quiz")
    print("Main Menu")
    print("-----------------")
    print("1 Adding Ramdon Numbers ")
    print("2 Subtrating Ramdon Numbers ")
    print("3 Exit Program")

def adding ():
     num1=random.randint(0,10)
     num2=random.randint(0,10)
     print(num1, "+" , num2)
     my_sum = num1 + num2
     #print("The suum is", my_sum)
     return my_sum

def subtacting ():
     num1=random.randint(0,10)
     num2=random.randint(0,10)
     print(num1, "-" , num2)
     my_diff = num1 - num2
     #print("The difference is", my_diff)
     return my_diff
     guessing (guess, value)

def guessing(guess, value):
    num_guesses = 0
    while guess != value:
        num_guesses += 1
        if guess > value:
            print("Your guess is too high")
            guess= int(input("Guess "))
        else:
            print("Your guess is too low")
            guess =int(input("Guess "))

    print("Congratulations, your guess is correct")
    print("It took you",num_guesses, "to get it rigth.")
    
#Main function that runs the program
     
     
def main():
    
    while True:
        show_menu()
        user_choice =int(input("Please choose one of the menu options : "))
        if user_choice == 1:
             value = adding() 
             guess= int(input("Guess "))
             guessing(guess, value)
             
        if user_choice == 2:
             value = subtacting()
             guess= int(input("Guess "))
             guessing(guess, value)
             
        if user_choice == 3:
            print("The program has ended")
            break
        
#Call the main function 
if __name__ == "__main__":
    main()

    


