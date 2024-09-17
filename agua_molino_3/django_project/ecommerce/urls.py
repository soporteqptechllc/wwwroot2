from django.urls import path
#from Skote_Django.Admin import ecommerce
from ecommerce import views
urlpatterns = [
    #ecommerce
    path('products',views.ProductsView.as_view(),name='ecommerce-products'),
    path('search',views.ProductSearchListView.as_view(),name='search'),
    path('area',views.ProductsViewPorArea.as_view(), name='area'),
    path('equipo',views.ProductsViewPorEquipo.as_view(), name='equipo'),
    path("filtro/<str:filtro>",views.ProductsDetailView2,name='ecommerce-detalle'),
    path("id/<int:i_id>", views.ProductsView2, name='ecommerce-prodcut-id'),
    path('productdetail',views.ProductDetailView.as_view(),name='ecommerce-productdetail'),
    path('orders',views.OrdersView.as_view(),name='ecommerce-orders'),
    path('customers',views.CustomersView.as_view(),name='ecommerce-customers'),
    path('cart',views.CartView.as_view(),name='ecommerce-cart'),
    path('checkout',views.CheckOutView.as_view(),name='ecommerce-checkout'),
    path('shops',views.ShopsView.as_view(),name='ecommerce-shops'),
    path('upload_file',views.ShopsView.as_view(),name='upload_file'),
    path('addproduct',views.AddProductView.as_view(),name='ecommerce-addproduct'),
]