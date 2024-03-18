from django.urls import path
from web.components import views
app_name = 'components_app'
urlpatterns = [
    #UI-ELEMENTS
    path('alerts',views.AlertsView.as_view(),name='uielements-alerts'),
    path('buttons',views.ButtonsView.as_view(),name='uielements-buttons'),
    path('cards',views.CardsView.as_view(),name='uielements-cards'),
    path('carousel',views.CarouselView.as_view(),name='uielements-carousel'),
    path('dropdowns',views.DropDownsView.as_view(),name='uielements-dropdowns'),
    path('grid',views.GridView.as_view(),name='uielements-grid'),
    path('images',views.ImagesView.as_view(),name='uielements-images'),
    path('lightbox',views.LightBoxView.as_view(),name='uielements-lightbox'),
    path('modals',views.ModalsView.as_view(),name='uielements-modals'),
    path('rangeslidebar',views.RangeSlidebarView.as_view(),name='uielements-rangeslidebar'),
    path('sessiontimeout',views.SessionTimeoutView.as_view(),name='uielements-sessiontimeout'),
    path('progressbars',views.ProgressBarsView.as_view(),name='uielements-progressbars'),
    path('sweetalert',views.SweetAlertView.as_view(),name='uielements-sweetalert'),
    path('tabs&accordians',views.TabsView.as_view(),name='uielements-tabs'),
    path('typography',views.TypoGraphyView.as_view(),name='uielements-typography'),
    path('video',views.VideoView.as_view(),name='uielements-video'),
    path('general',views.GeneralView.as_view(),name='uielements-general'),
    path('colors',views.ColorsView.as_view(),name='uielements-colors'),
    path('rating',views.RatingView.as_view(),name='uielements-rating'),
    path('notifications',views.NotificationsView.as_view(),name='uielements-notifications'),

    #FORMS
    path('formelements',views.FormelementsView.as_view(),name='forms-formelements'),
    path('formlayouts',views.FormLayoutsView.as_view(),name='forms-formlayouts'),
    path('formvalidation',views.FormValidationView.as_view(),name='forms-formvalidation'),
    path('formadvanced',views.FormAdvancedView.as_view(),name='forms-formadvanced'),
    path('formeditors',views.FormEditorsView.as_view(),name='forms-formeditors'),
    path('formfileupload',views.FormFileuploadView.as_view(),name='forms-formfileupload'),
    path('formxeditable',views.FormXeditableView.as_view(),name='forms-formxeditable'),
    path('formrepeater',views.FormRepeaterView.as_view(),name='forms-formrepeater'),
    path('formwizard',views.FormWizardView.as_view(),name='forms-formwizard'),
    path('formmask',views.FormMaskView.as_view(),name='forms-formmask'),

    #Tables
    path('basictables',views.BasicTablesView.as_view(),name='tables-basictables'),
    path('datatables',views.DataTablesView.as_view(),name='tables-datatables'),
    path('responsivetables',views.ResponsiveTablesView.as_view(),name='tables-responsivetables'),
    path('viewtables1/<int:kword>/',views.ListarTabla1View1.as_view(),name='tables-viewtabletables1'),
    path('viewtables2/<int:kword>/',views.ListarTabla1View2.as_view(),name='tables-viewtabletables2'),
    path('edittables/<int:kword>/',views.EditableTablesView.as_view(),name='tables-edittables'),    
    path('updatetables/<int:kword>/<int:knum>/',views.TablesUpdateView.as_view(), name='filas-editar'),

    path('viewtables11/<int:kword>/',views.ListarTabla1View1X.as_view(),name='tables-viewtabletables1X'),
    path('viewtables21/<int:kword>/',views.ListarTabla1View2X.as_view(),name='tables-viewtabletables2X'),
    path('edittables1/<int:kword>/',views.EditableTablesViewX.as_view(),name='tables-edittablesX'),
    path('updatetables1/<int:kword>/<int:knum>/',views.TablesUpdateViewX.as_view(), name='filas-editarX'),
    #Orders
    path('addorders2/<int:kword>/',views.ProductionOrderAddView.as_view(),name='orders-add'),

    path('addorders1/<int:kword>/',views.ProductionOrderAddViewX.as_view(),name='orders-addX'),  
    #Charts
    path('apexcharts',views.ApexChartsView.as_view(),name='charts-apexcharts'),
    path('echarts',views.EChartsView.as_view(),name='charts-echarts'),
    path('chartjs',views.ChartJsView.as_view(),name='charts-chartjs'),
    path('flotcharts',views.FlotChartsView.as_view(),name='charts-flotcharts'), 
    path('toastuicharts',views.ToastUiChartsView.as_view(),name='charts-toastuicharts'), 
    path('jqueryknobcharts',views.JqueryKnobChartsView.as_view(),name='charts-jqueryknobcharts'), 
    path('sparklinecharts',views.SparklineChartsView.as_view(),name='charts-sparklinecharts'),

    #Icons
    path('boxicons',views.BoxIconsView.as_view(),name='icons-boxicons'),
    path('materialdesign',views.MaterialDesignView.as_view(),name='icons-materialdesign'),
    path('dripicons',views.DripIconsView.as_view(),name='icons-dripicons'),
    path('fontawesome',views.FontAwesomeView.as_view(),name='icons-fontawesome'),

    #Maps
    path('googlemaps',views.GoogleMapsView.as_view(),name='maps-googlemaps'),
    path('vectormaps',views.VectorMapsView.as_view(),name='maps-vectormaps'),
    path('leafletmaps',views.LeafletMapsView.as_view(),name='maps-leafletmaps'),
    #Reporte de Horas
    #path("contact", views.contact, name="contact"),

]