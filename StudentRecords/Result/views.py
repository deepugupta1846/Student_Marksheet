from django.shortcuts import render, redirect
from .forms import *
# Create your views here.
from django.http import HttpResponse


def home(request):
    return render(request, 'base.html')


def studenthome(request):
    if request.session.get('name', 'None') == 'None':
        return redirect('/login/')
    nt = int(request.COOKIES.get("counter", "0"))
    response = render(request, 'studenthome.html', {"nt": nt})
    response.set_cookie("name", "ricla", 60*1)
    return response



def login(request):
    msg = ""
    if request.method == 'POST':
        if request.POST['un'] == 'students432@gmail.com' and request.POST['pwd'] == 'Ricla321':
            request.session['name'] = "ricla"
            request.session.set_expiry(100)
            return redirect('/')
        else:
            msg = "Invalid username and password !!!"
    return render(request, 'base.html', {'msg': msg})


def logout(request):
    if request.session.get('name', 'None') == 'None':
        return redirect('/login/')
    del request.session['name']
    return redirect('/')


def addnewstudent(request):
    msg = ""
    if request.session.get('name', 'None') == 'None':
        return redirect('/login/')
    if request.method == 'POST':
        f = addstudent(request.POST)
        f.save()
        msg = "Record Add Successfully"
    f = addstudent()
    return render(request, 'AddNewStudents.html', {'form': f, 'msg': msg})


def delete(request, roll):
    if request.session.get('name', 'None') == 'None':
        return redirect('/login/')
    f = StudentRecords.objects.get(roll=roll)
    f.delete()
    return redirect('/showall/')


def update(request, roll):
    if request.session.get('name', 'None') == 'None':
        return redirect('/login/')
    f = StudentRecords.objects.get(roll=roll)
    if request.method == 'POST':
        forms = addstudent(request.POST, instance=f)
        if forms.is_valid():
            forms.save()
            return redirect('/showall/')
    else:
        forms = addstudent(instance=f)
        return render(request, 'update.html', {'form': forms})


def showresult(request):
    if request.session.get('name', 'None') == 'None':
        return redirect('/login/')
    msg = ""
    gen = ""
    if request.method == 'POST':
        s = request.POST['rollno']
        if s:
            r = StudentRecords.objects.filter(roll__exact=s)
            if r:
                for i in r:
                    i.total = i.paper1 + i.paper2 + i.paper3 + i.paper4 + i.paper5
                    i.percent = i.total / 5.0
                    if i.paper1 < 30 or i.paper2 < 30 or i.paper3 < 30 or i.paper4 < 30 or i.paper5 < 30:
                        i.division = "Fail"
                    else:
                        if i.percent >= 60:
                            i.division = "First"
                        else:
                            if i.percent >= 45:
                                i.division = "Second"
                            else:
                                if i.percent >= 30:
                                    i.division = "Third"
                                else:
                                    i.division = "Fail"
                return render(request,'result.html', {'r': r, 'gen': gen})
            else:
                msg = "Result Not Found"
        else:
            return HttpResponse('/result/')
    return render(request, 'result.html',{'msg':msg})



def showall(request):
    if request.session.get('name', 'None') == 'None':
        return redirect('/login/')
    v = StudentRecords.objects.all()
    for i in v:
        i.total = i.paper1 + i.paper2 + i.paper3 + i.paper4 + i.paper5
        i.percent = i.total / 5.0
        if i.paper1 < 30 or i.paper2 < 30 or i.paper3 < 30 or i.paper4 < 30 or i.paper5 < 30:
            i.division = "Fail"
        else:
            if i.percent >= 60:
                i.division = "First"
            else:
                if i.percent >= 45:
                    i.division = "Second"
                else:
                    if i.percent >= 30:
                        i.division = "Third"
                    else:
                        i.division = "Fail"
    return render(request, 'ShowAllRecords.html', {'allrecords': v})
