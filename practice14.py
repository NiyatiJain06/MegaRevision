my_skills = {
    "Primary":"Python",
    "Secondary":"Blockchain"
}
print(my_skills)
try:
    print(my_skills["ternary"])

except:
    print("Skill not found, but don't worry, Niyati is still learning!")

finally:
    print("Search Completed")