students = []


class Student:
	
	school_name = "Springfield Elementary"
	#pass #tells the interpreter just to do nothing
	def __init__(self,name, student_id=332):
		self.name = name
		self.student_id = student_id
		students.append(self)
				
	def __str__(self):
		return "Student " + self.name

	def get_name_capitalize(self):
		return self.name.capitalize()
		
	def get_school_name(self):
		return self.school_name
	
	
print(Student.school_name)	
	
	
	
# mark = Student("Markooo")	
# print(mark)	
						
						

#print(students)
				
#self means the instance of the class  


