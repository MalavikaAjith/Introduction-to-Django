from django.shortcuts import render

# Create your views here.
def func(request):
    return render(request,'img1.html')

def fun(request):
    return render(request,'img2.html')
