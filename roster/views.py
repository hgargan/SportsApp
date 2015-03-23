from django.shortcuts import render, get_object_or_404 
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def home(request):
    context = {'message': 'This is a dynamic message variable.'}
    return render(request, "base.html", context)
    
