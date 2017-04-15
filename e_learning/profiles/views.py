from django.shortcuts import render, redirect
from django.template import RequestContext
from django.contrib.auth.decorators import login_required

from forms import User_Edit

# Create your views here.
def profile(request):
    user = request.user.username
    email = request.user.email
    return render(request,'profile/profile.html',{
        'user':user,
        'email':email,
    })

def edit_profile(request):
    current_user = request.user
    user_form = User_Edit(data=request.POST or None,
                          instance=current_user, user=current_user)
    if request.method == 'POST':
        if user_form.is_valid():
            user_form.save()
            return redirect('/profile')
    return render(request,'profile/edit_profile.html',{
        'form':user_form,
    })