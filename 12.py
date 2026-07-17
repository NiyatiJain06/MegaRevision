n = input("Enter a string:")
n=n.lower()
if n == n[::-1]:
    print("It is a Palindrome")
else:
    print("Not a Palindrome")    