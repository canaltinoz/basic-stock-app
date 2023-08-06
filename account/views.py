from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

def user_login(request):
    if request.user.is_authenticated:
        return redirect("index")

    if request.method != "POST":
        return render(request, "account/login.html")
    username = request.POST["username"]
    password = request.POST["password"]

    user = authenticate(request, username=username,password=password)

    if user is None:
        return render(request, "account/login.html", {"error":"username ya da parola yanlış"})
    login(request, user)
    return redirect("index")

def user_register(request):
    if request.method != "POST":
        return render(request, "account/register.html")
    
    
    username = request.POST["username"]
    email = request.POST["email"]
    password = request.POST["password"]
    repassword = request.POST["repassword"]

    if password != repassword:
        return render(request, "account/register.html", 
        {
            "error":"parola eşleşmiyor.",
            "username": username,
            "email": email
        })

    if User.objects.filter(username = username).exists():
        return render(request, "account/register.html", 
        {
            "error":"username kullanılıyor.",
            "username": username,
            "email": email
        })

    if User.objects.filter(email=email).exists():
        return render(request, "account/register.html", 
        {
            "error":"email kullanılıyor.",
            "username": username,
            "email": email
        })

    user = User.objects.create_user(username=username, email=email,password=password)
    user.save()
    return redirect("user_login")

def user_logout(request):
    logout(request)
    return redirect("index")