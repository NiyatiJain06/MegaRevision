print("Prime numbers between 1 and 100:")
for num in range(2,101):
    is_prime = True
    for i in range(2,int(num**0.5)+1):
        if num % 1 == 0:
            is_prime = False
            
    if is_prime:
        print(num)
print()            
