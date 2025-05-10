from django.shortcuts import render
from app1.models import student

def main(request):
    return render(request, 'app1/main.html')
def at(request):
    return render(request, 'app1/add.html')
def adding(request):
    msg=''
    sno=request.GET['rollno']
    sname=request.GET['name'] 
    sub1=request.GET['sub1']
    sub2=request.GET['sub2']
    if sno and sname and sub1 and sub2:
        s = student(sno=sno, sname=sname, sub1=sub1, sub2=sub2)
        s.save()
        msg = 'Data added!!'
    else:
        msg = 'Please fill in all fields.'
    return render(request,'app1/add.html',context={'msg':msg})
def um(request):
    return render(request, 'app1/up.html')
def update(request):
    msg=''
    sno=request.GET['rollno']
    sub1=request.GET['sub1']
    sub2=request.GET['sub2']
    try:
        u=student.objects.get(sno=sno)
        u.sub1=sub1
        u.sub2=sub2
        u.save()
        msg = 'Data updated!!'
    except student.DoesNotExist:
        msg = 'Student not found.'
    return render(request,'app1/up.html',context={'msg':msg})
def fr(request):
    return render(request, 'app1/find.html')
def find(request):
    sno=request.GET['rollno']
    r=''
    try:
        s=student.objects.get(sno=sno)
        r='pass' if int(s.sub1)>35 and int(s.sub2>35) else 'fail'
    except student.DoesNotExist:
        r='Enter a valid number!!'
    return render(request,'app1/find.html',context={'msg':r})
def d(request):
    return render(request, 'app1/delete.html')
def delete(request):
    msg = ''
    if 'rollno' in request.GET:
        sno = request.GET['rollno']
        print(f"Received rollno: {sno}")
        try:
            s = student.objects.get(sno=sno)
            s.delete()
            msg = 'Deleted Successfully'
        except student.DoesNotExist:
            msg = 'Enter a valid roll number!!'
    else:
        msg = 'No roll number provided!'
    return render(request, 'app1/delete.html', context={'msg': msg})
def viewstudent(request):
    qs = student.objects.all()
    return render(request, 'app1/vs.html', context={'qs': qs})
