#Andres Felipe Lezcano
# 10/5/2023
# How to make a dictionary

name = input("Enter your name: ")
hair = input("Enter your hair color: ")
eye = input("Enter your eye color: ")
height = float(input("Enter height as a decimal: "))
age = int(input("Enter your age: "))
food = input("Enter your favorite food?: ")

# Create a dictionary
my_dict = {"Name": name, "Hair_Color": hair, "Eye_Color": eye,      \
           "Height": height, "Age": age, "Food": food}

#Get values using the key
print(f" {my_dict['Name']} is a person that has a  {my_dict['Hair_Color']} hair, he is {my_dict['Height']}  tall student, he also has  {my_dict['Eye_Color']} eyes and his favorite food is {my_dict['Age']} {my_dict['Food']}")
