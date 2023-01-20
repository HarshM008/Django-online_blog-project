from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import SignupForm , LoginForm, Postform
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import Blogpost
from django.contrib.auth.models import Group


# home page 
def home(request):
    posts = Blogpost.objects.all() #Getting every fields from 'Blogpost' model.
    return render(request, 'appblog/home.html', {'Posts': posts})

# about page 
def about(request):
    return render(request, 'appblog/about.html')


# signup page 
def user_signup(request):
    if request.method == 'POST': #checking for POST data
        form = SignupForm(request.POST) #storing 'Signupform' data in variable.
        if form.is_valid(): #checking the valiidty of form
            user = form.save() #saving user details in variable
            group = Group.objects.get(name = 'Author') #getting author group data from admin panel
            user.groups.add(group) #adding new user to author group
            messages.success(request, 'Congratulations! You have become an Author.')
            return HttpResponseRedirect('/login')
    else: #checking if request is post
        form = SignupForm() #returning blank form
    return render (request, 'appblog/signup.html', {'form': form})

# dashboard page 
def dashboard(request):
    if request.user.is_authenticated: #checking if user is loggedin or not?
        posts = Blogpost.objects.all() #getting data of every blogpost
        user = request.user #storing users detail in variable
        full_name = user.get_full_name () #storing name of user in variable
        gps = user.groups.all() #storing users group name 
        return render(request, 'appblog/dashboard.html', {'Posts': posts, 'fname': full_name, 'groups':gps})
    else: #if user is not authenticated then redirecting to login page.
        return HttpResponseRedirect('/login')

# login page 
def user_login(request):
    if not request.user.is_authenticated: #checking if user is loggedin or not?
        if request.method =='POST': #checking for POST data
            form = LoginForm(request= request, data = request.POST)#storing 'Loginform' data in variable.
            if form.is_valid(): #checking the valiidty of form
                uname = form.cleaned_data['username'] #stroing clean data for name
                upass = form.cleaned_data['password'] #storing clean data for password 
                user = authenticate(username = uname, password = upass) #checking if proper credentials are there
                if user is not None: #if user's credentials are valid
                    login(request, user) #logging in with credentials
                    messages.success(request, 'Logged in successfully!') #msg after successful login
                    return HttpResponseRedirect('/dashboard') 
        else: #for GET data
            form = LoginForm() #blank form returning
        return render(request, 'appblog/login.html', {'form': form})
    else:
        return HttpResponseRedirect('/dashboard')


# logout page
def user_logout(request):
    logout(request) #performing logout with inbuilt 'logout' function
    return HttpResponseRedirect('/')

#adding post
def add_post(request):
    if request.user.is_authenticated: #checking if user is loggedin or not?
        if request.method =='POST': #checking for POST data
            form = Postform(request.POST)#storing 'Postform' data in variable.
            if form.is_valid(): #checking valididty of form
                title = form.cleaned_data['title'] #storing cleaned data of title
                desc = form.cleaned_data['desc'] #storing cleaned data of description
                pst = Blogpost(title = title, desc = desc ) #storing data of model 'Blogpost'
                pst.save() #saving data of variable 
                messages.success(request, 'Post added successfully!') 
                return HttpResponseRedirect('/dashboard')
        else: #checking for get data
            form = Postform() #returning blank form
        return render(request, 'appblog/addpost.html', {'form': form})
    else:
        return HttpResponseRedirect('/login')

#updating post
def update_post(request,id):
    if request.user.is_authenticated: #checking if user is loggedin or not?
        if request.method =='POST': #checking for POST data
            pi = Blogpost.objects.get(pk = id) #getting data of particular id 
            form = Postform(request.POST, instance = pi) #updating data for particular id
            if form.is_valid(): #checking validity of form
                form.save() #saving data 
                messages.success(request, 'Post updated successfully!')
                return HttpResponseRedirect('/dashboard')
        else: #checking for get data
            pi = Blogpost.objects.get(pk = id) #getting data of particular id
            form = Postform(instance = pi) #returning data back for particular id
        return render(request, 'appblog/updatepost.html', {'form': form})
    else:
        return HttpResponseRedirect('/login')


#deleting post
def delete_post(request,id):
    if request.user.is_authenticated: #checking if user is loggedin or not?
        if request.method == 'POST': #checking for POST data
            pi = Blogpost.objects.get(pk = id) #getting data of particular id
            pi.delete() #deleteing data of particular id
        return HttpResponseRedirect('/dashboard')
    else:
        return HttpResponseRedirect('/login')





