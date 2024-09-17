from django.shortcuts import render
from django.views import View
from django.http import HttpResponseRedirect
from ecommerce.models import inventario, molino3

from django.db.models import query
from django.http.request import QueryDict
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.db.models import Q

#from .forms import ModelFormWithFileField
# Create your views here.


class ProductsView(View):
    def get(self, request):
        greeting = {}
        greeting['heading'] = "ALMACEN"
        greeting['pageview'] = "Inventario de Materiales de Almacén"
        greeting['tabla'] = inventario.objects.all().exclude(pk=0)
        greeting['molino3_areas']=molino3.objects.values('descripcion_de_ubicacion_funcional').distinct()
        #greeting['molino3_equipos']=molino3.objects.filter(descripcion_de_ubicacion_funcional="MC3 ALIMENTACION").distinct()
        #greeting['equipos'] = Molino3.objects.values('descripcion_de_equipo').distinct()
        return render(request, 'ecommerce/ecommerce-products.html', greeting)

class ProductsViewPorArea(ListView):
    template_name =  'ecommerce/ecommerce-products-area.html'
    def get_queryset(self):
       filters = Q(descripcion_de_ubicacion_funcional__icontains=self.query())
       return molino3.objects.filter(filters).exclude(material=0)
    
    def query(self):
        return self.request.GET.get('i')

    def get_context_data(self, **kwargs):
        context = super().get_context_data( **kwargs)
        context['query'] = self.query()
        context['tabla'] = self.get_queryset()
        context['molino3_areas']=context['tabla'].values('descripcion_de_ubicacion_funcional').distinct()
        context['molino3_equipos']=context['tabla'].values('equipo_hac').distinct()
        return context

class ProductsViewPorEquipo(ListView):
    template_name =  'ecommerce/ecommerce-products-area.html'
    def get_queryset(self):
       filters = Q(equipo_hac__icontains=self.query())
       return molino3.objects.filter(filters).exclude(material=0)
    
    def query(self):
        return self.request.GET.get('i')

    def get_context_data(self, **kwargs):
        context = super().get_context_data( **kwargs)
        context['query'] = self.query()
        context['tabla'] = self.get_queryset()
        context['molino3_areas']=context['tabla'].values('descripcion_de_ubicacion_funcional').distinct()
        context['molino3_equipos']=context['tabla'].values('equipo_hac').distinct()
        return context

class ProductSearchListView(ListView):
    template_name =  'ecommerce/ecommerce-products.html'
    def get_queryset(self):
       filters = Q(texto_breve_de_material__icontains=self.query()) | Q(material__icontains=self.query())
       return inventario.objects.filter(filters).exclude(pk=0)
    
    def query(self):
        return self.request.GET.get('i')

    def get_context_data(self, **kwargs):
        context = super().get_context_data( **kwargs)
        context['query'] = self.query()
        context['tabla'] = self.get_queryset()
        context['molino3_areas']=molino3.objects.values('descripcion_de_ubicacion_funcional').distinct()
        return context

def ProductsDetailView2(request, filtro=''):
    greeting = {}
    greeting['heading'] = "ALMACEN"
    greeting['pageview'] = "Inventario de Materiales de Almacén"
    #filtro=form.cleaned_data["filtro"]
    greeting['tabla']= inventario.objects.filter(texto_breve_de_material__icontains=filtro).all()
    greeting['molino3_areas']=molino3.objects.values('descripcion_de_ubicacion_funcional').distinct()
    return render(request, 'ecommerce/ecommerce-products.html', greeting)
    
def ProductsView2(request, i_id=0):
    greeting = {}
    greeting['heading'] = "Product Details"
    greeting['pageview'] = "Ecommerce"
    #filtro=form.cleaned_data["filtro"]
    #greeting['tabla']= inventario.objects.filter(texto_breve_de_material__icontains=filtro).all()
    greeting['tabla']= inventario.objects.get(pk=i_id)
    greeting['molino3_areas']=molino3.objects.values('descripcion_de_ubicacion_funcional').distinct()
    return render(request, 'ecommerce/ecommerce-productdetailJG.html', greeting)


#    greeting['tabla'] = inventario.objects.get(pk=i_id)


class ProductDetailView(View):
    def get(self, request):
        greeting = {}
        greeting['heading'] = "Product Detail"
        greeting['pageview'] = "Ecommerce"
        return render(request, 'ecommerce/ecommerce-productdetail.html', greeting)


class OrdersView(View):
    def get(self, request):
        greeting = {}
        greeting['heading'] = "Orders"
        greeting['pageview'] = "Ecommerce"
        return render(request, 'ecommerce/ecommerce-orders.html', greeting)


class CustomersView(View):
    def get(self, request):
        greeting = {}
        greeting['heading'] = "Customers"
        greeting['pageview'] = "Ecommerce"
        return render(request, 'ecommerce/ecommerce-customers.html', greeting)


class CartView(View):
    def get(self, request):
        greeting = {}
        greeting['heading'] = "Cart"
        greeting['pageview'] = "Ecommerce"
        return render(request, 'ecommerce/ecommerce-cart.html', greeting)


class CheckOutView(View):
    def get(self, request):
        greeting = {}
        greeting['heading'] = "Checkout"
        greeting['pageview'] = "Ecommerce"
        return render(request, 'ecommerce/ecommerce-checkout.html', greeting)


class ShopsView(View):
    def get(self, request):
        greeting = {}
        greeting['heading'] = "Shops"
        greeting['pageview'] = "Ecommerce"
        return render(request, 'ecommerce/ecommerce-shops.html', greeting)


class AddProductView(View):
    def get(self, request):
        greeting = {}
        greeting['heading'] = "Add Product"
        greeting['pageview'] = "Ecommerce"
        return render(request, 'ecommerce/ecommerce-addproduct.html', greeting)


# def upload_file(request):
#    if request.method == 'POST':
#        form = ModelFormWithFileField(request.POST, request.FILES)
#        if form.is_valid():
#            # file is saved
#            form.save()
#            return HttpResponseRedirect('/ecommerce/ProductsView')
#    else:
#        form = ModelFormWithFileField()
#    return render(request, '/ecommerce/ProductsView', {'form': form})
def cuentaRepetidos():
    i = inventario.objects.all()
    ultimo = len(i)
    k=0
    repetidos=[]
    for j in range(ultimo):
        if k==ultimo:
            break
        else:
            if j[k].material==j[k+1].material:
                repetidos.append(j[k].material)
            k=+1
    return repetidos

            
        
