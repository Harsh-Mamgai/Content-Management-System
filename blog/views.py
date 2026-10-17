from django.shortcuts import render, HttpResponse, redirect
from blog.models import Blog, Comment
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
import math
# Create your views here.
def home(request):
    return render(request, 'index.html')

def blog(request):
    no_of_posts = 3
    page = request.GET.get('page')
    if(page is None):
        page = 1
    else:
        page = int(page)

    blogs = Blog.objects.all()
    length = len(blogs)
    blogs = blogs[(page-1)*(no_of_posts) : (page)*(no_of_posts)]

    if (page > 1):
        prev = page-1
    else:
        prev = None
    if(page < math.ceil(length/no_of_posts)):
        nxt = page+1
    else:
        nxt = None
    context = {'blogs' : blogs, 'prev' : prev, 'nxt' : nxt}
    return render(request, 'bloghome.html', context)

def search(request):
    if request.method == 'POST':
        query = request.POST['search']
        obj = Blog.objects.filter(content__icontains=query)
        context = {'logs' : obj}
    return render(request, 'search.html', context)

#this view is used to click on a blog title so it can be opened
def blogpost(request, slug):
    blog = Blog.objects.filter(slug=slug).first
    context = {'blog' : blog}
    return render(request, 'blogpost.html', context)

#Sign-Up and Lopgin views
def signup(request):
    if (request.method == 'POST'):
        name = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
        #validations
        if User.objects.filter(username = name).exists():
            messages.error(request, 'Username already exists')
            return redirect('signup')
        if pass1 != pass2:
            messages.error(request, 'Please enter same password as typed previously')
            return redirect('signup')
        if len(name) > 100:
            messages.error(request, 'Please enter a username with not more than 100 characters')
            return redirect('signup')
        obj = User.objects.create_user(username=name, password=pass1, email=email)
        obj.first_name = fname
        obj.last_name = lname
        obj.save()
        messages.success(request, "User account created successfully")
    return render(request, 'signup.html')

def userlogin(request):
    if request.method == 'POST':
        name = request.POST['name']
        password = request.POST['password']
        user = authenticate(request, username=name, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Congractulations you are logged in successfully")
            return redirect('/')
        else:
            messages.error(request, "Please provide correct username and password")
    return render(request, 'login.html')

def userlogout(request):
    logout(request)
    messages.success(request, "User logged out successfully")
    return render(request, 'logout.html')

def comment(request, slug):
    context = {'slug': slug}
    if request.method == 'POST':
        name = request.user.username
        fname = request.user.first_name
        lname = request.user.last_name
        cmt = request.POST['comment']
        info = slug
        obj = Comment(name=name, fname=fname, lname=lname, content=cmt, info=info)
        obj.save()
        messages.success(request, 'your comment was added')
    return render(request, 'comment.html', context)

def viewcomment(request, slug):
    comments = Comment.objects.filter(info=slug)
    context = {'comments': comments}
    return render(request, 'show.html', context)
