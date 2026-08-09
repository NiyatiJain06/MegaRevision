# write a python program takes a CGPA as input and count Backlogs

CGPA = float(input("Enter your CGPA:"))
Backlogs = int(input("Enter the number of Backlogs:"))

if CGPA >=  7.0 and Backlogs == 0:
 
    print("Congrates! you are eligible for the interview.")

elif CGPA < 7.0:
    print("Focus on your CGPA first") 

elif Backlogs > 0:
    print("Clear your Backlogs to sit in placements.")

