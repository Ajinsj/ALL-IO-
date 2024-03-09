from django.shortcuts import render,redirect,HttpResponse
from django.contrib import messages
from  django.contrib.auth import authenticate
from maxhome.models import Trendings,userregister,accessories,Fashions,HomeAppliences,Toys,sports,NutritionsandMore,shoesandcheppals,vegetables,Trendings
from maxhome.form import userregForm
from maxhome.logform import userlogForm
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
@csrf_exempt
def home(request):
    trend=Trendings.objects.filter(status=0)                                   
    return render(request,"html/home.html",{"Trendings":trend})
def login(request):  
     if request.method == 'POST':
        login= userlogForm(request.POST)
        if login.is_valid():
         login.save()
         return redirect('home')
     else: 
         usersid=userlogForm()
         return render(request,"html/Login.html",{"usersid":usersid})
def register(request):
     if request.method == 'POST':
        userregister = userregForm(request.POST)
        if userregister.is_valid():
            userregister.save()
            messages.success(request, 'Registration successful. You can now login.')
            return redirect('login')
        else:
            messages.error(request, 'Registration failed. Please correct the errors below.')
     else:
       
            
       
      userid = userregForm()   
      return render(request,"html/Register.html",context={"userid":userid})
def Order(request):
                                    
    return render(request,"html/orders.html")
def Deals(request):
                                 
    return render(request,"html/deals.html")
def filter(request):
                                 
    return render(request,"html/filters.html")
def account(request):
                                 
    return render(request,"html/account.html")
def selectedproductss(request):
    
    
    # Add the product to the user's cart
   
    
    # Redirect the user to the cart page
                            
    return render(request,"html/selectedproducts.html")
def cart(request):
                                 
    return render(request,"html/cart.html")
def accessoriess(request):
    acces=accessories.objects.filter(status=0)
    
    return render(request,"html/accessories.html",{"accessories":acces})
def fashionss(request):
    fash=Fashions.objects.filter(status=0)
                                 
    return render(request,"html/fashion.html",{"Fashions":fash})
def groceryss(request):
    groc=vegetables.objects.filter(status=0)
                                 
    return render(request,"html/grocery.html",{"vegitables":groc})
def sportss(request):
    sport=sports.objects.filter(status=0)
                                 
    return render(request,"html/sports.html",{"sports":sport})
def homeappliencess(request):
    homeapp=HomeAppliences.objects.filter(status=0)
                                 
    return render(request,"html/homeappliences.html",{"HomeAppliences":homeapp})
def toyss(request):

    toy=Toys.objects.filter(status=0)                            
    return render(request,"html/Toys.html",{"Toys":toy})
def nutritionss(request):
    nuttri=NutritionsandMore.objects.filter(status=0)
                                 
    return render(request,"html/nutrition.html",{"NutritionsandMore":nuttri})
def shoess(request):
     shoe=shoesandcheppals.objects.filter(status=0)                           
     return render(request,"html/footwear.html",{"shoesandcheppals":shoe})

def buy(request):#cart
    return render(request,"html/buy .html")

