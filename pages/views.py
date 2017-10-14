from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'pages/index.html')


def contact(request):
    return render(request, 'pages/contact.html')


def apply(request):
    return render(request, 'pages/apply.html')


def faq(request):
    return render(request, 'pages/faq.html')
