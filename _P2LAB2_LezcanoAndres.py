# Andres Felipe Lezcano
# 10/5/2023
#  Formating floats


# Get float from user
num1 = float(input("Paint: "))
num2 = float(input("Wall Area: "))
num3 = float(input("Gallons: "))
num4 = float(input("Cost: "))

product = num1 * num2 * num3* num4
average = (num1 + num2 + num3 + num4)/4 

# Display values with f-string
print(f"Wall area {average}  sq ft")

# Display Product and average with 0 places
print(f" {product:.0f} {average:.0f}")

# Display with 3 places
print(f" {product:.3f} {average:.3f}")
