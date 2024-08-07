from django.conf import settings
from .models import Password
from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login, logout as auth_logout, authenticate
from django.contrib.auth.forms import AuthenticationForm , UserCreationForm
from .forms import UserRegisterForm
from cryptography.fernet import Fernet 
from django.contrib.auth.views import PasswordResetView
from .forms import CustomPasswordResetForm
from django.contrib import messages
from django.urls import reverse_lazy
from cryptography.fernet import Fernet
from .forms import PasswordEntryForm
from django.shortcuts import get_object_or_404
# from .forms import PasswordForm


from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

@csrf_exempt
def test_login(request):
    return JsonResponse({
        "is_logged_in":request.user.is_authenticated,
        "logged_in_username":request.user.username if request.user.is_authenticated else None
    })

def encrypt_password(password):
    cipher_suite = Fernet(settings.FERNET_KEY.encode())
    encrypted_password = cipher_suite.encrypt(password.encode())
    return encrypted_password.decode()

def decrypt_password(encrypted_password):
    cipher_suite = Fernet(settings.FERNET_KEY.encode())
    decrypted_password = cipher_suite.decrypt(encrypted_password.encode()).decode()
    return decrypted_password

def signupPage(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            auth_login(request, user)
            return redirect('menu')   
    else:
        form = UserRegisterForm()
        if request.method == 'GET':
            form = UserRegisterForm()
    return render(request, 'signup.html', {'form': form})

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('menu')
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('menu')  
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def logoutPage(request):

        auth_logout(request)
        return redirect('login') 

# def menu(request):
#     if not request.user.is_authenticated:
#         return redirect('login')
#     if request.method == "POST":
#         username = request.POST.get('username', '')  
#         url = request.POST.get('url', '')  
#         password = request.POST.get('pwd', '')  
#         choice_text = request.POST.get('choice_text', '')

#         # Encrypt the password
#         cipher_suite = Fernet(settings.FERNET_KEY.encode()) 
#         encrypted_password = cipher_suite.encrypt(password.encode())


#         if username:
#             Password.objects.create(url=url, username=username, password=encrypted_password.decode(), user=request.user, choice_text=choice_text)
#             return redirect('menu')  
       
#     entries = Password.objects.filter(user=request.user)
#     cipher_suite = Fernet(settings.FERNET_KEY.encode())
#     decrypted_entries = []
#     for entry in entries:
#         try:
#             decrypted_password = cipher_suite.decrypt(entry.password.encode()).decode()
#             decrypted_entries.append({
#                 'url': entry.url,
#                 'username': entry.username,
#                 'password': decrypted_password,
#                 'choice_text': entry.choice_text
#             })
#         except Exception as e:
#             # Handle decryption error
#             print(f"Error decrypting password for {entry.url}: {e}")
#             decrypted_entries.append({
#                 'url': entry.url,
#                 'username': entry.username,
#                 'password': 'Error decrypting password',
#                 'choice_text': entry.choice_text
#             })

#     return render(request, 'password.html', {'entries': decrypted_entries})
def menu(request):
    if not request.user.is_authenticated:
        return redirect('login')

    if request.method == "POST":
        url = request.POST.get('url')
        username = request.POST.get('username')
        password = request.POST.get('pwd')
        choice_text = request.POST.get('choice_text')

        cipher_suite = Fernet(settings.FERNET_KEY.encode())
        encrypted_password = cipher_suite.encrypt(password.encode())

        Password.objects.create(
            url=url,
            username=username,
            password=encrypted_password.decode(),
            user=request.user,
            choice_text=choice_text
        )
        return redirect('menu')

    entries = Password.objects.filter(user=request.user)
    cipher_suite = Fernet(settings.FERNET_KEY.encode())
    decrypted_entries = []
    for entry in entries:
        decrypted_password = cipher_suite.decrypt(entry.password.encode()).decode()
        decrypted_entries.append({
            'id': entry.id,
            'url': entry.url,
            'username': entry.username,
            'password': decrypted_password,
            'choice_text': entry.choice_text
        })

    return render(request, 'password.html', {'entries': decrypted_entries})

def edit_entry(request, entry_id):
    entry = get_object_or_404(Password, id=entry_id, user=request.user)
    cipher_suite = Fernet(settings.FERNET_KEY.encode())
    if request.method == 'POST':
        entry.url = request.POST.get('url')
        entry.username = request.POST.get('username')
        entry.password = cipher_suite.encrypt(request.POST.get('pwd').encode()).decode()
        entry.choice_text = request.POST.get('choice_text')
        entry.save()
        return redirect('menu')

    decrypted_password = cipher_suite.decrypt(entry.password.encode()).decode()
    return render(request, 'edit_entry.html', {'entry': entry, 'password': decrypted_password})

def delete_entry(request, entry_id):
    entry = get_object_or_404(Password, id=entry_id, user=request.user)
    if request.method == 'POST':
        entry.delete()
        return redirect('menu')
    return render(request, 'delete_entry.html', {'entry': entry})

def notes(request):
    return render(request, 'notes.html')

def home(request):
    return render(request, 'base.html')
def about(request):
    return render(request, 'about.html')

def passwordgenerator(request):
    return render(request, 'passwordgenerator/passwordgenerator.html')

def passwordchange(request):
    return render(request, 'passwordchange.html')

class CustomPasswordResetView(PasswordResetView):
    form_class = CustomPasswordResetForm

    def form_valid(self, form):
        """
        If the form is valid, redirect to the supplied URL.
        """
        email = form.cleaned_data['email']
        users = form.get_users(email)
        if not users:
            messages.error(self.request, 'This email address is not registered.')
            return self.form_invalid(form)
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('password_reset_done')