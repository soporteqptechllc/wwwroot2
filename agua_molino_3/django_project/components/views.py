# -*- coding: utf-8 -*-
from ast import Num
from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views import View

from components.paquetes.delete_files import del_file
from .models import silos, silosML, Valoressensores
from django.shortcuts import redirect
from django.contrib import messages
from time import gmtime, strftime
from os import remove
from datetime import datetime, timedelta
import pytz

#UI-ELEMENTS
class AlertsView(View):
    def get(self , request):
        greeting = {}
        greeting['heading'] = "Alerts"
        greeting['pageview'] = "UI Elements"
        return render (request,'components/ui-elements/components-alerts.html',greeting)

class ButtonsView(View):
    def get(self , request):
        greeting = {}
        greeting['heading'] = "Buttons"
        greeting['pageview'] = "UI Elements"
        return render (request,'components/ui-elements/components-buttons.html',greeting)

class CardsView(View):
    def get(self , request):
        greeting = {}
        greeting['heading'] = "Cards"
        greeting['pageview'] = "UI Elements"
        return render (request,'components/ui-elements/components-cards.html',greeting)    

class CarouselView(View):
    def get(self , request):
        greeting = {}
        greeting['heading'] = "Carousel"
        greeting['pageview'] = "UI Elements"
        return render (request,'components/ui-elements/components-carousel.html',greeting)  


class DropDownsView(View):
    def get(self , request):
        greeting = {}
        greeting['heading'] = "Dropdowns"
        greeting['pageview'] = "UI Elements"
        return render (request,'components/ui-elements/components-dropdwons.html',greeting)                    

class GridView(View):
    def get(self , request):
        greeting = {}
        greeting['heading'] = "Grid"
        greeting['pageview'] = "UI Elements"
        return render (request,'components/ui-elements/components-grid.html',greeting) 

class ImagesView(View):
    def get(self , request):
        greeting = {}
        greeting['heading'] = "Images"
        greeting['pageview'] = "UI Elements"
        return render (request,'components/ui-elements/components-images.html',greeting)   

class LightBoxView(View):
    def get(self , request):
        greeting = {}
        greeting['heading'] = "Lightbox"
        greeting['pageview'] = "UI Elements"
        return render (request,'components/ui-elements/components-lightbox.html',greeting)    

class ModalsView(View):
    def get(self , request):
        greeting = {}
        greeting['heading'] = "Modals"
        greeting['pageview'] = "UI Elements"
        return render (request,'components/ui-elements/components-modals.html',greeting) 

class RangeSlidebarView(View):
    def get(self , request):
        greeting = {}
        greeting['heading'] = "Range Slider"
        greeting['pageview'] = "UI Elements"
        return render (request,'components/ui-elements/components-rangeslidebar.html',greeting) 

class SessionTimeoutView(View):
    def get(self , request):
        greeting = {}
        greeting['heading'] = "Session Timeout"
        greeting['pageview'] = "UI Elements"
        return render (request,'components/ui-elements/components-sessiontimeout.html',greeting)           

class ProgressBarsView(View):
    def get(self , request):
        greeting = {}
        greeting['heading'] = "Progress Bars"
        greeting['pageview'] = "UI Elements"
        return render (request,'components/ui-elements/components-progressbars.html',greeting)    

class SweetAlertView(View):
    def get(self , request):
        greeting = {}
        greeting['heading'] = "Sweet-Alert"
        greeting['pageview'] = "UI Elements"
        return render (request,'components/ui-elements/components-sweetalert.html',greeting)     

class TabsView(View):
    def get(self , request):
        greeting = {}
        greeting['heading'] = "Tabs & Accordions"
        greeting['pageview'] = "UI Elements"
        return render (request,'components/ui-elements/components-tabs.html',greeting)   

class TypoGraphyView(View):
    def get(self , request):
        greeting = {}
        greeting['heading'] = "Typography"
        greeting['pageview'] = "UI Elements"
        return render (request,'components/ui-elements/components-typography.html',greeting)   

class VideoView(View):
    def get(self , request):
        greeting = {}
        greeting['heading'] = "Video"
        greeting['pageview'] = "UI Elements"
        return render (request,'components/ui-elements/components-video.html',greeting)   


class GeneralView(View):
    def get(self , request):
        greeting = {}
        greeting['heading'] = "General"
        greeting['pageview'] = "UI Elements"
        return render (request,'components/ui-elements/components-general.html',greeting)                                                                           

class ColorsView(View):
    def get(self , request):
        greeting = {}
        greeting['heading'] = "Colors"
        greeting['pageview'] = "UI Elements"
        return render (request,'components/ui-elements/components-colors.html',greeting)  

class RatingView(View):
    def get(self , request):
        greeting = {}
        greeting['heading'] = "Rating"
        greeting['pageview'] = "UI Elements"
        return render (request,'components/ui-elements/components-rating.html',greeting)  


class NotificationsView(View):
    def get(self , request):
        greeting = {}
        greeting['heading'] = "Notifications"
        greeting['pageview'] = "UI Elements"
        return render (request,'components/ui-elements/components-notifications.html',greeting)

##FORMS
class FormelementsView(View):
    def get(self , request):
        greeting = {}
        greeting['heading'] = "Form Elements"
        greeting['pageview'] = "Forms"
        return render (request,'components/forms/components-formelements.html',greeting)


class FormLayoutsView(View):
    def get(self , request):
        greeting = {}
        greeting['heading'] = "Form Layouts"
        greeting['pageview'] = "Forms"
        return render (request,'components/forms/components-formlayouts.html',greeting)

        
class FormValidationView(View):
    def get(self , request):
        greeting = {}
        greeting['heading'] = "Form Validation"
        greeting['pageview'] = "Forms"
        return render (request,'components/forms/components-formvalidation.html',greeting)        

        
class FormAdvancedView(View):
    def get(self , request):
        greeting = {}
        greeting['heading'] = "Form Advanced"
        greeting['pageview'] = "Forms"
        return render (request,'components/forms/components-formadvanced.html',greeting)           


class FormEditorsView(View):
    def get(self , request):
        greeting = {}
        greeting['heading'] = "Form Editors"
        greeting['pageview'] = "Forms"
        return render (request,'components/forms/components-formeditors.html',greeting)         

 # CAPTURA de ARCHIVO TXT========================================================================
class FormFileuploadView(View):
    def get(self , request):
        #messages.error(request, 'hola')
        greeting = {}
        greeting['heading'] = "Formulario Para Subir Archivo de Inventario (Inventario.txt)"
        greeting['pageview'] = "Forms"
        return render (request,'components/forms/components-formfileupload.html',greeting)
# CAPTURA de ARCHIVO XLSX========================================================================
class FormFileuploadView1(View):
    def get(self , request):
        messages.info(
            request, 'Por favor espere un tiempo, después de presionar el Botón, ya que el proceso es complejo.')
        greeting = {}
        greeting['heading'] = "Formulario Para Subir Archivo de Repuestos de Molino3 (REPUESTO POR AREAS.xlsx)"
        greeting['pageview'] = "Forms"
        return render (request,'components/forms/components-formfileupload1.html',greeting)         

class FormFileuploadView2(View):
    def get(self , request):
        greeting = {}
        greeting['heading'] = "Formulario Para Subir Archivo de Imagenes (.jpeg, .jpg, .png)"
        greeting['pageview'] = "Forms"
        return render (request,'components/forms/components-formfileupload2.html',greeting)

class FormFileuploadView3(View):
    def get(self, request):
        greeting = {}
        greeting[
            'heading'] = "Formulario Para Subir Archivo de Repuestos Por Equipos (Equipos.xlsx)"
        greeting['pageview'] = "Forms"
        return render(request, 'components/forms/components-formfileupload3.html', greeting)

class FormTanksView1(View):
    def get(self, request):
        messages.info(
            request, 'Por favor espere que carge la información, utilice el boton Refrescar para actualizar.')
        greeting = {}
        greeting['heading'] = "Información de los Silos"
        greeting['pageview'] = "Planta Argos Tocumen"
        greeting['tanques'] = silos.objects.all().exclude(pk=0)
        return render(request, 'components/forms/components-formtanks1.html', greeting)

class TanksViewSilosListas(View):

    def get(self, request, silo=None, dia=None, fecha=None):
        # Declaracion de variables 
        #print('El silo es:', silo)
        #print('El dia es:', dia)
        #print('La fecha es:', fecha)
        # Selecciono el Silo por un numero enviado por URL
        if silo == 1:
            silotxt = 'Silo 1'
            TanquesArgos = silosML.objects.filter(silo = silotxt)
            mensaje1 = "Información de los Silos, Mezclas Listas"
            mensaje2 = "Planta Argos Mezclas Listas"
        elif silo == 2:
            silotxt = 'Silo 2'
            TanquesArgos = silosML.objects.filter(silo = silotxt)
            mensaje1 = "Información de los Silos, Mezclas Listas"
            mensaje2 = "Planta Argos Mezclas Listas"
        elif silo == 212:
            silotxt = 'Silo 21-2'
            TanquesArgos = silos.objects.filter(silo = silotxt)
            mensaje1 = "Información de los Silos, Planta de Concretos Tocumen"
            mensaje2 = silotxt
        elif silo == 213:
            silotxt = 'Silo 21-3'
            TanquesArgos = silos.objects.filter(silo = silotxt)
            mensaje1 = "Información de los Silos, Planta de Concretos Tocumen"
            mensaje2 = silotxt
        elif silo == 253:
            silotxt = 'Silo 25-3'
            TanquesArgos = silos.objects.filter(silo = silotxt)
            mensaje1 = "Información de los Silos, Planta de Concretos Tocumen"
            mensaje2 = silotxt
        else:
            silotxt = 'Silo 1'
        #print('El silo es:', silotxt) 
        now = datetime.now()  # current date and time
        hoy = now.strftime("%Y-%m-%d")
        #print("hoy:", hoy)
        #  Selecciono la fecha segun el valor de la variable dia enviado por URL
        if dia == 0:
            dato = datetime.strptime(hoy,"%Y-%m-%d")
        else:
            dato = datetime.strptime(fecha,"%Y-%m-%d")
        #print("date:", dato)
        dato1 = dato - timedelta(days=1)  # day subtraction operation
        #print("date1:", dato1)
        dato2 = dato + timedelta(days=1)  # day addition operation
        #print("date2:", dato2)
        dato3 = dato1.strftime("%Y-%m-%d")
        #print("date3:", dato3)
        dato4 = dato2.strftime("%Y-%m-%d")
        #print("date4:", dato4)
        # Selecciono la fecha segun el valor de la variable dia enviado por URL
        if dia == 0: # Es la fecha actual
            diatxt = hoy
        elif dia == 1: # Es la misma fecha 
            diatxt = fecha
        elif dia == 2: # Es la fecha menos un dia
            diatxt = dato3
        elif dia == 3: # Es la fecha mas un dia
            diatxt = dato4
        else:
            diatxt = hoy 
        #print('El dia es:', diatxt)
        
        DataGraf = Valoressensores.objects.filter(nombre_silo = silotxt , fecha__contains = diatxt).order_by('-fecha','-hora')
        listx = ''
        listy = ''
        for i in DataGraf: # Se crea las listas de los eje X y Y de la Grafiva
            if listx == '':
                listx = str(i.hora)
                listy = str(i.nivel)
            else:              
                listx = str(i.hora) + ',' + listx
                listy = str(i.nivel) + ',' + listy
                
        messages.info(
            request, 'Por favor espere que carge la información')
        greeting = {}
        greeting['heading'] = mensaje1
        greeting['pageview'] = mensaje2
        greeting['tanques'] = TanquesArgos
        greeting['listaX'] = listx
        greeting['listaY'] = listy
        greeting['tituloX'] = "Nivel del Silo (m)"
        greeting['fechaX'] = diatxt
        greeting['silo'] = silo

        return render(request, 'components/forms/components-mezclaslistasJG.html', greeting)      
# Nivel de Tanque y Grafica Lineal JG ========================================================================
class TanksViewMezclasListas(View): 
    def get(self,request):
        # Declaracion de variables
        tz = pytz.timezone('America/Bogota') # current time zone local
        now = datetime.now()  # current date and time
        hoy = now.strftime("%Y-%m-%d")
        silotxt = 'Silo 1'
        TanquesArgos = silosML.objects.filter(silo = silotxt)
        DataGraf = Valoressensores.objects.filter(nombre_silo = silotxt, fecha__contains = hoy).order_by('-fecha','-hora')
        listx = ''
        listy = ''
        for i in DataGraf:
            if listx == '':
                listx=str(i.hora.astimezone(tz))
                listy=str(i.nivel)
            else:
                listx = str(i.hora.astimezone(tz)) + ',' + listx
                listy = str(i.nivel) + ',' + listy
        messages.info(
            request, 'Por favor espere que carge la información')
        greeting = {}
        greeting['heading'] = "Información de los Silos, Mezclas Listas"
        greeting['pageview'] = "Planta Argos Mezclas Listas"
        greeting['tanques'] = TanquesArgos
        greeting['listaX'] = listx
        greeting['listaY'] = listy
        greeting['tituloX'] = "Nivel del Silo (m)"
        greeting['fechaX'] = hoy
        greeting['refrescar'] = 'mezclaslistas'
        return render(request, 'components/forms/components-mezclaslistas.html', greeting)

class TanksViewMezclasListas2(View): 
    def get(self,request):
        # Declaracion de variables
        tz = pytz.timezone('America/Bogota') # current time zone local
        now = datetime.now()  # current date and time
        hoy = now.strftime("%Y-%m-%d")
        silotxt = 'Silo 2'
        TanquesArgos = silosML.objects.filter(silo = silotxt)
        DataGraf = Valoressensores.objects.filter(nombre_silo = silotxt, fecha__contains = hoy).order_by('-fecha','-hora')
        listx = ''
        listy = ''

        for i in DataGraf:
            if listx == '':
                listx=str(i.hora.astimezone(tz))
                listy=str(i.nivel)
            else:
                listx = str(i.hora.astimezone(tz)) + ',' + listx
                listy = str(i.nivel) + ',' + listy
        messages.info(
            request, 'Por favor espere que carge la información')
        greeting = {}
        greeting['heading'] = "Información de los Silos, Mezclas Listas"
        greeting['pageview'] = "Planta Argos Mezclas Listas"
        greeting['tanques'] = TanquesArgos
        greeting['listaX'] = listx
        greeting['listaY'] = listy
        greeting['tituloX'] = "Nivel del Silo (m)"
        greeting['fechaX'] = hoy
        greeting['refrescar'] = 'mezclaslistas2'
        return render(request, 'components/forms/components-mezclaslistas.html', greeting)

class TanksViewMezclasListas211(View): 
    def get(self,request):
        # Declaracion de variables
        tz = pytz.timezone('America/Bogota') # current time zone local
        now = datetime.now()  # current date and time
        hoy = now.strftime("%Y-%m-%d")
        silotxt = 'Silo 21-2'
        TanquesArgos = silos.objects.filter(silo = silotxt)
        DataGraf = Valoressensores.objects.filter(nombre_silo = silotxt, fecha__contains = hoy).order_by('-fecha','-hora')
        listx = ''
        listy = ''
        for i in DataGraf:
            if listx == '':
                listx=str(i.hora.astimezone(tz))
                listy=str(i.nivel)
            else:
                listx = str(i.hora.astimezone(tz)) + ',' + listx
                listy = str(i.nivel) + ',' + listy
        messages.info(
            request, 'Por favor espere que carge la información')
        greeting = {}
        greeting['heading'] = "Información de los Silos, Planta de Concretos Tocumen"
        greeting['pageview'] = "Silo 21-2"
        greeting['tanques'] = TanquesArgos
        greeting['listaX'] = listx
        greeting['listaY'] = listy
        greeting['tituloX'] = "Nivel del Silo (m)"
        greeting['fechaX'] = hoy
        greeting['refrescar'] = 'mezclaslistas211'
        return render(request, 'components/forms/components-mezclaslistas.html', greeting)

class TanksViewMezclasListas212(View): 
    def get(self,request):
        # Declaracion de variables
        tz = pytz.timezone('America/Bogota') # current time zone local
        now = datetime.now()  # current date and time
        hoy = now.strftime("%Y-%m-%d")
        silotxt = 'Silo 21-3'
        TanquesArgos = silos.objects.filter(silo = silotxt)
        DataGraf = Valoressensores.objects.filter(nombre_silo = silotxt, fecha__contains = hoy).order_by('-fecha','-hora')
        listx = ''
        listy = ''
        for i in DataGraf:
            if listx == '':
                listx=str(i.hora.astimezone(tz))
                listy=str(i.nivel)
            else:
                listx = str(i.hora.astimezone(tz)) + ',' + listx
                listy = str(i.nivel) + ',' + listy
        messages.info(
            request, 'Por favor espere que carge la información')
        greeting = {}
        greeting['heading'] = "Información de los Silos, Planta de Concretos Tocumen"
        greeting['pageview'] = "Silo 21-3"
        greeting['tanques'] = TanquesArgos
        greeting['listaX'] = listx
        greeting['listaY'] = listy
        greeting['tituloX'] = "Nivel del Silo (m)"
        greeting['fechaX'] = hoy
        greeting['refrescar'] = 'mezclaslistas212'
        return render(request, 'components/forms/components-mezclaslistas.html', greeting)

class TanksViewMezclasListas213(View): 
    def get(self,request):
        # Declaracion de variables
        tz = pytz.timezone('America/Bogota') # current time zone local
        now = datetime.now()  # current date and time
        hoy = now.strftime("%Y-%m-%d")
        silotxt = 'Silo 25-3'
        TanquesArgos = silos.objects.filter(silo = silotxt)
        DataGraf = Valoressensores.objects.filter(nombre_silo = silotxt, fecha__contains = hoy).order_by('-fecha','-hora')
        listx = ''
        listy = ''
        for i in DataGraf:
            if listx == '':
                listx=str(i.hora.astimezone(tz))
                listy=str(i.nivel)
            else:
                listx = str(i.hora.astimezone(tz)) + ',' + listx
                listy = str(i.nivel) + ',' + listy
        messages.info(
            request, 'Por favor espere que carge la información')
        greeting = {}
        greeting['heading'] = "Información de los Silos, Planta de Concretos Tocumen"
        greeting['pageview'] = "Silo 25-3"
        greeting['tanques'] = TanquesArgos
        greeting['listaX'] = listx
        greeting['listaY'] = listy
        greeting['tituloX'] = "Nivel del Silo (m)"
        greeting['fechaX'] = hoy
        greeting['refrescar'] = 'mezclaslistas213'
        return render(request, 'components/forms/components-mezclaslistas.html', greeting)

# CAPTURA de ARCHIVO TXT========================================================================

def file_upload_view(request):   
    if request.method == 'POST':
        return HttpResponse('')
    return JsonResponse({'post':'false'})
    


def file_upload_inventario(request):   
    # Specify path
    return redirect('forms-formfileupload')

# CAPTURA de ARCHIVO XLSX========================================================================

def file_upload_view1(request):
    if request.method == 'POST':
        my_file = request.FILES.get('file')
        return HttpResponse('')
    return JsonResponse({'post': 'false'})

def file_upload_repuestos1(request):
    # Specify path
    path1 = r'media\files1\REPUESTO_POR_AREAS.xlsx'
    # Check whether the specified
    # path exists or not
    return redirect('forms-formfileupload1')

# CAPTURA de ARCHIVO JPEG========================================================================

def file_upload_view2(request):
    if request.method == 'POST':
      return JsonResponse({'post': 'false'})


class FormXeditableView(View):
    def get(self , request):
        greeting = {}
        greeting['heading'] = "Form Xeditable"
        greeting['pageview'] = "Forms"
        return render (request,'components/forms/components-formxeditable.html',greeting) 
              
class FormRepeaterView(View):
    def get(self , request):
        greeting = {}
        greeting['heading'] = "Form Repeater"
        greeting['pageview'] = "Forms"
        return render (request,'components/forms/components-formrepeater.html',greeting) 
           

class FormWizardView(View):
    def get(self , request):
        greeting = {}
        greeting['heading'] = "Form Wizard"
        greeting['pageview'] = "Forms"
        return render (request,'components/forms/components-formrwizard.html',greeting)                  
        
class FormMaskView(View):
    def get(self , request):
        greeting = {}
        greeting['heading'] = "Form Mask"
        greeting['pageview'] = "Forms"
        return render (request,'components/forms/components-formrmask.html',greeting)         

        
##Tables
class BasicTablesView(View):
    def get(self , request):
        greeting = {}
        greeting['heading'] = "Basic Tables"
        greeting['pageview'] = "Tables"
        return render (request,'components/tables/components-basictables.html',greeting)  

class DataTablesView(View):
    def get(self , request):
        greeting = {}
        greeting['heading'] = "Data Tables"
        greeting['pageview'] = "Tables"
        return render (request,'components/tables/components-datatables.html',greeting) 


class ResponsiveTablesView(View):
    def get(self , request):
        greeting = {}
        greeting['heading'] = "Responsive Table"
        greeting['pageview'] = "Tables"
        return render (request,'components/tables/components-responsivetables.html',greeting) 

class EditableTablesView(View):
    def get(self , request):
        greeting = {}
        greeting['heading'] = "Editable Table"
        greeting['pageview'] = "Tables"
        return render (request,'components/tables/components-editabletables.html',greeting) 

#Charts     
class ApexChartsView(View):
    def get(self , request):
        greeting = {}
        greeting['heading'] = "Apex Charts"
        greeting['pageview'] = "Charts"
        return render (request,'components/charts/components-apexcharts.html',greeting)  

class EChartsView(View):
    def get(self , request):
        greeting = {}
        greeting['heading'] = "E Charts"
        greeting['pageview'] = "Charts"
        return render (request,'components/charts/components-echarts.html',greeting)  

class ChartJsView(View):
    def get(self , request):
        greeting = {}
        greeting['heading'] = "Chartjs Charts"
        greeting['pageview'] = "Charts"
        return render (request,'components/charts/components-chartjs.html',greeting)  

class FlotChartsView(View):
    def get(self , request):
        greeting = {}
        greeting['heading'] = "Flot Charts"
        greeting['pageview'] = "Charts"
        return render (request,'components/charts/components-flotcharts.html',greeting)    


class ToastUiChartsView(View):
    def get(self , request):
        greeting = {}
        greeting['heading'] = "Toast UI Charts"
        greeting['pageview'] = "Charts"
        return render (request,'components/charts/components-toastuicharts.html',greeting)                  
                         

class JqueryKnobChartsView(View):
    def get(self , request):
        greeting = {}
        greeting['heading'] = "Jquery Knob Charts"
        greeting['pageview'] = "Charts"
        return render (request,'components/charts/components-jqueryknobcharts.html',greeting)   

class SparklineChartsView(View):
    def get(self , request):
        greeting = {}
        greeting['heading'] = "Sparkline Charts"
        greeting['pageview'] = "Charts"
        return render (request,'components/charts/components-sparklinecharts.html',greeting)                                   

#Icons        
class BoxIconsView(View):
    def get(self , request):
        greeting = {}
        greeting['heading'] = "Boxicons"
        greeting['pageview'] = "Icons"
        return render (request,'components/icons/components-boxicons.html',greeting)         
        

class MaterialDesignView(View):
    def get(self , request):
        greeting = {}
        greeting['heading'] = "Material Design"
        greeting['pageview'] = "Icons"
        return render (request,'components/icons/components-materialdesign.html',greeting)    


class DripIconsView(View):
    def get(self , request):
        greeting = {}
        greeting['heading'] = "Dripicons"
        greeting['pageview'] = "Icons"
        return render (request,'components/icons/components-dripicons.html',greeting)  

class FontAwesomeView(View):
    def get(self , request):
        greeting = {}
        greeting['heading'] = "Font Awesome"
        greeting['pageview'] = "Icons"
        return render (request,'components/icons/components-fontawesome.html',greeting)                     

#Maps
class GoogleMapsView(View):
    def get(self , request):
        greeting = {}
        greeting['heading'] = "Google Maps"
        greeting['pageview'] = "Maps"
        return render (request,'components/maps/components-googlemaps.html',greeting) 

class VectorMapsView(View):
    def get(self , request):
        greeting = {}
        greeting['heading'] = "Vector Maps"
        greeting['pageview'] = "Maps"
        return render (request,'components/maps/components-vectormaps.html',greeting)      

class LeafletMapsView(View):
    def get(self , request):
        greeting = {}
        greeting['heading'] = "Leaflet Maps"
        greeting['pageview'] = "Maps"
        return render (request,'components/maps/components-leafletmaps.html',greeting)            
        