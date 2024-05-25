from django.urls import path, include
from . import views
from password.views import menu
from password.views import home
from django.contrib import admin
urlpatterns = [ 
    path('menu/', menu, name='menu'),
   path('admin/', admin.site.urls),
    path('', home, name='home'),
    # path('password/', include('password.urls')),
    # path('', include('password.urls')),  
]