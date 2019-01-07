from django.shortcuts import render

# Create your views here.
# Anytime to create a new webpage, create a view 

def home(request):
    return render(request, "home.html", {})

def about(request):
    return render(request, "about.html", {})

def contact(request):
    return render(request, "contact.html", {})
