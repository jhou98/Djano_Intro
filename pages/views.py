from django.shortcuts import render

# Create your views here.
# Anytime to create a new webpage, create a view 

def home(request):
    return render(request, "home.html", {})

def about(request):
    my_name = "Hello, My Name is Jack"
    return render(request, "about.html", {"key_name": my_name})

def contact(request):
    from pages.namer import email
    return render(request, "contact.html", {"contact_info": email})
