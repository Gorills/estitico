from django.shortcuts import render
from .models import Specialist

# Create your views here.

def specialist(request):

    context = {
        'specialists': Specialist.objects.all()
    }

    return render(request, 'specialist/specialist.html', context)


def specialist_detail(request, slug):

    context = {
        'specialist': Specialist.objects.get(slug=slug)
    }

    return render(request, 'specialist/specialist_detail.html', context)