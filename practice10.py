# You are given a list of programming languages:
# ["Python", "Java", "C++", "Python", "Java", C"]
# Convert it into a set and print how many unique language You knows.

programmingList = ["Python", "Java", "C++", "Python", "Java", "C"]
print(programmingList)
print(type(programmingList))
 # how to convert a list into set

programmingSet = set(programmingList)
print(type(programmingSet))
print(programmingSet)
print("Enter the unique languages you know:",len(programmingSet))