from django.shortcuts import render, redirect
from .forms import *
from django.http import JsonResponse
# Create your views here.


def index(request):
    return render(request, 'home.html')


def loginpage(request):
    if request.session.get('name', 'none') == 'none':
        return redirect('/login/')
    un = request.session['name']
    return render(request, 'loginpage.html',{'un':un})


def login(request):
    msg = ""
    if request.method == 'POST':
        user = SignupData.objects.filter(Email__exact=request.POST['uid']).filter(Password__exact=request.POST['pwd'])
        if len(user) != 0:
            request.session['name'] = user[0].Name
            return redirect('/loginpage/')
        else:
            msg = "Invalid user name and password"
    return render(request, 'login.html', {'msg': msg})


def addUser(request):
    msg = ""

    if request.method == 'POST':
        f = signup()
        d = SignupData.objects.filter(Email__exact=request.POST['Email'])
        if len(d) != 0:
            msg = "Email already exists!"
            return render(request, 'signup.html', {'form': f, 'msg': msg})
        f = signup(request.POST)
        f.save()
        msg = "User Added Successfully"
    f = signup()
    return render(request, 'signup.html', {'form': f, 'msg': msg})


def logout(request):
    if request.session.get('name', 'None') == 'None':
        return redirect('/login/')
    del request.session['name']
    return redirect('/login/')


def profile(request):
    if request.session.get('name', 'None') == 'None':
        return redirect('/login/')
    data = SignupData.objects.get(Name=request.session['name'])
    if data.Gender == 'M':
        Gen = "Mr. "
    else:
        Gen = "Miss. "
    return render(request, 'profile.html', {'data': data, 'Gen': Gen})

def showdata(request):
    if request.session.get('name', 'None') == 'None':
        return redirect('/login/')
    d = SignupData.objects.all()
    data = []
    for i in d:
        p = {'Name':i.Name, 'Mob_No':i.Mob_No, 'Gender':i.Gender, 'Email':i.Email, 'Password':i.Password}
    data.append(p)
    return JsonResponse(data, safe=False)


def update(request):
    if request.session.get('name', 'None') == 'None':
        return redirect('/login/')
    data = SignupData.objects.get(Name=request.session['name'])
    if data.Gender == 'M':
        Gen = "Mr. "
    else:
        Gen = "Miss. "
    if request.method == 'POST':
        forms = updateform(request.POST, instance=data)
        if forms.is_valid():
            forms.save()
            return redirect('/logoutpage/')
    else:
        forms = updateform(instance=data)
    return render(request, 'update.html', {'updateform': forms, 'data':data, 'Gen': Gen})


def logoutpage(request):
    if request.session.get('name', 'None') == 'None':
        return redirect('/login/')
    return render(request, 'logout.html')




