from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib import messages
from django.shortcuts import render
from .forms import CustomUserCreationForm

# Signup view
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib import messages


def signup_view(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Signup successful")
            return redirect("home")  # Adjust this if your home URL is named differently
    else:
        form = CustomUserCreationForm()
    return render(
        request, "accounts/signup.html", {"form": form}
    )  # Ensure this matches the path


# Login view
def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, "Login successful")
            return redirect("home")  # Redirect to home page after login
    else:
        form = AuthenticationForm()
    return render(request, "accounts/login.html", {"form": form})


# Logout view
def logout_view(request):
    logout(request)
    messages.success(request, "Logged out successfully")
    return redirect("home")


def home_view(request):
    return render(request, "pages/home.html")