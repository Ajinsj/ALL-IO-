from django.urls import path
from . import views


urlpatterns = [
     path('', views.home,name='home'),
     path('home', views.home,name='home'),
     path('login', views.login,name='login'),
     path('register', views.register,name='Register'),
     path('Order', views.Order,name='Order'),
     path('Deals', views.Deals,name='Deals'),
     path('filter', views.filter,name='filter'),
     path('account', views.account,name='account'),
     path('cart', views.cart,name='cart'),
     path('selectedproductss', views.selectedproductss,name='selectedproductss'),
     path('accessoriess', views.accessoriess,name='accessoriess'),
     path('groceryss', views.groceryss,name='grocerys'),
     path('sportss', views.sportss,name='sportss'),
     path('fashionss', views.fashionss,name='fashionss'),
     path('homeappliencess', views.homeappliencess,name='homeappliencess'),
     path('toyss', views.toyss,name='toyss'),
     path('nutritionss', views.nutritionss,name='nutritionss'),
     path('shoess', views.shoess,name='shoess'),
     path('buy', views.buy,name='buy'),
    
]