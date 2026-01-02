from django.shortcuts import render
from .models import Universited
# Create your views here.




def universited(request):
    universitedlar = Universited.objects.all()
    return render(request, 'universited/universited_list.html', {
        'universitedlar': universitedlar
    })


def universited_detail(request, pk):
    universited = Universited.objects.get(id=pk)
    return render(request, 'universited/universited_detail.html', {
        'universited': universited
    })





