from django.contrib.auth import login, authenticate
from django.shortcuts import render
from .forms import SignUpForm
from django.http import HttpResponse

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            number_for_func = 0
            user.refresh_from_db()  # load the profile instance created by the signal
            user.profile.birth_date = form.cleaned_data.get('birth_date')
            user.save()
            user.profile.username = form.cleaned_data.get('username')
            user.save()
            user.profile.first_name = form.cleaned_data.get('first_name')
            user.save()
            user.profile.last_name = form.cleaned_data.get('last_name')
            user.save()
            user.profile.email = form.cleaned_data.get('email')
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return HttpResponse("Registration accepted")
    else:
        form = SignUpForm()
    return render(request, 'Points/templates/signup.html', {'form': form})