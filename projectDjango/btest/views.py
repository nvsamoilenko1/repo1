from .models import Bb
from django.shortcuts import render
 
def index(request):
    bbs = Bb.objects.order_by('-published')
    return render(request, "btest/index.html", {'bbs': bbs})


