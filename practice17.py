class college_student:
    def show_identity(self):
        print("I am a student at TMU")

class AIMLDL_student(college_student):
    def specialization(self):
        print("My focus is AI and ML")

branch=AIMLDL_student()
branch.show_identity()
branch.specialization()        


