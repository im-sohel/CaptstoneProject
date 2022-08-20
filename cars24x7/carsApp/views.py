from django.shortcuts import render
from . import models

def apphome(request):
    return render(request, 'carsApp/apphome.html')

def bookvisit(request):
    return render(request, 'carsApp/bookvisit.html')

def visitconf(request):
    if(request.POST):
     formdata = request.POST
     obj = models.AppoinMentData(name=formdata['user_name'], email=formdata['email_id'], mobile=formdata['mobile_no'], date=formdata['visit_date'])
     obj.save()
     context ={'data': formdata}
     return render(request, 'carsApp/visitconfirm.html', context)
    else:
        return render(request, 'carsApp/bookvisit.html')
