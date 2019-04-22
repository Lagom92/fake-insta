from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from .forms import CustomUserCreationForm, CustomUserChangeForm
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required

# Create your views here.
def signup(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("posts:list")
        
    else:
        form = CustomUserCreationForm()

    return render(request, 'accounts/form.html', {'form':form})
    
    
def login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect("posts:list")
        
    else:
        form = AuthenticationForm()
        
    return render(request, 'accounts/form.html', {'form':form})
    
@login_required
def logout(request):
    auth_logout(request)
    return redirect("posts:list")
   
@login_required
def user_page(request, id):
    User = get_user_model()
    user_info = User.objects.get(id=id)
    return render(request, "accounts/user_page.html", {"user_info":user_info})
    
@login_required
def follow(request, id):
    # 로그인한 사람 
    me = request.user
    # 팔로우를 하려는 사람
    User = get_user_model()
    you = User.objects.get(id=id)
    
    if me != you:
        if you in me.followings.all():
            # 취소
            me.followings.remove(you)
        else:
            # 추가
            me.followings.add(you)
    
    return redirect("accounts:user_page", id)
    
@login_required
def edit_profile(request, id):
    me = request.user
    User = get_user_model()
    user = User.objects.get(id=id)
    if me == user:
        if request.method == "POST":
            form = CustomUserChangeForm(request.POST, request.FILES, instance=user)
            if form.is_valid():
                form.save()
                
                return redirect("accounts:user_page", id)
        else:
            form = CustomUserChangeForm(instance=user)
        return render(request, 'accounts/form.html', {'form':form})
    else:
        return redirect("posts:list")
    