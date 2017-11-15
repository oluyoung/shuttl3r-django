from django.http import HttpResponse
from django.contrib.auth import login
#
from django.contrib.sites.shortcuts import get_current_site
#
from django.utils.encoding import force_bytes, force_text
#
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
#
from django.template.loader import render_to_string
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
#
from django.core.mail import EmailMessage
from .tokens import account_activation_token
from .forms import UserForm
from .models import User
from drivers.models import DriverOrder
from cars.models import CarOrder
from shuttle.models import ShuttleOrder


def register(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
        form = UserForm(request.POST or None)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            password = form.cleaned_data.get('password')
            user.set_password(password)
            user.save()
            current_site = get_current_site(request)
            message = render_to_string('registration/acc_active_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user)
            })
            mail_subject = 'Activate your FreehandNG account.'
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(mail_subject, message, to=[to_email])
            email.send()
            # need to return HTML page
            return HttpResponse('Kindly confirm your email address to complete the registration')

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
    # if user hasn't made any orders yet
    if request.user.is_authenticated:
        user = request.user
        most_recent_driver_order = None
        driver_orders = None
        most_recent_car_order = None
        car_orders = None
        most_recent_shuttle_order = None
        shuttle_orders = None
        mrd, mrc, mrs = False, False, False

        if DriverOrder.objects.filter(user=user).count() > 0:
            mrd = True
            most_recent_driver_order = DriverOrder.objects.filter(user=user).order_by('-id')[0]
            driver_orders = DriverOrder.objects.filter(user=user).order_by('-id')[1:10]
        if CarOrder.objects.filter(user=user).count() > 0:
            mrc = True
            most_recent_car_order = CarOrder.objects.filter(user=user).order_by('-id')[0]
            car_orders = CarOrder.objects.filter(user=user).order_by('-id')[1:10]
        if ShuttleOrder.objects.filter(user=user).count() > 0:
            mrs = True
            most_recent_shuttle_order = ShuttleOrder.objects.filter(user=user).order_by('-id')[0]
            shuttle_orders = ShuttleOrder.objects.filter(user=user).order_by('-id')[1:10]

        context = {
            'user': user,
            'mrd_order': most_recent_driver_order,
            'd_orders': driver_orders,
            'mrc_order': most_recent_car_order,
            'c_orders': car_orders,
            'mrs_order': most_recent_shuttle_order,
            's_orders': shuttle_orders,
            'mrd': mrd,
            'mrc': mrc,
            'mrs': mrs
        }

        return render(request, 'users/dashboard.html', context)


@login_required
def account(request):
    if request.user.is_authenticated:
        user = request.user
    # use session id as auth
    # make sure user can only view his Profile
    form = UserForm(request.POST or None, instance=user)
    if form.is_valid():
        user = form.save(commit=False)
        user.is_active = False
        password = form.cleaned_data.get('password')
        user.set_password(password)
        user.save()
        current_site = get_current_site(request)
        message = render_to_string('registration/acc_active_email.html', {
            'user': user,
            'domain': current_site.domain,
            'uid': urlsafe_base64_encode(force_bytes(user.pk)),
            'token': account_activation_token.make_token(user)
        })
        mail_subject = 'Verify E-mail change for FreehandNG account.'
        to_email = form.cleaned_data.get('email')
        email = EmailMessage(mail_subject, message, to=[to_email])
        email.send()
        # need to return HTML page
        return HttpResponse('Kindly verify your new email')
        #return HttpResponseRedirect(user.get_absolute_url())

    return render(request, 'users/account.html', {'form': form})
