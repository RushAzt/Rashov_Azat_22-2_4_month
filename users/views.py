from django.shortcuts import render, redirect
from users.forms import LoginForm, RegisterForm
from django.contrib.auth import login, authenticate, logout
from users.utils import get_user_from_request
from django.contrib.auth.models import User
from django.views.generic import CreateView


# Create your views here.

class LoginView(CreateView):
    form_class = LoginForm
    template_name = 'users/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        return {
            'form': kwargs['form'] if kwargs.get('form') else self.form_class,
            'user': get_user_from_request(self.request)
        }

    def post(self, request, *args, **kwargs):
        form = self.form_class(data=request.POST)

        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data.get('username'),
                password=form.cleaned_data.get('password')
            )
            if user:
                login(request, user)
                return redirect('/product')
            else:
                form.add_error('username', 'bad request')

        return render(request, self.template_name, context=self.get_context_data(form=form))


class LogoutView(CreateView):
    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect('/product')


class RegisterView(CreateView):
    template_name = 'users/register.html'
    form_class = RegisterForm

    def get_context_data(self, *, object_list=None, **kwargs):
        return {
            'form': kwargs['form'] if kwargs.get('form') else self.form_class
        }

    def post(self, request, *args, **kwargs):
        form = self.form_class(data=request.POST)

        if form.is_valid():
            if form.cleaned_data.get('password1') == form.cleaned_data.get('password2'):
                user = User.objects.create_user(
                    username=form.cleaned_data.get('username'),
                    password=form.cleaned_data.get('password')
                )
                login(request, user)
                return redirect('/product')
            else:
                form.add_error('password', 'password do not match!')

        return render(request, self.template_name, context=self.get_context_data(form=form))
