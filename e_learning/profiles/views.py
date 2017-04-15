from django.shortcuts import render

# Create your views here.
def profile(request):
    user = request.user.username
    email = request.user.email
    return render(request,'profile/profile.html',{
        'user':user,
        'email':email,
    })

def edit_profile(request):
    return render(request,'profile/edit_profile.html')