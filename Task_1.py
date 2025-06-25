# Create a Dictionary of Student Marks

students={'Alice':80,'Mike':90,'Sam':85,'Nick':95}
a=input("Enter the student's name: ")
marks=students.get(a)
marks=str(marks)
if(a in students):
    print(a+"'s"+' marks: '+marks)
else:
    print("Student not found.")