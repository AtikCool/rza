from django.shortcuts import render, HttpResponseRedirect
from django.contrib import auth
from functools import reduce
from main.models import *
from django.contrib.auth.decorators import login_required
from django.urls import reverse


from main.models import *



# Create your views here.


def cool_profile(request):
    def count_elements(lst):
         return {i: lst.count(i) for i in lst}
    products_id = count_elements(request.session['basket'])
    products = map(lambda x:Product.objects.get(id=x), products_id.keys())
     
    basket = BasketCool.objects.filter(user=request.session['username'])  



    if request.session['basket'] == []:
        total_sum = 0
        total_quantity = 0
    else:
        products_id = count_elements(request.session['basket'])
        products = map(lambda x:Product.objects.get(id=x), products_id.keys())
        basket = BasketCool.objects.filter(user=request.session['username'])
        price_in_id = {}
        for x in products_id:
            price_in_id[Product.objects.get(id=x).price] = products_id[x]
        total_sum = reduce(lambda x, y:(x[0]*x[1])+(y[0]*y[1]), list(price_in_id.items()))
        total_quantity = sum(products_id.values())
    return render(request, 'main/basket.html', {'products':products, 'basket':basket ,'total_sum':total_sum, 'total_quantity':total_quantity})


