from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from .forms import UserRegisterForm, EditProfileForm
from .models import UserProfile


# Create your views here.
def register_user(request):
    if request.method != 'POST':
        form = UserRegisterForm()
    else:
        form = UserRegisterForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('shop:index')
    context = {'form': form}
    return render(request, 'registration/register.html', context)


def logout_view(request):
    logout(request)
    return redirect('/')


@login_required(login_url='users:login')
def user_profile(request):
    profile = UserProfile.objects.get(email=request.user.email)
    context = {'profile': profile}
    return render(request, 'registration/profile.html', context)


@login_required(login_url='users:login')
def edit_profile_view(request):
    profile = UserProfile.objects.get(email=request.user.email)
    if request.method != 'POST':
        form = EditProfileForm(instance=profile)
    else:
        form = EditProfileForm(instance=profile, data=request.POST, files=request.FILES)
        user = User.objects.get(id=request.user.id)

        if form.is_valid():
            user.username = form.instance.username
            user.first_name = form.instance.first_name
            user.last_name = form.instance.last_name
            user.email = form.instance.email
            user.save()
            form.save()
            return redirect('users:profile')

    context = {'form': form}
    return render(request, 'registration/edit_profile.html', context)
