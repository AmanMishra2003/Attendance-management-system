from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def landingPage(request):
    return render(request, 'members/landing.html')

def login_page(request):
    if request.method =='POST':
        username = request.POST.get('username',False)
        password = request.POST.get('pass',False)
        if username!="" and password!="":
            user = authenticate(request, username =username, password = password)
            if user is not None:
                login(request, user)
                return redirect("/User/home")
            else:
                messages.success(request,("There was a error Login IN, Try again"))
                return redirect("login")
        else:
            messages.success(request,("Enter correct credentials."))
            return redirect("login")
    else:
        return render(request, 'members/login.html')

def sign_up(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = request.POST.get('username',False)
            password = request.POST.get('password1',False)
            user = authenticate(request, username =username, password = password)
            login(request, user)
            return redirect("/User/home")
    else:
        form = UserCreationForm()
    context =  {'form':form}
    return render(request, 'members/signup.html',context)

def sign_out(request):
    logout(request)
    
    return redirect('landing')