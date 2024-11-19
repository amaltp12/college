from django.shortcuts import render,redirect
from newapp.models import Department,User,Teacher,Student
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout


def adminhome(request):
    return render(request,'adminhome.html')

def studenthome(request):
    return render(request,'studenthome.html')

def teacherhome(request):
    return render(request,'teacherhome.html')

def approve(request,aid):
    st=Student.objects.get(id=aid)
    st.sid.is_active=True
    st.sid.save()
    return redirect(viewstudents)

def viewstudents(request):
    x=Student.objects.all()
    return render(request,'viewstudents.html',{'x1':x})

def dep_add(request):
    if request.method=="POST":
        d=request.POST["dep"]
        x=Department.objects.create(Dep_Name=d)
        x.save()
        return HttpResponse("Success")
    else:
        return render(request,'dep_add.html')

def index(request):
    return render(request,'index.html')

def reg_teacher(request):
    if request.method=="POST":
        d=request.POST['dep']
        f=request.POST['fname']
        l=request.POST['lname']
        e=request.POST['email']
        u=request.POST['uname']
        p=request.POST['password']
        a=request.POST['age']
        ad=request.POST['address']
        q=request.POST['qual']
        x=User.objects.create_user(first_name=f,last_name=l,email=e,username=u,password=p,usertype='teacher')
        x.save()
        y=Teacher.objects.create(tid=x,depid_id=d,Age=a,Address=ad,Qualification=q)
        y.save()
        return HttpResponse("success")
    else:
        x=Department.objects.all()
        return render(request,'regtchr.html',{'x1':x})


def reg_student(request):
    if request.method=="POST":
        d=request.POST['dep']
        f=request.POST['fname']
        l=request.POST['lname']
        e=request.POST['email']
        u=request.POST['uname']
        p=request.POST['password']
        a=request.POST['age']
        ad=request.POST['address']
        x=User.objects.create_user(first_name=f,last_name=l,email=e,username=u,password=p,usertype='student',is_active=False)
        x.save()
        y=Student.objects.create(depid_id=d,sid=x,Age=a,Address=ad)
        y.save()
        return HttpResponse("student registered")
    else:
        x=Department.objects.all()
        return render(request,'reg_student.html',{'x1':x})



def logins(request):
    if request.method=="POST":
        u=request.POST['username']
        p=request.POST['password']
        user=authenticate(request,username=u,password=p)
        if user is not None and user.is_superuser==1:
            return redirect(adminhome)
        elif user is not None and user.usertype=="teacher":
            login(request,user)
            request.session['teach_id']=user.id
            return redirect(teacherhome)
        elif user is not None and user.usertype=="student" and user.is_active==1:
            login(request,user)
            request.session['stu_id']=user.id
            return redirect(studenthome)
        else:
            return HttpResponse("not valid")
    else:
        return render(request,'logins.html')



def approved_stview(request):
    x=User.objects.filter(is_active=1,usertype="student")
    return render(request,'approved_stview.html',{'x':x})


def updates(request):
    stud=request.session.get('stu_id')
    student=Student.objects.get(sid_id=stud)
    user=User.objects.get(id=stud)
    return render(request,'updatest.html',{'view':student,'data':user})

def updatestudent(request,uid):
    if request.method=="POST":
        stud=Student.objects.get(id=uid)
        sid=stud.sid_id
        user=User.objects.get(id=sid)
        user.first_name=request.POST['fname']
        user.last_name=request.POST['lname']
        user.email=request.POST['email']
        user.username=request.POST['uname']
        user.save()
        stud.Age=request.POST['age']
        stud.Address=request.POST['address']
        stud.save()
        return HttpResponse("success")
    

def updates1(request):
    teach=request.session.get('teach_id')
    teacher=Teacher.objects.get(tid_id=teach)
    user=User.objects.get(id=teach)
    return render(request,'updatetch.html',{'view':teacher,'data':user})

def updateteacher(request,uid):
    if request.method=="POST":
        teach=Teacher.objects.get(id=uid)
        tid=teach.tid_id
        user=User.objects.get(id=tid)
        user.first_name=request.POST['fname']
        user.last_name=request.POST['lname']
        user.email=request.POST['email']
        user.username=request.POST['uname']
        user.save()
        teach.Age=request.POST['age']
        teach.Address=request.POST['address']
        teach.Qualification=request.POST['qual']
        teach.save()    
        return HttpResponse("success")


def lgout(request):
    logout(request)
    return redirect(logins)

	
def deletestud(request,uid):
	x=User.objects.get(id=uid)
	x.delete()
	return redirect(viewstudents)


def adtchrview(request):
    x=Teacher.objects.all()
    return render(request,'admintchr.html',{'x':x})


def dlttchr(request,uid):
	x=User.objects.get(id=uid)
	x.delete()
	return redirect(adtchrview)



def depbystudent(request):
    teacher=Teacher.objects.get(tid=request.user)
    department_students=Student.objects.filter(depid=teacher.depid)
    return  render(request,'department_student.html',{'x1':department_students})


def depbyteacher(request):
    student=Student.objects.get(sid=request.user)
    department_teachers=Teacher.objects.filter(depid=student.depid)
    return render(request,'department_teacher.html',{'x1':department_teachers}) 