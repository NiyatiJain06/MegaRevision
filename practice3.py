# write a program to take two number to a user 
# do addition, subtraction, multipication, division
# and convert value in float
# division wrap with round(result/2)

num1 = int(input("Enter the value:"))
num2 = int(input("Enter the value:"))
sum = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2
div_round1 = round(num1/2)
div_round2 = round(num2/2)
print(sum)
print(subtraction)
print(multiplication)
print(div_round1)
print(div_round2)
convertedValue1 = float(num1)
convertedValue2 = float(num2)
print("Converted Value of num1 is:", convertedValue1)
print("Converted Value of num2 is:", convertedValue2)

