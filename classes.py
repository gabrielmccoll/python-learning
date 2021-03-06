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
	
	
class HighSchoolStudent(Student): #derived class from parent
	school_name = "Springfield High School"
	
	# method overides
	def get_school_name(self):
		return "This is high school"
	
	def get_name_capitalize(self):
		original_value = super().get_name_capitalize() 
		return original_value + " - HS"


james = HighSchoolStudent("james")
print(james.get_name_capitalize())
