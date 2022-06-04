<<<<<<< HEAD
from django.shortcuts import render
from django.views import generic
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from Accounts.forms import CreacionUsuario
from django.urls import reverse_lazy
from .forms import EditProfileForm
from django.core.files.storage import FileSystemStorage


# ACCOUNTS PAGE
def accounts_page(request):
    return render(request, "registration/accounts.html")

def signup_estudio(request):
    
    form = CreacionUsuario

    if request.method == 'POST':
        
        form = CreacionUsuario(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            form.save()
            return render(request, "EstudioApp/index.html", {'msj': f'Se creó el usuario {username}'})


        else: 
            form = CreacionUsuario()
    
    return render(request, "registration/signup.html", {'form': form})

# LOGIN
def login_estudio(request):

    if request.method == 'POST':
        form = AuthenticationForm(request, data = request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)

                return render(request, "registration/accounts.html", {'msj':f'Bienvenido {user}'})

            else:
                return render(request, "registration/login.html", {'form' : form, 'msj': 'Error, los datos son incorrectos'})
        
        else:
            return render(request, "registration/login.html", {'form' : form, 'msj' : 'Usuario y/o contraseña incorrectos'})

    form = AuthenticationForm()

    return render(request, "registration/login.html", {'form' : form})

# EDITAR PERFIL

class UserEditView(generic.UpdateView):
    form_class = EditProfileForm
    template_name = 'registration/edit_profile.html'
    success_url = reverse_lazy("registration/login.html")

    def get_object(self):
=======
from django.shortcuts import render
from django.views import generic
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from Accounts.forms import CreacionUsuario
from django.urls import reverse_lazy
from .forms import EditProfileForm
from django.core.files.storage import FileSystemStorage


# ACCOUNTS PAGE
def accounts_page(request):
    return render(request, "registration/accounts.html")

def signup_estudio(request):
    
    form = CreacionUsuario

    if request.method == 'POST':
        
        form = CreacionUsuario(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            form.save()
            return render(request, "EstudioApp/index.html", {'msj': f'Se creó el usuario {username}'})


        else: 
            form = CreacionUsuario()
    
    return render(request, "registration/signup.html", {'form': form})

# LOGIN
def login_estudio(request):

    if request.method == 'POST':
        form = AuthenticationForm(request, data = request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)

                return render(request, "registration/accounts.html", {'msj':f'Bienvenido {user}'})

            else:
                return render(request, "registration/login.html", {'form' : form, 'msj': 'Error, los datos son incorrectos'})
        
        else:
            return render(request, "registration/login.html", {'form' : form, 'msj' : 'Usuario y/o contraseña incorrectos'})

    form = AuthenticationForm()

    return render(request, "registration/login.html", {'form' : form})

# EDITAR PERFIL

class UserEditView(generic.UpdateView):
    form_class = EditProfileForm
    template_name = 'registration/edit_profile.html'
    success_url = reverse_lazy("registration/login.html")

    def get_object(self):
>>>>>>> origin/main
        return self.request.user