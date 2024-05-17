import json

from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.http.response import HttpResponse
from datetime import date

from web.models import Subscribe, Product

# Create your views here.
def index(request):
    products = Product.objects.all()
    today = date.today()
    products_len = len(products) - 9

    phone_category = Product.objects.filter(product_category='phone')
    computer_category = Product.objects.filter(product_category='computer')
    smartwatch_category = Product.objects.filter(product_category='smart_watch')
    headphone_category = Product.objects.filter(product_category='headphone')
    games_category = Product.objects.filter(product_category='gaming')
    camera_category = Product.objects.filter(product_category='camera')







    context = {
        "products":products[:products_len:-1],
        "today":today,
        "phone_category":phone_category[:8:-1],
        "computer_category":computer_category[:8:-1],
        "smartwatch_category":smartwatch_category[:8:-1],
        "headphone_category":headphone_category[:8:-1],
        "games_category":games_category[:8:-1],
        "camera_category":camera_category[:8:-1],
    }

    
    return render(request, 'home.html', context=context)


def view_products(request):
    return render(request, 'product-detail.html')

def product(request, id):
    instance = get_object_or_404(Product.objects.filter(id=id))
    usercatogary = instance.product_category
    category = Product.objects.filter(product_category=usercatogary)
    context = {
        "instance":instance,
        "category_lists" : category[:4:-1]
    }
    return render(request,'product-detail.html', context=context)


def products_list(request):

    products = Product.objects.all()
    today = date.today()
    products_len = len(products) - 21

    context = {
        "products":products[:products_len:-1],
        "today":today
    }
    
    return render(request, 'product-list.html', context=context)




def subscribe(request):
    email = request.POST.get('email')
    
    if not Subscribe.objects.filter(email=email).exists():
        Subscribe.objects.create(
            email=email
        )

        response_data = {
            'status':"success",
            'title':"Successfully registered",
            "message":"You subscribed to out newsletter successfully"
        }
        
    else:
        response_data = {
            'status':"error",
            'title':"You are already subscribed",
            "message":"You already a memeber, No need to register again"
        }


    return HttpResponse(json.dumps(response_data),content_type="applicatoin/javascript")