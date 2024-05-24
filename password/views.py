
# from django.shortcuts import render
# from .models import Password

# def menu(request):
#     if request.method == "POST":
#         username = request.POST['username','']
#         url = request.POST['url','']
#         password = request.POST['pwd','']
#         Password.objects.create(url=url,username=username, password=password)
#         return redirect('menu')  # Redirect to the same page to prevent form resubmission
#     entries = Password.objects.all()
#     return render(request, 'password.html', {'entries': entries})

# def notes(request):
#     return render(request, 'notes.html')

from django.shortcuts import render, redirect
from .models import Password

def menu(request):
    if request.method == "POST":
        # Use request.POST.get() to handle the case where the key is missing or its value is empty
        username = request.POST.get('username', '')  
        url = request.POST.get('url', '')  
        password = request.POST.get('pwd', '')  
        
       
        if username:
            Password.objects.create(url=url, username=username, password=password)
            return redirect('menu')  
        else:
           
            pass
        
    entries = Password.objects.all()
    return render(request, 'password.html', {'entries': entries})

def notes(request):
    return render(request, 'notes.html')
