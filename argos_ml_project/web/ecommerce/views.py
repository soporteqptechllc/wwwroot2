from django.shortcuts import render
from django.views import View
# Create your views here.
class ProductsView(View):
    def get(self , request):
        greeting = {}
        greeting['heading'] = "Products"
        greeting['pageview'] = "Ecommerce"
        return render (request,'ecommerce/ecommerce-products.html',greeting)

class ProductDetailView(View):
    def get(self , request):
        greeting = {}
        greeting['heading'] = "Product Detail"
        greeting['pageview'] = "Ecommerce"
        return render (request,'ecommerce/ecommerce-productdetail.html',greeting)       

class OrdersView(View):
    def get(self , request):
        greeting = {}
        greeting['heading'] = "Orders"
        greeting['pageview'] = "Ecommerce"
        return render (request,'ecommerce/ecommerce-orders.html',greeting)          

class CustomersView(View):
    def get(self , request):
        greeting = {}
        greeting['heading'] = "Customers"
        greeting['pageview'] = "Ecommerce"
        return render (request,'ecommerce/ecommerce-customers.html',greeting)      


class CartView(View):
    def get(self , request):
        greeting = {}
        greeting['heading'] = "Cart"
        greeting['pageview'] = "Ecommerce"
        return render (request,'ecommerce/ecommerce-cart.html',greeting)      

class CheckOutView(View):
    def get(self , request):
        greeting = {}
        greeting['heading'] = "Checkout"
        greeting['pageview'] = "Ecommerce"
        return render (request,'ecommerce/ecommerce-checkout.html',greeting) 

class ShopsView(View):
    def get(self , request):
        greeting = {}
        greeting['heading'] = "Shops"
        greeting['pageview'] = "Ecommerce"
        return render (request,'ecommerce/ecommerce-shops.html',greeting)                                         

class AddProductView(View):
    def get(self , request):
        greeting = {}
        greeting['heading'] = "Add Product"
        greeting['pageview'] = "Ecommerce"
        return render (request,'ecommerce/ecommerce-addproduct.html',greeting)                                                 