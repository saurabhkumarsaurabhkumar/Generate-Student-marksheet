from django.shortcuts import render,redirect
from django.contrib.auth import (login as auth_login,  authenticate,logout)
from django.contrib import messages
from django.contrib.auth.models import User,auth
from .forms import StudentRegistrationForm,STUDENTMARKSHEETFORM
from .models import StudentRegistrationData,STUDENTMARKSHEETDATA
from .forms import StudentMarksheetform2
# from .models import StudentMarksheetdata2
# from .forms import FilterForm
 

def spinner(request):
    return render(request,'spinner.html')


# def index(request):
# 	return render(request,'index.html')

def Logins(request):
	return render(request,'all_logins.html')



def login_assistant(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
                auth.login(request, user)
                return redirect('login_assistant2')
                messages.info(request,' Login Successefully')
        else:
                messages.info(request,'Your account is not activated')
                return redirect("Login2")
        
    context = {'message': messages}
    return render(request, 'assistant_login.html', context)

def dean_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
                auth.login(request, user)
                return redirect('login_assistant2')
                messages.info(request,' Login Successefully')
        else:
                messages.info(request,'Your account is not activated')
                return redirect('dean_login2')
        
    context = {'message': messages}
    return render(request, 'dean_login.html', context)

def hod_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
                auth.login(request, user)
                return redirect('login_assistant2')
                messages.info(request,' Login Successefully')
        else:
                messages.info(request,'Your account is not activated')
                return redirect('hod_login2')
        
    context = {'message': messages}
    return render(request, 'hod_login.html', context)



def logout_assistant(request):
    logout(request)
    messages.success(request,('You Have Been Logout....'))
    return redirect('Login2')







def student_registration(request):

        context={"form":StudentRegistrationForm}
        return render(request,'student_registration.html',context)
        

def addUser(request):
    form = StudentRegistrationForm(request.POST)

    if request.method == "POST" and form.is_valid():
        register=StudentRegistrationData(username=request.POST['username'],
        dob=request.POST['dob'],
        reg_no=request.POST['reg_no'],
        email=request.POST['email'],
        mobile=request.POST['mobile'],
        branch=request.POST['branch'],
        gender=request.POST['gender'],
        degree=request.POST['degree'])
        register.save()
        # messages.success(request,('you have been Successefully Register....'))
    return render(request,'assistant_login.html')





def marksheet(request):
    return render(request,'marksheet.html')





def marksheetdatabase(request):
    # form = STUDENTMARKSHEETFORM(request.POST)
    obj=STUDENTMARKSHEETDATA.objects.all()
    return render(request,'marksheetdatabase.html',{'obj1':obj})






# def studentmarksheet2(request):
#     context1={"form1":StudentMarksheetform2}
#     return render(request,'nitstudentmarksheet.html',context1)

# def Addstudentmarksheet2(request):
#     form1=StudentMarksheetform2(request.POST)
#     if request.method=="POST" and form.is_valid():
#         marksheet=StudentMarksheetdata2(code_title=request.POST['code_title']
#         ,grade_title=request.POST['grade_title'],student_name=request.POST['student_name']
#         ,roll_no=request.POST['roll_no'],subject_title=request.POST['subject_title']
#         ,Date_of_birth=request.POST['Date_of_birth'],branch_title=request.POST['branch_title']
#         ,years=request.POST['years'],degree_of_student=request.POST['degree_of_student'])

#         marksheet.save()

#     return render(request,'assistant_login.html')
            



def student(request):
    if request.method=='POST':
        form1=StudentMarksheetform2(request.post)
        # Date_of_birth=''
        if form1.is_valid():
            # answer = request.GET['dropdown'] 
            # Date_of_birth=form1.clean_data.get['Birthday_day']
            form1.save()
            return redirect('student2')
    else:
        form1=StudentMarksheetform2()
    return render(request,'nitstudentmarksheet.html',{'form2':form1})





# def name_of_the_page(request):
#  form = FilterForm(request.POST or None)
#  answer = ''
#  if form.is_valid():
#   answer = form.cleaned_data.get('filter_by') 

            

