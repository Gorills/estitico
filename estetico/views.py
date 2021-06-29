from django.shortcuts import render
from .models import Services, Special, Departments

# Create your views here.
def home(request):


    return render(request, 'estetico/home.html')


def blog(request):


    return render(request, 'estetico/blog.html')

def contact(request):


    return render(request, 'estetico/contact.html')

def special(request):


    return render(request, 'estetico/special.html')



def price(request):

    context = {

        'services': Services.objects.all()
    }

    return render(request, 'estetico/price.html', context)



def special_detail(request, slug):

    context = {
        'special': Special.objects.get(slug=slug),
        'image': Special.objects.get(slug=slug).images.first(),
        'images': Special.objects.get(slug=slug).images.all()[1:],
    }

    return render(request, 'estetico/special_view.html', context)


def services_detail(request, slug):

    context = {

        'service': Services.objects.get(slug=slug),
        'image': Services.objects.get(slug=slug).images.first(),
        'images': Services.objects.get(slug=slug).images.all()[1:],


    }


    return render(request, 'estetico/services_detail.html', context)

def review_list(request):

    return render(request, 'estetico/review_list.html')