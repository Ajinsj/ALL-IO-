"""
URL configuration for AIO project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path,include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
     path('admin', admin.site.urls),
     path('',include('maxhome.urls')),
     path('home',include('maxhome.urls')),
     path('login',include('maxhome.urls')),
     path('register',include('maxhome.urls')),
     path('Order',include('maxhome.urls')),
     path('Deal',include('maxhome.urls')),
     path('Filter',include('maxhome.urls')),
     path('account',include('maxhome.urls')),
     path('cart',include('maxhome.urls')),
     path('accessoriess',include('maxhome.urls')),
     path('groceryss',include('maxhome.urls')),
     path('sportss',include('maxhome.urls')),
     path('fashionss',include('maxhome.urls')),
     path('homeappliencess',include('maxhome.urls')),
     path('toyss',include('maxhome.urls')),
     path('nutritionss',include('maxhome.urls')),
     path('shoess',include('maxhome.urls')),
     path('buy',include('maxhome.urls')),
    
    
]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
