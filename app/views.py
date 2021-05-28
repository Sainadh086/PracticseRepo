from django.shortcuts import render
# Create your views here.

def index(request):

    return render(request, 'index.html', {'name':"Sainadh Cherukumalli"})


def project(request):

    return render(request, 'projects.html', {'name':"Projects"})

def model(request):

    return render(request, 'model.html', {'name':"Models"})

def about(request):

    return render(request, 'about.html', {'name':"About"})

def test(request):

    return render(request, 'portfolio-details.html', {'name':"About"})