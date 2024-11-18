from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def hydjobsinfo(request):
    return HttpResponse('<h1>Hyderabad Jobs</h1>')
def bngjobsinfo(request):
    return HttpResponse('<h1>Bangalore Jobs</h1>')
def punejobsinfo(request):
    return HttpResponse('<h1>Pune Jobs</h1>')
def mumbaijobsinfo(request):
    return HttpResponse('<h1>Mumbai Jobs</h1>')