from django.http import HttpResponse
from django.shortcuts import render

from .models import Data


# Create your views here.
def insertdata(request):
    if request.method == 'POST':  # Check is the user has posted the data /
        if request.POST.get('name') and request.POST.get('gender') and request.POST.get('course') and request.POST.get(
                'level'):  # checks if there is unfilled field
            details = Data()
            details.name = request.POST.get('name')
            details.gender = request.POST.get('gender')
            details.course = request.POST.get('course')
            details.level = request.POST.get('level')
            details.save()
            return render(request, 'senddata/data.html')
        else:
            return HttpResponse('Error occurred')
    else:
        return render(request, 'senddata/index.html')

def viewdata(request):
    details = Data.objects.all()
    return render(request, 'senddata/details.html', {'details': details})