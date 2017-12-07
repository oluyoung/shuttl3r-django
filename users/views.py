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
#
from django.core.mail import send_mail
from .tokens import account_activation_token
from .forms import UserForm, UserUpdateForm
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
            send_mail(
                mail_subject,
                '',
                'freehand@sendgrid.net',
                [to_email],
                fail_silently=False,
                html_message=message,
            )

            response = HttpResponse()
            response.write('<h2 style="text-align:center;font-family:arial;padding:2% 1.5%;background-color:darkcyan;color:#f0f0f0;font-size:1.2em;">Kindly confirm your email address to activate your account</h2>')

            return response

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
        return redirect('/users/user/dashboard')
    else:
        response = HttpResponse()
        response.write('<h2 style="text-align:center;font-family:arial;padding:2% 1.5%;background-color:darkcyan;color:#f0f0f0;font-size:1.2em;">Activation link is invalid!</h2>')
        if user is not None:
            current_site = get_current_site(request)
            message = render_to_string('registration/acc_active_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user)
            })
            mail_subject = 'Activate your FreehandNG account.'
            to_email = user.email
            send_mail(
                mail_subject,
                '',
                'freehand@sendgrid.net',
                [to_email],
                fail_silently=False,
                html_message=message,
            )

        return response()


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
        mrd, mrc, mrs, has_order = False, False, False, False

        if DriverOrder.objects.filter(user=user).count() > 0:
            has_order, mrd = True, True
            most_recent_driver_order = DriverOrder.objects.filter(user=user).order_by('-id')[0]
            driver_orders = DriverOrder.objects.filter(user=user).order_by('-id')[1:]
        if CarOrder.objects.filter(user=user).count() > 0:
            has_order, mrc = True, True
            most_recent_car_order = CarOrder.objects.filter(user=user).order_by('-id')[0]
            car_orders = CarOrder.objects.filter(user=user).order_by('-id')[1:]
        if ShuttleOrder.objects.filter(user=user).count() > 0:
            has_order, mrs = True, True
            most_recent_shuttle_order = ShuttleOrder.objects.filter(user=user).order_by('-id')[0]
            shuttle_orders = ShuttleOrder.objects.filter(user=user).order_by('-id')[1:]

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
            'mrs': mrs,
            'has_order': has_order
        }

        return render(request, 'users/dashboard.html', context)


@login_required
def account(request):
    req_user = None

    if request.user.is_authenticated:
        req_user = request.user
        user_email = req_user.email

    form = UserUpdateForm(request.POST or None, instance=req_user)
    if form.is_valid():
        user = form.save(commit=False)
        if form.cleaned_data.get('email') != user_email:
            user.is_active = False
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

            mail_subject = 'Activate your FreehandNG account.'
            to_email = form.cleaned_data.get('email')
            send_mail(
                mail_subject,
                '',
                'freehand@sendgrid.net',
                [to_email],
                fail_silently=False,
                html_message=message,
            )

            response = HttpResponse()
            response.write('<h2 style="text-align:center;font-family:arial;padding:2% 1.5%;background-color:darkcyan;color:#f0f0f0;font-size:1.2em;">Kindly verify your new email.</h2>')

            return response

        else:
            user.save()

    return render(request, 'users/account.html', {'form': form, 'user': req_user})


@login_required
def delete_account(request):
    if request.user.is_authenticated:
        user = request.user
        user = User.objects.get(pk=user.id)
        user.is_active = False
        user.save()
        return redirect('/users/logout')
