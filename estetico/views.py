
from django.shortcuts import render
from .models import Services, Special, Departments, Review
from blog.models import Post



# Create your views here.
def home(request):

    context = {
        'first': Services.objects.get(id=1),
        'second': Services.objects.get(id=2),
        'third': Services.objects.get(id=3),
        'fourth': Services.objects.get(id=4),
        'fifth': Services.objects.get(id=5),
        'sixth': Services.objects.get(id=6),
        'posts': Post.objects.all().order_by('-id')[:4],
       
        

    }



    return render(request, 'estetico/home.html', context)




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

    context = {
        'reviews': Review.objects.all().order_by('-id')
    }

    return render(request, 'estetico/review_list.html', context)


def privacy(request):

    return render(request, 'estetico/privacy.html')


def user_agreement(request):

    return render(request, 'estetico/user_agreement.html')


def pravovaya_informaciya(request):

    return render(request, 'estetico/pravovaya-informaciya.html' )