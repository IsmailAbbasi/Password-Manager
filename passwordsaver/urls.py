"""
URL configuration for passwordsaver project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import include, path
from django.http import HttpResponse
from django.shortcuts import redirect
from password.views import menu
from password.views import notes
from password.views import signupPage
from password.views import loginPage
from password.views import logoutPage
from password.views import about
from password.views import passwordgenerator
from password.views import passwordchange
from django.contrib.auth import views as auth_views
from password.views import CustomPasswordResetView
from password.views import menu, edit_entry, delete_entry
from password.views import test_login


def home(request):
    if request.user.is_authenticated:
        return redirect('menu')
    return redirect('login')

urlpatterns = [
    path('',home,name='home'),
    path("password/", include("password.urls")), 
    path("admin/", admin.site.urls),
    path('menu/', menu, name='menu'),
    path('notes/', notes, name='notes'),
    path('signup/', signupPage, name='signup'),
    path('login/', loginPage, name='login'),
    path('logout/', logoutPage, name='logout'),
    path('about/', about, name='about'),
    path('passwordgenerator/passwordgenerator/', passwordgenerator, name='passwordgenerator'),
    path('passwordchange/', auth_views.PasswordChangeView.as_view(template_name='passwordchange.html'), name='passwordchange'),
    path('passwordchange/done/', auth_views.PasswordChangeDoneView.as_view(template_name='password_change_done.html'), name='password_change_done'),
    # path('password_reset/', auth_views.PasswordResetView.as_view(template_name='password_reset_form.html'), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'), name='password_reset_complete'),
    path('password_reset/', CustomPasswordResetView.as_view(template_name='password_reset_form.html'), name='password_reset'),
    path('edit/<int:entry_id>/', edit_entry, name='edit_entry'),
    path('delete/<int:entry_id>/', delete_entry, name='delete_entry'), 

    path('test-login/', test_login),
]