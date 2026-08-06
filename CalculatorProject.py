# Mini Calculator Project using function

def addFunc(a, b): 
    print (f"Result: {a+b}")

def subFunc(a, b):
    print(f"Result: {a-b}")

def multiFunc(a, b):
    print(f"Result: {a*b}")

# Get user Input

print("____My Mini Calculator____")
num1 = float(input("Enter the first Value:"))
num2 = float(input("Enter the second value"))
 
print("Choose Operation: 1.Add,  2.Subtarct, 3.Multiply")
choice = input("Enter 1, 2, or 3:")

# Decision Making (The Logic)

if choice == '1':
    addFunc(num1, num2)

elif choice == '2':
    subFunc(num1, num2)

elif choice == '3':
    multiFunc(num1, num2)

else:
    print("Invalid choice! Please run again.")        
    