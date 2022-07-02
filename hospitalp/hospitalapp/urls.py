from django.urls import path
from .views import About,Home,Contact,Login,Logout,Index,add_appointment,delete_appointment,view_Doctor,delete_Doctor,add_Doctor,add_Patient,view_Patient,delete_Patient, view_appoinment
urlpatterns = [
path('',Home,name="home"),
    path('about/',About,name="about"),
    path('contact/',Contact,name="contact"),
    path('admin_login/',Login,name="admin_login"),
    path('index/',Index,name='dashboard'),
    path('logout/',Logout,name="logout"),
    path('view_doctor/',view_Doctor,name="view_doctor"),
    path('add_doctor/',add_Doctor,name="add_doctor"),
    path('delete_doctor(?p<int:pid>)/',delete_Doctor,name="delete_doctor"),
    path('view_patient/',view_Patient,name="view_patient"),
    path('add_patient/',add_Patient,name="add_patient"),
    path('delete_patient(?p<int:pid>)/',delete_Patient,name="delete_patient"),
    path('view_appointment/',view_appoinment,name="view_appointment"),
    path('add_appointment/',add_appointment,name="add_appointment"),
    path('delete_appointment(?p<int:pid>)/',delete_appointment,name="delete_appointment"),
    
]