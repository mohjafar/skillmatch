"""Skillmatch URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from Mainapp  import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.HomePage ),
    #path('feedback_form/', views.feedback_view),
    #path('work-complete/', views.CompleteWork),
    path('account/',views.account),
    path('signup/',views.SignupSection),
    path('login/',views.LoginPage),
    path('logout/',views.LogOut),
    path('plumber/',views.PlumberPage),
    path('electrician/',views.ElectricianPage),
    path('carpenter/',views.CarpenterPage),
    path('painter/',views.PainterPage),
    path('mechenic/',views.MachenicPage),
    path('search/',views.SearchPage),
    path('search1/',views.SearchLocation),
    path('updateEmp/<int:id>/',views.UpdateEmp),
    path('add-to-cart/<int:id>/',views.AddToCart),
    path('cart/',views.cartfrontpage),
    path('profile/',views.ProfileSection),
    path('EmployeeData/',views.ProfilePage),
    path('worker/',views.WorkerSignup),
    path('updateprofile/',views.UpdateProfile),
    path('service/<int:id>/',views.BookService),
    path('booking/',views.BookPage),
    path('deleteservice/<int:id>/',views.DeleteService),
    path('workerjob/',views.WorkerJob),
    path('all_services/',views.all_services),
    path('contact/',views.ContactUS),
    path('forget-username/',views.ForgetUsername),
    path('forget-otp/',views.forgetOTP),
    path('password/',views.password),
    




]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
