from django.shortcuts import render, redirect
from django.template import RequestContext
from django.contrib.auth.decorators import login_required

from forms import UserEdit, AccountEdit


# Create your views here.
@login_required
def profile(request):
    user = request.user.username
    email = request.user.email
    return render(request, 'profile/profile.html', {
        'user': user,
        'email': email,
    })

@login_required
def edit_profile(request):
    current_user = request.user
    user_form = UserEdit(data=request.POST or None,
                         instance=current_user, user=current_user)
    account_form = AccountEdit(request.POST or None,
                               request.FILES or None,
                               instance=current_user.account)
    if request.method == 'POST':
        if user_form.is_valid() and account_form.is_valid():
            user_form.save()
            account_form.save()
            return redirect('/profile')
    print account_form.errors
    return render(request, 'profile/edit_profile.html', {
        'form': user_form,
        'form_acc': account_form,
    })
