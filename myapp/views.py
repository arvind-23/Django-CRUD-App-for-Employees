from django.shortcuts import render,HttpResponse,redirect
from myapp.models import Employee
from myapp.form import EmployeeForm


# Create your views here.
def index(request):
    # retrieve all employees object from table
    employees=Employee.objects.all()
 
    #send employees objects list to our templates
    return render(request,'index.html',{'empData':employees})
 
 
#upload
def upload(request):
 
    #to create a empty form
    upload=EmployeeForm()
 
    #code to be executed after form is submitted
    if request.method=='POST':
        upload=EmployeeForm(request.POST,request.FILES)
 
        #if form data is valid , save it to database
 
        if upload.is_valid():
            upload.save()
            return redirect('index')
        else:
            return HttpResponse("<H2 style='color:red'> Form Data is Incorrect </h2>")
 
    else:
        #for request method other than POST, bydefault GET
        return render(request,'EmployeeRegisterForm.html',{'upload_form':upload})
 
 
def update_emp(request,eid):
    eid=int(eid)
 
    try:
        emp_selected=Employee.objects.get(id=eid)
    except Employee.DoesNotExist:
        return redirect('index')
 
    emp_form=EmployeeForm(request.POST or None, instance=emp_selected)
 
    if emp_form.is_valid():
        emp_form.save()
        return redirect('index')
    return render(request,'EmployeeRegisterForm.html',{'upload_form':emp_form})
 
def delete_emp(request,eid):
    eid=int(eid)
 
    try:
        emp_selected=Employee.objects.get(id=eid)
    except Employee.DoesNotExist:
        return redirect('index')
 
    emp_selected.delete()
    return redirect('index')