from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from .forms import *
from django.shortcuts import render, redirect
from django.contrib.auth.models import User


def home(request):
	template = 'interfaces/home.html'
	return render(request, template, {})

def login(request):
	template = 'interfaces/login.html'
	
	if request.method == 'POST':
		print('entro por aca la wea!')
		print (request.POST)
		form = LoginForm(request.POST)

	form = LoginForm()

	return render(request, template, {'form':form})


def signup(request):

    template = 'interfaces/signup.html'

    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
        	print(form.cleaned_data)
        	username = form.cleaned_data.get('username')
        	raw_password = form.cleaned_data.get('password')
        	if User.objects.filter(username=username).count() > 0:
        		return render(request, template, {'form':form,
        										  'error': username + ' ya está registrado.'})
        	user = User(username=username, password=raw_password, email= form.cleaned_data_ ,first_name=form.cleaned_data.get('nombre'), last_name=form.cleaned_data.get('apellido'))
        	user.save()
            


            #user = authenticate(username=username, password=raw_password)
            #login(request, user)
            #return redirect('home')
    else:
        form = SignUpForm()

    return render(request, template, {'form': form})