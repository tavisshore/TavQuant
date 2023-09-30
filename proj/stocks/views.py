from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, authenticate

@login_required
def index(request):
    return render(request, 'index.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['inputUser']
        password = request.POST['inputPassword']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            return render(request, 'login.html')
        

    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return render(request, 'login.html')