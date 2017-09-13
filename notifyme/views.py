from django.shortcuts import render
from .models import Notification

def home(request):
    
    c = {}
    if request.user.is_authenticated():
        c['notifications'] = Notification.objects.filter(user=request.user)    
    return render(request,'notifyme/home.html',c)

