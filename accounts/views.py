from django.shortcuts import render, redirect
from .forms import RegistrationForm
from .models import Account
from django.contrib import messages, auth

# Create your views here.


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            phone_number = form.cleaned_data['phone_number']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            username = email.split('@')[0]
            user = Account.objects.create_user(
                first_name=first_name,
                last_name=last_name,
                email=email,
                username=username,
                password=password
            )
            """ we are updating phone number later bcoz in creat_user method we create earlier dont have phone number field
            """
            user.phone_number = phone_number
            user.save()
            messages.success(request, 'Registration Sucessful')
            return redirect('register')
    else:
        form = RegistrationForm()
    context = {
        'form': form
    }
    return render(request, 'accounts/register.html', context)


def login(request):
    import os
    print(os.getcwd())
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        user = auth.authenticate(email=email, password=password)
        
        if user is not None:
            auth.login(request, user)
            messages.success(request, 'you are logged in succesfully')
            return redirect('home')
        else:
            messages.error(request, 'invalid login credentials')
            return redirect('login')
    context = {

    }
    return render(request, 'accounts/login.html', context)


def logout(request):
    pass
