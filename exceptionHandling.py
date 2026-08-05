a =input("Enter the number:")
print("Multiplication table of is:",a)

try:
   for i in range(1, 11):
    print(f"{int(a)} x {i}={int(a)*i}")
except Exception as e:
  print(e)
   
print("Some impotant lines of code ")
print("End of program.")