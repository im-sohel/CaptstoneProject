from django.shortcuts import render

def home(request):
 return render(request, 'home.html')

def contact(request):
    return render(request, 'contactus.html')


def buypolicy(request):
    if(request.POST):
     formdata = request.POST
     context ={'data': formdata}
     return render(request, 'confirm.html', context)
    else:
        return render(request, 'buypolicy.html')

