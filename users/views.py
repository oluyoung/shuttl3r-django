from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from .forms import UserForm
from .models import User


def register(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        password = form.cleaned_data.get('password')
        user.set_password(password)
        user.save()

        return redirect("/")

    return render(request, 'registration/register.html', {"form": form})


@login_required
def dashboard(request):
    return render(request, 'users/dashboard.html', {})


@login_required
def account(request, id):
    user = get_object_or_404(User, pk=id)
    form = UserForm(request.POST or None, instance=user)
    if form.is_valid():
        form.save()

        return HttpResponseRedirect(user.get_absolute_url())

    return render(request, 'users/account.html', {'form': form})
