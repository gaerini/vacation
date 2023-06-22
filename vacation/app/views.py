from django.shortcuts import render

# Create your views here.
def home(request):
    #logic here
    return render(request, "home.html")