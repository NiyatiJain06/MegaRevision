n = input("Enter a sentence:")
words = n.split()
capitalized_words = [word[0].upper()+word[1:] for word in words if word]
print(" ".join(capitalized_words))