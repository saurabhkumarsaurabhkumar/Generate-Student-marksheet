from django.db import models
# from django.contrib.auth.models import User
# from multiselectfield import MultiSelectField
# autopep8 -i my_file.py



class StudentRegistrationData(models.Model):
	username=models.CharField(max_length=100,null=True)
	dob=models.CharField(max_length=100,null=True)
	reg_no=models.PositiveIntegerField(null=True)
	email=models.EmailField(max_length=100,null=True)
	mobile=models.IntegerField(null=True)
	branch=models.CharField(max_length=100,null=True)
	gender=models.CharField(max_length=100,null=True)
	degree=models.CharField(max_length=100,null=True)
    

	def __str__(self):

		return self.username






class STUDENTMARKSHEETDATA(models.Model):
	username=models.CharField(max_length=100,unique=True)
	dof=models.DateTimeField(max_length=100)
	reg_no=models.IntegerField()
	graph_theory=models.CharField(max_length=100)
	autometa_theory=models.CharField(max_length=100)
	data_mining=models.CharField(max_length=100)
	dsp=models.CharField(max_length=100)
	networking=models.CharField(max_length=100)
	computer_graphics=models.CharField(max_length=100)
	grade_S=models.CharField(max_length=100)
	grade_A=models.CharField(max_length=100)
	grade_B=models.CharField(max_length=100)
	grade_C=models.CharField(max_length=100)
	grade_D=models.CharField(max_length=100)
	grade_E=models.CharField(max_length=100)
	grade_U=models.CharField(max_length=100)
	code_962=models.IntegerField()
	code_302=models.IntegerField()
	code_303=models.IntegerField()
	code_903=models.IntegerField()
	code_301=models.IntegerField()
	code_304=models.IntegerField(unique=True)
	branch_cse=models.CharField(max_length=100,default='', unique=True,null=True)
	degree1=models.CharField(max_length=10,null=True,unique=True)
	

def __str__(self):
	return self.username



class StudentMarksheetdata2(models.Model):
	   	subject_code=(

	        (1,'CS962')
	        ,(2,'CS302')
	        ,(3,'CS303')
	        ,(4,'CS903')
	        ,(5,'CS301')
	        ,(6,'CS304')
	        )
	   	subject_grade=(

	        (1,'S')
	        ,(2,'A')
	        ,(3,'B')
	        ,(4,'C')
	        ,(5,'D')
	        ,(6,'E')
	        ,(7,'U')
	        )
	   	subject_name=(

	        (1,'graph_theory')
	        ,(2,'autometa_theory')
	        ,(3,'data_mining')
	        ,(4,'digital signal processing')
	        ,(5,'networking')
	        ,(6,'computer graphic')
	        
	        )
   		branch_name=(

	        (1,'CSE')
	        ,(2,'ECE')
	        ,(3,'Civil')
	        ,(4,'mechanical')
	        ,(5,'EI')
	        
	        )
   		year_of_student=(

	        (1,'2016-2020')
	        ,(2,'2017-2021')
	        ,(3,'2018-2024')
	        ,(4,'2019-2025')
	        
	        )
   		degree_student=(

	        (1,'B.Tech')
	        ,(2,'M.Tech')
	        ,(3,'PHD')
	        
	        )


	   	code_title=models.IntegerField(choices=subject_code,default='1')
	   	grade_title=models.IntegerField(choices=subject_grade,default='1')
	   	student_name=models.CharField(max_length=100,null=True)
	   	roll_no=models.IntegerField(null=True)
	   	subject_title=models.IntegerField(choices=subject_name,default='1')
	   	date_of_birth=models.DateField(null=True)
	   	branch_title=models.IntegerField(choices=branch_name,default='1')
	   	years=models.IntegerField(choices=year_of_student,default='1')
	   	degree_of_student=models.IntegerField(choices=degree_student,default='1')


	   	def __str__(self):
	   		return self.student_name



           


      