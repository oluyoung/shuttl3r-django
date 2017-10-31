from django.http import HttpResponse
from django.contrib.auth import login, authenticate
#
from django.contrib.sites.shortcuts import get_current_site
#
from django.utils.encoding import force_bytes, force_text
#
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
#
from django.template.loader import render_to_string
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
#
from django.core.mail import EmailMessage
from .tokens import account_activation_token
from .forms import UserForm
from .models import User


def register(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        user.is_active = False
        password = form.cleaned_data.get('password')
        user.set_password(password)
        user.save()
        current_site = get_current_site(request)
        message = render_to_string('registration/acc_active_email.html',{
            'user':user,
            'domain':current_site.domain,
            'uid':urlsafe_base64_encode(force_bytes(user.pk)),
            'token':account_activation_token.make_token(user)
        })
        mail_subject = 'Activate your FreehandNG account.'
        to_email = form.cleaned_data.get('email')
        email = EmailMessage(mail_subject, message, to=[to_email])
        email.send()
        return HttpResponse('Please confirm your email address to complete the registration')

    return render(request, 'registration/register.html', {"form": form})


def activate(request, uidb64, token, backend='django.contrib.auth.backends.ModelBackend'):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user, backend)
        # return redirect('home') or previous URL
        return HttpResponse('Thank you for your email confirmation. Now you can login to your account.')
    else:
        return HttpResponse('Activation link is invalid!')


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
