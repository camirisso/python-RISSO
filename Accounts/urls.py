from django.urls import path
from Accounts import views 
from django.contrib.auth.views import LogoutView 
from .views import UserEditView
from django.contrib.auth import views as auth_views


urlpatterns = [
    # ACCOUNTS PAGE
    path('accounts/', views.accounts_page, name = 'accounts'),
    # SIGNUP
    path('signup/', views.signup_estudio, name = 'signup'),
    # LOGIN
    path('login/', views.login_estudio, name = 'login'),
    # LOGOUT
    path('logout/', LogoutView.as_view(template_name='registration/logout.html'), name = 'logout'),
    # EDITAR PERFIL
    path('edit_profile', UserEditView.as_view(), name = 'edit_profile'),
]
