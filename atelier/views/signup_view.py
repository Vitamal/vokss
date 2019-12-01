from django.shortcuts import render
from django.contrib.auth import login, authenticate
from atelier.forms import SignUpForm
from django.shortcuts import render, redirect


def signup_view(request):
    """
    We are using refresh_from_db() method to handle synchronism issue,
    basically reloading the database after the signal, so by this method our profile instance will load.
    Once profile instance loaded, set the cleaned data to the fields and save the user model.
    """
    form = SignUpForm(request.POST)
    if form.is_valid():
        user = form.save()
        user.refresh_from_db()
        user.profile.atelier = form.cleaned_data.get('atelier')
        user.profile.is_tailor = form.cleaned_data.get('is_tailor')
        user.profile.is_seamstress = form.cleaned_data.get('is_seamstress')
        user.save()
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password=password)
        login(request, user)
        return redirect('atelier:home')
    else:
        form = SignUpForm()
    return render(request, 'atelier/signup.html', {'form': form})