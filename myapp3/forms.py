from django import forms
from .models import StudentRegistrationData
from .models import STUDENTMARKSHEETDATA,StudentMarksheetdata2

# class RegistrationForm(forms.Form):

	# username=forms.CharField(max_length=100)
	# Reg_no=models.PositiveIntegerField(max_length=100)
	# dof=models.CharField(max_length=100)
	# Branch=models.CharField(max_length=100)
	# email=forms.CharField(max_length=100)
	# phone=forms.CharField(max_length=100)


# ,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Username'})
		 

# class student_form(forms.ModelForm):
# 	name=forms.CharField(widget=forms.TextInput(),required=True,max_length=100)
# 	emailid=forms.EmailField(widget=forms.EmailInput,required=True,max_length=100)
# 	city=forms.CharField(widget=forms.TextInput(),required=True,max_length=100)
# 	marks=forms.CharField(widget=forms.NumberInput(),required=True,max_length=10)

# 	class Meta():
# 		model=student
# 		fields=['name','emailid','city','marks']
			



class StudentRegistrationForm(forms.Form):

	username=forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'saurabh1','placeholder':'Enter Username111'}))
	dob=forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'saurabh2','placeholder':'DD-MM-YYYY'}))
	reg_no=forms.IntegerField(widget=forms.TextInput(attrs={'class':'saurabh3','placeholder':'Enter registration no.'}))
	email=forms.EmailField(max_length=100,widget=forms.TextInput(attrs={'class':'saurabh4','placeholder':'Enter email id'}))
	mobile=forms.IntegerField(widget=forms.TextInput(attrs={'class':'saurabh5','placeholder':'Enter Mobile no.'}))
	branch=forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'saurabh6','placeholder':'Enter Branch Name'}))
	gender=forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'saurabh7','placeholder':' Enter Gender  Name'}))
	degree=forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'saurabh8','placeholder':'Enter  Degree name'}))



class Meta():
		model=StudentRegistrationData
		fields=['username','dob','reg_no','email','mobile','branch','gender','degree']






class STUDENTMARKSHEETFORM(forms.Form):

	username=forms.CharField()
	dof=forms.DateTimeField()
	reg_no=forms.IntegerField()
	graph_theory=forms.CharField()
	autometa_theory=forms.CharField()
	data_mining=forms.CharField()
	dsp=forms.CharField()
	networking=forms.CharField()
	computer_graphics=forms.CharField()
	grade_S=forms.CharField()
	grade_A=forms.CharField()
	grade_B=forms.CharField()
	grade_C=forms.CharField()
	grade_D=forms.CharField()
	grade_E=forms.CharField()
	grade_U=forms.CharField()
	code_962=forms.IntegerField()
	code_302=forms.IntegerField()
	code_303=forms.IntegerField()
	code_903=forms.IntegerField()
	code_301=forms.IntegerField()
	code_304=forms.IntegerField()
	branch_cse=forms.CharField()
	degree1=forms.CharField()



	class Meta():

		model=STUDENTMARKSHEETDATA

		fields=['username','dof','reg_no','graph_theory','autometa_theory','data_mining','dsp',
		'networking','computer_graphics','grade_S','grade_A','grade_B','grade_C','grade_D',
		'grade_E','grade_U','code_962','code_302','code_303','code_903','code_301','code_304',
		'branch_cse','degree1']



class StudentMarksheetform2(forms.Form):
		subject_code=(

	        (1,'CS101')
	        ,(2,'CS102')
	        ,(3,'CS103')
	        ,(4,'CS104')
	        ,(5,'CS105')
	        ,(6,'CS106')
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

   		
	   
	   


		code_title=forms.TypedChoiceField(choices=subject_code,coerce=int, initial=1
			,widget=forms.TextInput(),required=True)
		grade_title=forms.TypedChoiceField(choices=subject_grade,coerce=int, initial=1,
			widget=forms.TextInput(),required=True)
		student_name=forms.CharField(widget=forms.TextInput(),required=True)
		roll_no=forms.IntegerField(widget=forms.TextInput(),required=True)
		subject_title=forms.TypedChoiceField(choices=subject_name,coerce=int,initial=1,
			widget=forms.TextInput(),required=True)
		Date_of_birth=forms.DateField(required=True,widget=forms.TextInput())
		branch_title=forms.TypedChoiceField(choices=branch_name,coerce=int,initial=1,
			widget=forms.TextInput(),required=True)
		years=forms.TypedChoiceField(choices=year_of_student,coerce=int,initial=1,
			widget=forms.TextInput(),required=True)
		degree_of_student=forms.TypedChoiceField(choices=degree_student,coerce=int,
			widget=forms.TextInput(),initial=1,required=True)

	   	

class Meta():
		model=StudentMarksheetdata2
		fields=['code_title','grade_title','student_name','roll_no','subject_title','Date_of_birth',
		'branch_title','years','degree_of_student']






# class FilterForm(forms.Form):
#     FILTER_CHOICES = (
#         ('time', 'Time'),
#         ('timesince', 'Time Since'),
#         ('timeuntil', 'Time Untill'),
#     )

#     filter_by = forms.ChoiceField(choices = FILTER_CHOICES)