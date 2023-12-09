from django.shortcuts import render
from .forms import UserForm,UserProfilForm 
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate,login,logout

# Create your views here.

def anasayfa(request):
    return render(request,"basic_app/index.html")

def uye_ol(request):
    registered=False
    uyeForm=UserForm()
    profilForm=UserProfilForm()
    if request.method=="POST":
        uyeForm=UserForm(request.POST)
        profilForm=UserProfilForm(request.POST,request.FILES)
        if uyeForm.is_valid() and profilForm.is_valid():
            user=uyeForm.save()
            user.set_password(user.password)
            user.save()
            profil=profilForm.save(commit=False)
            profil.user=user
            if 'profile_pic' in request.FILES.keys():
                profil.profile_pic=request.FILES["profile_pic"]
            profil.save()
            registered=True
    
    context={
        "userform":uyeForm,
        "profilform":profilForm,
        "registered":registered
    }


    return render(request,"basic_app/register.html",context)

def girisYap(request):
    if request.method=="POST":
        username=request.POST.get("username","")
        password=request.POST.get("password","")
        user=authenticate(request,username=username,password=password)
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse("index"))
            else:
                return HttpResponse("Kullanıcı aktif değil!")
        else:
            return HttpResponse("Hatalı kullanıcı adı veya şifre!")
    else:
        return render(request,"basic_app/login.html")
    
@login_required
def cikisYap(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))

@login_required
def ozel(required):
    return HttpResponse("You are logginned!({})".format(required.user.username))