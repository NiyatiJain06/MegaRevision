my_profile = {
    "name":"Sparsh",
    "internship":"Google",
    "favLanguage":"Python",
    "age":20
}
print(my_profile)
print(my_profile["name"])
my_profile["status"]="Learning"
print(my_profile)
my_profile["age"]=21
print(my_profile)

print("\n----My Profile Keys----")
for x in my_profile.keys():
    print(x)

print("\n----My Profile Details----")
for k, v in my_profile.items():
    print(k, ":", v)