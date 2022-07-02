from email.headerregistry import Address
from pydoc import Doc
import re
from django.shortcuts import redirect,render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from .models import Doctor, Patient,Appointment

# Create your views here.
def About(request):
	return render(request,'about.html')
def Home(request):
	return render(request,'home.html')
def Contact(request):
	return render(request,'contact.html')
def Index(request):
	if not request.user.is_staff:
		return redirect('login')
	doctor=Doctor.objects.all()
	patient=Patient.objects.all()
	appointement=Appointment.objects.all()
	d=p=a=0
	for i in doctor:
		d+=1
	for i in patient:
		p+=1
	for i in appointement:
		a+=1
	dict1={'d':d,'p':p,'a':a}
	return render(request,'index.html',dict1)

def Login(request): 
	error = ""
	if request.method=="POST":
		U=request.POST['uname']
		P=request.POST['pwd']
		user=authenticate(username=U,password=P)
		try:
			if user.is_staff:
				login(request,user)
				error = "no"
			else:
				error = "yes"
		except:
			error = "yes"
	d={'error': error}
	return render(request,'login.html',d)

def Logout(request):
	if not request.user.is_staff:
		return redirect('login')
	else:
		logout(request)
		return redirect('home')

#DOCTOR
def view_Doctor(request):
	if not request.user.is_staff:
		return redirect('login')
	doc=Doctor.objects.all()
	return render(request,"view_doctor.html",{"doc":doc})

def delete_Doctor(request,pid):
	if not request.user.is_staff:
		return redirect('login')
	doctor=Doctor.objects.get(id=pid)
	doctor.delete()
	return redirect("view_doctor")

def add_Doctor(request):
	error = ""
	if not request.user.is_staff:
		return redirect("login")
	if request.method=="POST":
		n=request.POST['uname']
		m=request.POST['mob']
		sp=request.POST['spe']
		try:
			Doctor.objects.create(Name=n,Mobile=m,Special=sp)
			error="no"
		except:
			error = "yes"
	d={'error': error}
	return render(request,'add_doctor.html',d)

#PATIENT 
def view_Patient(request):
	if not request.user.is_staff:
		return redirect('login')
	pat=Patient.objects.all()
	return render(request,"view_patient.html",{"patient":pat})

def delete_Patient(request,pid):
	if not request.user.is_staff:
		return redirect('login')
	pat=Patient.objects.get(id=pid)
	pat.delete()
	return redirect("view_patient")

def add_Patient(request):
	error = ""
	if not request.user.is_staff:
		return redirect("login")
	if request.method=="POST":
		n=request.POST['uname']
		g=request.POST['gdr']
		m=request.POST['mob']
		addr=request.POST['add']
		try:
			Patient.objects.create(Name=n,Gender=g,Mobile=m,Address=addr)
			error="no"
		except:
			error = "yes"
	d={'error': error}
	return render(request,'add_patient.html',d)

def add_appointment(request):
	error = ""
	doctor1=Doctor.objects.all()
	patient1=Patient.objects.all()
	if not request.user.is_staff:
		return redirect("login")
	if request.method=="POST":
		n=request.POST['doctor']
		p=request.POST['patient']
		d=request.POST['date']
		t=request.POST['time']
		doctor=Doctor.objects.filter(Name=n).first()
		patient=Patient.objects.filter(Name=p).first()
		try:
			Appointment.objects.create(doctor=doctor,patient=patient,Date=d,Time=t)
			error="no"
		except:
			error = "yes"
	d={'error': error,'doctor':doctor1,'patient':patient1}
	return render(request,'add_appointment.html',d)
 
def view_appoinment(request):
	if not request.user.is_staff:
		return redirect('login')
	app=Appointment.objects.all()
	return render(request,"view_appointment.html",{"appoinment":app})

def delete_appointment(request,pid):
	if not request.user.is_staff:
		return redirect('login')
	app=Appointment.objects.get(id=pid)
	app.delete()
	return redirect("view_appointment")	
	


