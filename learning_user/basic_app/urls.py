from django.urls import path
from . import views

app_name="basic_app"

urlpatterns=[
    path("register/",views.uye_ol,name="register"),
    path("user_login/",views.girisYap,name='user_login'),
    path("user_logout/",views.cikisYap,name="user_logout"),
    path("ozel/",views.ozel,name="user_ozel") 

]