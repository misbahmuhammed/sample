from django.shortcuts import render,redirect
from django.views import View
from .models import Product,OrderPlaced,Cart,Customer
from .forms import CustomerRegistrationForm,CustomeProfileForm
from django.contrib import  messages
'''def home(request):
 return render(request, 'app/home.html')'''

class ProductView(View):
  def get(self,request):
   studymaterials = Product.objects.filter(category='SM')
   Others = Product.objects.filter(category='O')
   data = {
        'studymaterials':studymaterials,
        'others':Others
   }
   return render(request,'app/home.html',data)


'''def product_detail(request):
 return render(request, )'''

class ProductDetail(View):
    def get(self,request,pk):
     product = Product.objects.get(pk=pk)
     return render(request,'app/productdetail.html',{'product':product})

def add_to_cart(request):
    user = request.user
    product_id = request.GET.get('prod_id')

    return redirect('/cart')


def buy_now(request):
 return render(request, 'app/buynow.html')



def address(request):
    add = Customer.objects.filter(user=request.user)
    return render(request, 'app/address.html',{'add':add,'active':'btn-primary'})


def show_cart(request):
    if request.user.is_authenticated:
        user = request.user
        cart = Cart.objects.filter(user=user)
        return render(request,'app/addtocart.html',{'cart':cart})



def orders(request):
 return render(request, 'app/orders.html')

def change_password(request):
 return render(request, 'app/changepassword.html')

def mobile(request):
 return render(request, 'app/mobile.html')

def login(request):
 return render(request, 'app/login.html')



class CustomerRegistarionView(View):
 def get(self,request):
   form = CustomerRegistrationForm()
   return render(request, 'app/customerregistration.html',{'form':form})
 def post(self,request):
     form = CustomerRegistrationForm(request.POST)
     if form.is_valid():
         messages.success(request,'Congratulations! Registered Successfully..')
         form.save()
     return render(request, 'app/customerregistration.html', {'form': form})
def checkout(request):
 return render(request, 'app/checkout.html')


class ProfileView(View):
    def get(self,request):
       form = CustomeProfileForm()
       return render(request,'app/profile.html',{'form':form, 'active':'btn-primary'})
    def post(self,request):
        form = CustomeProfileForm(request.POST)
        if form.is_valid():
            usr = request.user
            name = form.cleaned_data['name']
            locality = form.cleaned_data['locality']
            city = form.cleaned_data['city']
            state = form.cleaned_data['state']
            zipcode = form.cleaned_data['zipcode']
            reg = Customer(user=usr,name=name,locality=locality,city=city,state=state,zipcode=zipcode)
            reg.save()
            messages.success(request,'Congratulations..! Profile Updated Successfully')
        return render(request,'app/profile.html',{'form':form,'active':'btn-primary'})
