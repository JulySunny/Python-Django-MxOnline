from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def hello(request):
    # return render(request,"HelloWorld")
    return HttpResponse("hello World")