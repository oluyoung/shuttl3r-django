from django.shortcuts import render
from .models import User, ShuttleOrder, ShuttleOrder

# Create your views here.
def index(request):
    return render(request, 'shuttle/index.html')
