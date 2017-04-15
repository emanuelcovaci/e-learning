from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.contrib.auth import logout

from .forms import LoginForm, UserRegisterForm,PasswordResetForm


# Create your views here.

@login_required
def logout_view(request):
    logout(request)
    return redirect(reverse('home'))


def login_page(request):
    if request.user.is_authenticated():
        return redirect('/')
    else:
        errors = []
        form = LoginForm(request.POST)
        if request.method == 'POST':
            if form.is_valid():
                user = authenticate(username=form.cleaned_data['username'],
                                    password=form.cleaned_data['password'])
                if user is not None:
                    login(request, user)
                    return redirect('/')

                else:
                    errors.append('Incorrect username or password')

            else:
                errors.append('Invalid form')
        return render(request, "authentication/logIn.html", {
            'form': form,
            'errors': errors})


def register_page(request):
    form = UserRegisterForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.instance.set_password(form.cleaned_data['password'])
            form.save()
            user = authenticate(username=form.instance.username,
                                password=form.cleaned_data['password'])
            login(request, user)
            return redirect('/')
    return render(request, "authentication/register.html", {
        'form': form,
    })

@login_required
def change_password(request):
    errors = []
    form = PasswordResetForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            password_old = form.cleaned_data['old_password']
            password_new = form.cleaned_data['password_1']
            check = password_new == form.cleaned_data['password_2']
            if not check:
                errors.append('Those two password are not the same')
            elif request.user.check_password(password_old):
                if password_new.isdigit():
                    errors.append('Password is entirely numeric')
                else:
                    request.user.set_password(password_new)
                    request.user.save()
                    user = authenticate(username=request.user.username,
                                        password=password_new)
                    login(request, user)
                    return redirect('/')
            else:
                errors.append('Incorrect old password')
        else:
            errors.append('Invalid form')
    return render(request, "authentication/change_password.html",
                  {'form': form,
                   'errors': errors})
