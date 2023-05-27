from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import Contact
# Create your views here.


def index(request):
    return render(request, 'index.html')

def vrshome(request):
    return render(request, 'vrshome.html')

def about(request):
    return render(request, 'about.html')


def contact(request):
    error = ""
    if request.method == "POST":
        name = request.POST['w3lName']
        email = request.POST['w3lSender']
        msg = request.POST['w3lMessage']
    try:
        Contact.objects.create(name=name, email=email, msg=msg)
        error = "no"
    except:
        error = "yes"
    else:
        error = "yes"
    d = {}
    d['error'] = error
    return render(request, 'contact.html', d)


def services(request):
    return render(request, 'services.html')




def signup(request):
    error = ""
    if request.method == "POST":
        name = request.POST['uname']
        email = request.POST['uemail']
        password = request.POST['upass']
    try:
        User.objects.create_user(
            username=email,  password=password, first_name=name)
        error = "NO"
    except:
        error = "YES"
    d = {'error': error}

    return render(request, 'signup.html', d)


def login(request):
    error = ""
    if request.method == "POST":
        uemail = request.POST["lemail"]
        password = request.POST["lpass"]

        root = authenticate(username=uemail, password=password)
        try:
            if root:
                login(request, root)
                error = "NO"
            else:
                error = "NO"
        except:
            error = "NO"
    d = {"error": error}

    return render(request, 'login.html', d)
