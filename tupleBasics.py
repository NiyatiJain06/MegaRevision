 # tuple Basice program

myTuple = (78, 90, 75)
studentTuple = ("Niyati", "Mahi", "Sparsh","Mahi")
print(studentTuple)
print(myTuple)

# studentTuple[1] = "Vinita" Tuples are IMMUTABLE/NOT Changeable

print(studentTuple[2])

#empty Tuple
emptyTuple = ()
singleTuple = (1,)
print(type(emptyTuple))
print(type(studentTuple))
print(type(singleTuple))
print(singleTuple)
print(studentTuple.index("Mahi"))
print(studentTuple.count("Mahi"))