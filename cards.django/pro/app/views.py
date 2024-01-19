from django.shortcuts import render

from . models import card


# Create your views here.
def func(request):
    imag = {
        'img': card.objects.all()
    }
    return render(request,'cards.html',imag)
