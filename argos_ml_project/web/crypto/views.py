from django.shortcuts import render
from django.views import View
# Create your views here.
class WalletView(View):
    def get(self , request):
        greeting = {}
        greeting['heading'] = "Wallet"
        greeting['pageview'] = "Crypto"
        return render (request,'crypto/crypto-wallet.html',greeting)

class BuySellView(View):
    def get(self , request):
        greeting = {}
        greeting['heading'] = "Buy/Sell"
        greeting['pageview'] = "Crypto"
        return render (request,'crypto/crypto-buysell.html',greeting)

class ExchangeView(View):
    def get(self , request):
        greeting = {}
        greeting['heading'] = "Exchange"
        greeting['pageview'] = "Crypto"
        return render (request,'crypto/crypto-exchange.html',greeting)

class LendingView(View):
    def get(self , request):
        greeting = {}
        greeting['heading'] = "Lending"
        greeting['pageview'] = "Crypto"
        return render (request,'crypto/crypto-lending.html',greeting)        

class OrdersView(View):
    def get(self , request):
        greeting = {}
        greeting['heading'] = "Orders"
        greeting['pageview'] = "Crypto"
        return render (request,'crypto/crypto-orders.html',greeting)  

class KYCView(View):
    def get(self , request):
        greeting = {}
        greeting['heading'] = "KYC Application"
        greeting['pageview'] = "Crypto"
        return render (request,'crypto/crypto-kycappication.html',greeting)  

class ICOLandingView(View):
    def get(self , request):
        greeting = {}
        greeting['heading'] = "ICO Landing"
        greeting['pageview'] = "Crypto"
        return render (request,'crypto/crypto-icolanding.html',greeting)                         