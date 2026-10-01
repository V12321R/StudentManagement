def add_stu(students, stu):
	detail=input("Enter detail:")
	students[stu]=detail
	print("New student in student list:",students)
def display_stu(students, stu):
	print(students[stu])
def search_stu(students, stu):
	for i in students:
		if i==stu:
			print("Student found")
		else:
			print("Student NOT found")
def del_stu(students, stu):
	students.pop(stu)
	print("Reflected:", students)



students={"sample":"details"}
while True:
	stu=input("Enter student name:")
	ch=int(input("Choose an action: 1. Add student, 2. Display student details, 3. Search for a student, 4. Delete a student's record:"))
	if ch==1:
		add_stu(students, stu)
	if ch==2:
		display_stu(students, stu)
	if ch==3:
		search_stu(students, stu)
	if ch==4:
		del_stu(students, stu)
	w=input("Continue? Y/N:")
	if w.lower()=="n":
		break

