

from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name="home"),
    path('aboutus/', views.about, name="about"),
   
    path('feedback/', views.feedback,name="feedback"),
    path('signup/',views.register,name="signup"),
    path('upload/', views.upload, name='upload'),

    path('index/',views.home,name="index"),
    path('logout/',views.userlogout,name="logout"),
    path('login/',views.loginnew,name="login"),
]
