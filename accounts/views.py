from django.views.generic.edit import CreateView
from django.contrib.auth.views import LoginView
from accounts.forms import MyUserCreationForm


class RegisterView(CreateView):
    form_class = MyUserCreationForm
    success_url = '/login'
    template_name = 'accounts/register.html'


class AuthorizationView(LoginView):
    template_name = 'accounts/login.html'
