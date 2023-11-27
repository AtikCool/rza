from django.urls import path, re_path
from . import views
app_name = 'main'
urlpatterns = [

    re_path(r'^menu/category/(?P<slug>\D+)(?:/query/(?P<search_slug>\D+))?$', views.menu),

    path('', views.main, name='main'),
    path('menu', views.menu, name='menu'),
    path('menu/page/<int:page>/', views.menu,  name='paginator'),
    path('cool_baskets/add/<int:product_id>/', views.cool_basket_add, name='basket_add'),
    path('baskets/remove/<int:basket_id>', views.cool_basket_remove, name='basket_remove'),




]