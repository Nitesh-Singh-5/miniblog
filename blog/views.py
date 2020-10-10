from django.shortcuts import render,HttpResponseRedirect
from .forms import SignUpForm,LoginForm,PostForm,studentRegistration,PassChange,EditUserProfileForm,EditAdminProfileForm,UserChangeForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from .models import Post,contact
from django.contrib.auth.models import Group
from django.core.cache import cache
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.views.generic import DetailView


# Home Page
def home(request):
    posts = Post.objects.all()
    # paginator = Paginator(posts, 4,orphans=1)
    # page_number = request.GET.get('page')
    # page_obj = paginator.get_page(page_number)
    return render(request,'blog/home.html',{'posts':posts})
    
# About Page
def about(request):
    return render(request, 'blog/about.html')

# contact page
def contact(request):
    if request.method == 'POST':
        fm= studentRegistration(request.POST)
        if fm.is_valid():
            nm= fm.cleaned_data['name']
            em= fm.cleaned_data['email']
            msg= fm.cleaned_data['message']
            reg=contact(name=nm,email=em,message=msg)
            reg.save()
            
            fm=studentRegistration()
            
    else:   
        fm= studentRegistration()
    return render(request,'blog/contact.html',{'form':fm})


# Dashboard Page
def dashboard(request):
    if request.user.is_authenticated:
        user =request.user
        posts = Post.objects.order_by('-id')
        full_name = user.get_full_name()
        gps = user.groups.all()
        ip = request.session.get('ip',0)
        ct = cache.get('count', version=user.pk)
        return render(request, 'blog/dashboard.html',{'posts':posts,'full_name':full_name,'groups':gps,'ip':ip,'ct':ct})
    else:
        return HttpResponseRedirect('/login/')

# Logout Page
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')

# SignUp Page
def user_signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            messages.success(request, 'Congratulations!! You have become an Author')
            user = form.save()
            group = Group.objects.get(name='author')  
            user.groups.add(group)
    else:
        form = SignUpForm()
    return render(request, 'blog/signup.html',{'form':form})

# Login Page
def user_login(request):
    if not request.user.is_authenticated:
        request.session['name'] = 'Nitesh'
        if request.method =='POST':
            form = LoginForm(request=request, data = request.POST)
            if form.is_valid():
                uname = form.cleaned_data['username']
                upass = form.cleaned_data['password']
                user = authenticate(username=uname, password = upass)
                if user is not None:
                    login(request,user)
                    messages.success(request, 'Logged in successfully')
                    return HttpResponseRedirect('/dashboard/')
        else:
            form= LoginForm()
        return render(request, 'blog/login.html',{'form':form})
    else:
        return HttpResponseRedirect('/dashboard/')


# Change password
def user_change_pass(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            fm=PassChange(user=request.user,data=request.POST)
            if fm.is_valid():
                fm.save()
                update_session_auth_hash(request,fm.user)
                messages.success(request,'password successfully changed')
                return HttpResponseRedirect('/dashboard/')
        else:
            fm=PassChange(user=request.user)
        return render(request,'blog/changepass.html',{'form':fm})
    else:
        HttpResponseRedirect('/login/')


# Add New Post
def add_post(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = PostForm(request.POST)
            if form.is_valid():
                title = form.cleaned_data['title']
                description = form.cleaned_data['description']
                pst= Post(title=title, description=description)
                pst.save()
                messages.success(request,'post added successfully')
                return HttpResponseRedirect('/dashboard/')
        else:
            form = PostForm
        return render(request, 'blog/addpost.html',{'form':form})
    else:
        return HttpResponseRedirect('/login/')


# Update Post
def update_post(request,id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            pi = Post.objects.get(pk=id)
            form = PostForm(request.POST, instance=pi)
            if form.is_valid():
                form.save()
                messages.success(request, 'Post edited successfully')
        else:
            pi = Post.objects.get(pk=id)
            form = PostForm(instance=pi)
        return render(request, 'blog/updatepost.html',{'form':form})
    else:
        return HttpResponseRedirect('/login/')

# Delete Post
def delete_post(request,id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            pi = Post.objects.get(pk=id)
            pi.delete()
            return HttpResponseRedirect('/dashboard/')
    else:
        return HttpResponseRedirect('/login/')

# Profile Page
def userinfo(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            fm = EditUserProfileForm(request.POST ,
            instance= request.user)
            if fm.is_valid():
                messages.success(request,'Your Profile updated successfully')
                fm.save()
        else:
            fm = EditUserProfileForm(instance = request.user)
        return render(request,'blog/profile.html',{'name':request.user,'form':fm})
    else:
        return HttpResponseRedirect('/login/')

# Post detail page
class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/postdetail.html'

        
            
    

