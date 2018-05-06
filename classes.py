students = []


class Student:
	#pass #tells the interpreter just to do nothing
	def add_student(self,name, student_id=332):
		student = {"name": name, "student_id": student_id}
		students.append(student)

	
student = Student()
student.add_student("marl")

print(students)
				
#self means the instance of the class  
