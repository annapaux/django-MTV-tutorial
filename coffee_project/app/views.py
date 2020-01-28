from django.shortcuts import render
from django.http import HttpResponse

from app.models import User
import datetime

def index(request):
    today = datetime.datetime.now().date()
    users = User.objects.all()
    data = {'today':today, 'users':users}
    return render(request, "index.html", data)
