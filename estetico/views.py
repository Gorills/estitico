from django.shortcuts import render

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


    return render(request, 'estetico/price.html')

def special_view(request):

    return render(request, 'estetico/special_view.html')


def servises_detail(request):

    return render(request, 'estetico/servises_detail.html')

def review_list(request):

    return render(request, 'estetico/review_list.html')