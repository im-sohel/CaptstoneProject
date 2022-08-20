from django.shortcuts import render

def ProjectHomePage(request):
    return render(request, 'home.html')