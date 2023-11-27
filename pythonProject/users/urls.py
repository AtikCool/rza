from django.urls import path
from . import views
app_name = 'users'
urlpatterns = [

    path('cool_profile/', views.cool_profile, name='profile')

]