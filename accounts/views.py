from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.forms import AuthenticationForm
from . forms import UserRegistrationForm




def home(request):
    return render(request,'accounts/home.html')

def register_view(request):
   
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('login')
        

    else:
        form = UserRegistrationForm()

    return render(request, 'accounts/register.html', {'form':form})



def login_view(request):
   
    if request.method == 'POST':
        # username = request.POST.get('username')
        # password = request.POST.get('password')
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
        # else:
        #     return HttpResponse("Username or password is incorrect ")
            
    else:
        form = AuthenticationForm()

    return render(request, 'accounts/login.html', {'form':form})

def logout_view(request):
    logout(request)
    return redirect('home')


# Create your views here.
