my_skills1 = input("Enter skill 1:")
my_skills2 = input("Enter skill 2:")
my_skills3 = input("Enter skill 3:")
my_skills4 = input("Enter skill 4:")

my_skillsList = []
my_skillsList.append(my_skills1)
my_skillsList.append(my_skills2)
my_skillsList.append(my_skills3)
my_skillsList.append(my_skills4)

print(my_skillsList)
print("____Skill Search Portal____")
search_skill = input("Enter the skill you want to search:")

if search_skill in my_skillsList:
    print("you already have this skill!")
else:
    print("Time to add this to your roadmap!")


