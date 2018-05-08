from student import Student
class HighSchoolStudent(Student): #derived class from parent
	school_name = "Springfield High School"
	
	# method overides
	def get_school_name(self):
		return "This is high school"
	
	def get_name_capitalize(self):
		original_value = super().get_name_capitalize() 
		return original_value + " - HS"
