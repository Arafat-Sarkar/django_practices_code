from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('this is home page please go the first_app')
    # return render(request, 'base.html',)