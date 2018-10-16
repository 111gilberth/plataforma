from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth

def signup(request):
    if request.method == 'POST':
<<<<<<< HEAD
        # El usuario tiene información y quiere una cuenta ahora!
=======
        # User has info and wants an account now!
>>>>>>> 84de7422dccebd14ef84d006e602175bf5f0a2a6
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.get(username=request.POST['username'])
                return render(request, 'accounts/signup.html', {'error':'Username has already been taken. Please choose another one'})
            except User.DoesNotExist:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                auth.login(request,user)
                return redirect('home')
        else:
            return render(request, 'accounts/signup.html', {'error':'The passwords you have entered does not match'})
    else:
<<<<<<< HEAD
        # El usuario quiere ingresar información
=======
        # User wants to enter info
>>>>>>> 84de7422dccebd14ef84d006e602175bf5f0a2a6
        return render(request, 'accounts/signup.html')

def login(request):
    if request.method == 'POST':
        user = auth.authenticate(username=request.POST['username'],password=request.POST['password'])
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request, 'accounts/login.html',{'error':'The username or the password that you have entered is incorrect. Please try again'})
    else:
        return render(request, 'accounts/login.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('chao')
def home(request):
    #documents = Document.objects.all()
    return render(request, 'accounts/home.html')
def chao(request):
    return render(request,'accounts/chao.html')

# Create your views here.
