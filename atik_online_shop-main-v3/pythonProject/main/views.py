import uuid


from django.shortcuts import render, get_object_or_404, HttpResponseRedirect

from .forms import ProductForm, ProductChangeForm

from .models import *

from django.contrib.admin.views.decorators import staff_member_required
# Create your views here.

from django.core.paginator import Paginator




def menu(request, slug=None , page=1):
    if slug:
        category = Category.objects.get(slug=slug)
        product = Product.objects.filter(cat=category)
    else:

        product = Product.objects.all()
    paginator = Paginator(object_list=product, per_page=9)
    products_paginator = paginator.page(page)
    context={'category':Category.objects.all(), 'product': products_paginator}

    return render(request, 'main/menu.html', context=context)

def main(request):



    return render(request, 'main/main.html')




def detail(request,  slug):
    product_info = get_object_or_404(Product, slug=slug, available=True)



    return render(request, 'main/detail.html',  {'product':product_info})


def cool_basket_add(request, product_id):
    if 'username' in request.session:
        pass
    else:
        request.session['username'] = str(uuid.uuid4())
    if 'basket' not in request.session:
        request.session['basket'] = []
    basket = request.session['basket']
    del request.session['basket']
    request.session['basket'] = basket + [product_id]


    product = Product.objects.get(id=product_id)
    baskets = BasketCool.objects.filter(user=request.session['username'], product=product)


    if not baskets.exists():
        BasketCool.objects.create(user=request.session['username'], product=product, quantity=1)

    else:
        basket = baskets.first()
        basket.quantity += 1
        basket.save()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])

def cool_basket_remove(request, basket_id):
    request.session['basket'] = list(filter(lambda x:False if x == basket_id else True,request.session['basket']))
    return HttpResponseRedirect(request.META['HTTP_REFERER'])
