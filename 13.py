s = input("Enter a sentence:")
s = s.lower()
vowels = "aeiou"
count = sum(1 for char in s if char in vowels)
print("Number of vowels:",count)
