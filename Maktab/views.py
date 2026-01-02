from django.shortcuts import render
from .models import Maktab
# Create your views here.



def maktab(request):
    maktablar = Maktab.objects.all()
    return render(request, 'maktab/maktab_list.html', {
        'maktablar': maktablar
    })




def maktab_detail(request, pk):
    maktab = Maktab.objects.get(id=pk)
    return render(request, 'maktab/maktab_detail.html', {
        'maktab': maktab
    })