from django.urls import path
from . import views

urlpatterns = [
    path('',views.spinner,name="spinner2"),
    # path('index', views.index,name="index2"),
    path('all_logins/', views.Logins,name="Login2"),
    path('all_logins/login_assistant/',views.login_assistant,name="login_assistant2"),
    path('logout/',views.logout_assistant,name="logout2"),
    path('all_logins/login_assistant/student_registration/',views.student_registration,name="student_registration2"),
    path('all_logins/dean_login/',views.dean_login,name="dean_login2"),
    path('all_logins/hod_login/',views.hod_login,name="hod_login2"),
    path('addUser',views.addUser,name="AddUser2"),
    path('all_logins/login_assistant/marksheet/',views.marksheet,name="marksheet2"),
    path('marksheetdatabase/',views.marksheetdatabase,name="marksheetdatabase2"),


    path('student/',views.student,name="student2"),
    # path('name_of the page',views.name_of_the_page,name="name_of_the_page22"),

   
]
