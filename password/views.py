from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Password

def menu(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['pwd']
        print("Submit")
        Password.objects.create(url=username, password=password)
    # return HttpResponse("Hello, world. You're at the index.")
    return render(request, 'password.html')
def notes(request):
    return render(request, 'notes.html')
def passwords(request):
    return render(request, 'password.html')