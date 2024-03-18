from django.shortcuts import render
from django.views import View
from django.urls import reverse_lazy
# Import from  Django
from django.views.generic import ( 
    ListView, 
    DetailView,
    CreateView,
    TemplateView,
    UpdateView,
    DeleteView,
    FormView
    )
from django.http import HttpResponse
from .models import Empresa,Responsables,CentroDeCostos,Ingenieros,encabezado,reportehoras,producciondiaria
from api.models import (
    operaciones, 
    em_sp, 
    ProductionOrders1_SAP, 
    ProductionOrders2_SAP, 
    MaestroDeMateriales,
    RecetasSAP
)
from .forms import ContactForm
# Import from datetime of Python 
from datetime import datetime
# Forms from forms.py
from .forms import TablaProdDiariaForm, ProductionOrderForm

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
    def post(self , request):
        greeting = {}
        form = ContactForm()
        formVacio = ContactForm()
        inge = Ingenieros()
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            # Aquí podrías enviar el correo electrónico o guardar los datos en la base de datos
            inge.nombre = name
            inge.email = email
            inge.telefono = message
            inge.save()
        greeting['form'] = form
        greeting['heading'] = "Form Layouts"
        greeting['pageview'] = "Forms"
        return render (request,'components/forms/components-formlayouts.html',greeting)

    def get(self , request):
        form = ContactForm()
        formVacio = ContactForm()
        inge = Ingenieros()
        
        greeting = {}
        greeting['form'] = formVacio 
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

        
class FormFileuploadView(View):
    def get(self , request):
        greeting = {}
        greeting['heading'] = "Form File Upload"
        greeting['pageview'] = "Forms"
        return render (request,'components/forms/components-formfileupload.html',greeting) 

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
###################################################################################################
###################################################################################################
###################################################################################################
###################################################################################################
# ****************************************************    
# Listar los Batchs por dia y lote (Actuales), para ser
# modificados, guardados y cerrados
# **************************************************** 
class EditableTablesViewX(View):
    # Metodo que busca y crea las listas para ser mostrada en pantalla
    def get(self , request, kword=None):
        #print('*********GET*********')
        # ********************************************    
        # Inicio de cabecera 
        # ******************************************** 
        now = datetime.now()  # current date and time
        fecha1 = now.strftime("%Y-%m-%d")
        #print('fecha1: ',fecha1)
        if kword ==1:
            # ********************************************    
            # Datos para la tabla
            # ********************************************
            batchs1 = operaciones.objects.filter(idfabricacion = None,idlote__gt=0).first()
            if batchs1:
                Sem = batchs1.receta_nombre
                idsem = batchs1.receta_id
                idlote = batchs1.idlote
                data1 = batchs1.hora[0:20].replace(" ", "").replace(":","").replace("-","")
                fechatxt2 = datetime.strptime(data1,"%Y%m%d%H%M%S%f")
                fecha2 = fechatxt2.strftime("%Y-%m-%d")
                fecha3 = fechatxt2.strftime("%Y%m%d")
                # print('hora:',batchs1.hora)
                # print('hora2: ',data1)
                # print('fechatxt2: ',fechatxt2)
                # print('fecha2: ',fecha2)
                # print('fecha3: ',fecha3)
                if Sem == None or Sem =="":
                    Sem = "NO EXISTE EN M.MATERIALES"
                if idlote==None:
                    idlote = 0
            else:
                Sem = "NO EXISTE EN M.MATERIALES"
                idlote = 0
                idsem = 0
                fechatxt2 = None
            batchs2 = operaciones.objects.filter(idfabricacion = None,idlote__gt=0,hora__startswith = fecha3).order_by("id")
            if batchs2:
                listaT = list()
                idl = 0
                for i in batchs2:
                    if i.idlote:                    
                        if idl == 0:
                            listaT.append(i.idlote)
                            idl = i.idlote
                        elif idl != i.idlote:
                            listaT.append(i.idlote)
                            idl = i.idlote                       
                #print("listaturno: ",listaT)                
            # print("Semi : ",Sem)
            # print("idlote : ",idlote)
            # print("idsem : ",idsem)
            lista1 = em_sp.objects.filter(em__gt = 0).order_by("id")
            lista2 = operaciones.objects.filter(idfabricacion = None,idlote=idlote).order_by("id")
            nolista1 = len(lista1)
            nolista2 = len(lista2)
            # print(nolista1)
            #print(nolista2)
            #print(lista1)
            #print(lista2)
            # ********************************************    
            # Fin de cabecera 
            # ********************************************
            # ********************************************    
            # Inicio de cuerpo 
            # ********************************************
            import VisualizacionReporteCremasFuncionX
            resultado = VisualizacionReporteCremasFuncionX.ListarDataTabla(idlote, idsem, idtipo = 0)                
            # ********************************************    
            # Fin de cuerpo 
            # ******************************************** 
        elif kword != None and kword > 1:
            batchs1 = operaciones.objects.filter(idfabricacion = None,idlote=kword).first()
            if batchs1:
                Sem = batchs1.receta_nombre
                idsem = batchs1.receta_id
                idlote = batchs1.idlote
                data1 = batchs1.hora[0:20].replace(" ", "").replace(":","").replace("-","")
                fechatxt2 = datetime.strptime(data1,"%Y%m%d%H%M%S%f")
                fecha2 = fechatxt2.strftime("%Y-%m-%d")
                fecha3 = fechatxt2.strftime("%Y%m%d")
                #print('hora:',batchs1.hora)
                #print('hora2: ',data1)
                #print('fechatxt2: ',fechatxt2)
                #print('fecha2: ',fecha2)
                #print('fecha3: ',fecha3)
                if Sem == None or Sem =="":
                    Sem = "NO EXISTE EN M.MATERIALES"
                if idlote==None:
                    idlote = 0
            else:
                Sem = "NO EXISTE EN M.MATERIALES"
                idlote = 0
                idsem = 0
                fechatxt2 = None
            batchs2 = operaciones.objects.filter(idfabricacion = None,idlote__gt=0,hora__startswith = fecha3).order_by("id")
            if batchs2:
                listaT = list()
                idl = 0
                for i in batchs2:
                    if i.idlote:                    
                        if idl == 0:
                            listaT.append(i.idlote)
                            idl = i.idlote
                        elif idl != i.idlote:
                            listaT.append(i.idlote)
                            idl = i.idlote                       
                #print("listaturno: ",listaT)            
            # print("Semi : ",Sem)
            # print("idlote : ",idlote)
            # print("idsem : ",idsem)
            lista1 = em_sp.objects.filter(em__gt = 0).order_by("id")
            lista2 = operaciones.objects.filter(idfabricacion = None,idlote=idlote).order_by("id")
            nolista1 = len(lista1)
            nolista2 = len(lista2)
            #print(nolista1)
            #print(nolista2)
            #print(lista1)
            #print(lista2)
            # ********************************************  
            # Fin de cabecera 
            # ********************************************
            # ********************************************
            # Inicio de cuerpo 
            # ********************************************
            import VisualizacionReporteCremasFuncionX
            resultado = VisualizacionReporteCremasFuncionX.ListarDataTabla(idlote, idsem, idtipo = 0)                             
            # ********************************************    
            # Fin de cuerpo 
            # ********************************************            
        else:
            Sem = "NO EXISTE EN M.MATERIALES"
            idlote = 0
            idsem = 0
            total = 0
            fechatxt2 = None             
            #print("Semi : ",Sem)
            #print("idlote : ",idlote)
            #print("idsem : ",idsem)

        greeting = {}

        greeting['heading'] = "Producción Actual Diaría En Cremas"+" - Lote: "+ str(idlote)
        greeting['pageview'] = "Fecha: "+ fecha2 +" - "+"Producto: "+ Sem
        greeting['fechatxt'] = fecha2
        greeting['idlotetxt'] = idlote
        greeting['nolista2txt'] = nolista2
        greeting['tabla'] = resultado
        greeting['noturnos'] = listaT
        greeting['nourl'] = 0

        return render (request,'components/tables/components-edittables1.html',greeting)

# ****************************************************    
# Listar los datos de una fila de los Batchs de un Turno
# para ser modificados y guardados
# ****************************************************     
class TablesUpdateViewX(View):
    # Metodo que busca y crea las listas para ser mostrada en pantalla
    def get(self , request, kword=None, knum=None):
        #print('*********GET*********')
        #print("kword: ",kword)
        #print("knum: ",knum)
        # ********************************************    
        # Inicio de cabecera 
        # ******************************************** 
        now = datetime.now()  # current date and time
        fecha1 = now.strftime("%Y-%m-%d")
        #print('fecha1: ',fecha1)
        if kword != None and kword > 1:                                               
            batchs1 = operaciones.objects.filter(idfabricacion = None,idlote=kword).first()
            if batchs1:
                Sem = batchs1.receta_nombre
                idsem = batchs1.receta_id
                idlote = batchs1.idlote
                data1 = batchs1.hora[0:20].replace(" ", "").replace(":","").replace("-","")
                fechatxt2 = datetime.strptime(data1,"%Y%m%d%H%M%S%f")
                fecha2 = fechatxt2.strftime("%Y-%m-%d")
                fecha3 = fechatxt2.strftime("%Y%m%d")
                if Sem == None or Sem =="":
                    Sem = "NO EXISTE EN M.MATERIALES"
                if idlote==None:
                    idlote = 0
            else:
                Sem = "NO EXISTE EN M.MATERIALES"
                idlote = 0
                idsem = 0
                fechatxt2 = None
                    
            lista1 = em_sp.objects.filter(em__gt = 0).order_by("id")
            lista2 = operaciones.objects.filter(idfabricacion = None,idlote=idlote).order_by("id")
            nolista1 = len(lista1)
            nolista2 = len(lista2)
            #print("nolista1: ",nolista1)
            if knum !=None and knum <= nolista1:
                if knum <= 15:
                    nofila = knum
                else:
                    nofila = 0
            #print("nofila: ", nofila)
            # ********************************************    
            # Fin de cabecera 
            # ********************************************
            # ********************************************    
            # Inicio de cuerpo 
            # ********************************************
            import VisualizacionReporteCremasFuncionX
            resultado = VisualizacionReporteCremasFuncionX.ListarDataTabla(idlote, idsem, idtipo = 0)                 
            # ********************************************    
            # Fin de cuerpo 
            # ********************************************                 
        else:
            Sem = "NO EXISTE EN M.MATERIALES"
            idlote = 0
            #print("Semi : ",Sem)
            #print("idlote : ",idlote)

        greeting = {}

        greeting['heading'] = "Producción Actual Diaría En Cremas"+" - Lote: "+ str(idlote)
        greeting['pageview'] = "Fecha: "+ fecha2 +" - "+"Producto: "+ Sem
        greeting['fechatxt'] = fecha1
        greeting['idlotetxt'] = idlote
        greeting['nolista2txt'] = nolista2
        greeting['nofilatxt'] = nofila
        greeting['tabla'] = resultado
        greeting['nourl'] = 0

        return render (request,'components/tables/components-editablefila1.html',greeting)
    
    # Metodo que se ejecuta antes de validar y guardar los datos
    def post(self, request, kword=None, knum=None):
        #self.object = self.get_object()
        #print('*********POST*********')
        #print(request.POST) # Se crea como un diccionario
        #print(request.POST['c2']) # Se consulta 
        #print(request.POST['c5']) # Se consulta
        #print("kword: ",kword)
        #print("knum: ",knum)
        if kword:
            idlote = kword
            idf = knum
            lista1 = operaciones.objects.filter(idfabricacion = None,idlote=idlote).order_by("id")
        else:
            Sem = "NO EXISTE EN M.MATERIALES"
            idlote = 0   
            lista1 = 0
            idf = 0
        nolista1 = len(lista1)
        if nolista1 > 20:
            nolista1 = 20
        #print("nolista1: ",nolista1)
        ems = ['em1','em2','em3','em4','em5','em6','em7','em8','em9','em10','em11','em15','em14','reproceso','em16','humedad','ph']
        ops = ['c5','c6','c7','c8','c9','c10','c11','c12','c13','c14',
               'c15','c16','c17','c18','c19','c20','c21','c22','c23','c24']
        idop = list()
        if lista1:
            for i in lista1:
                idop.append(i.id)
        #print("idop: ",idop)
        # Reviso cual fila fue Editada para indicar a que 'em' se le debe cargar
        
        for i in range(0,nolista1):
            if idop[i]:
                if request.POST['c2'] == 'MPDC00008':
                    operaciones.objects.filter(id=idop[i]).update(em1=request.POST[ops[i]])
                elif idf == 1 and request.POST['c2'] == 'MPDC00004':
                    operaciones.objects.filter(id=idop[i]).update(em2=request.POST[ops[i]])
                elif idf == 2 and request.POST['c2'] == 'MPDC00004':
                    operaciones.objects.filter(id=idop[i]).update(em3=request.POST[ops[i]]) 
                elif idf == 3 and request.POST['c2'] == 'MPDC00004':
                    operaciones.objects.filter(id=idop[i]).update(em4=request.POST[ops[i]])                                       
                elif request.POST['c2'] == 'MPDC00002':
                    operaciones.objects.filter(id=idop[i]).update(em5=request.POST[ops[i]])
                elif request.POST['c2'] == 'AGUA':
                    operaciones.objects.filter(id=idop[i]).update(em6=request.POST[ops[i]])
                elif request.POST['c2'] == 'SE-NEUT001':
                    operaciones.objects.filter(id=idop[i]).update(em7=request.POST[ops[i]])                                    
                elif request.POST['c2'] == 'MPCL00002':
                    operaciones.objects.filter(id=idop[i]).update(em8=request.POST[ops[i]])
                elif idf == 9 and request.POST['c2'] == 'MPC000022':
                    operaciones.objects.filter(id=idop[i]).update(em9=request.POST[ops[i]])
                elif request.POST['c2'] == 'MPD000044':
                    operaciones.objects.filter(id=idop[i]).update(em10=request.POST[ops[i]])
                elif idf == 11 and request.POST['c2'] == 'MPC000022':
                    operaciones.objects.filter(id=idop[i]).update(em11=request.POST[ops[i]])
                elif request.POST['c2'] == 'MPC000025':
                    operaciones.objects.filter(id=idop[i]).update(em15=request.POST[ops[i]])
                elif request.POST['c2'] == 'MPC000030':
                    operaciones.objects.filter(id=idop[i]).update(em14=request.POST[ops[i]])
                elif request.POST['c2'] == 'SE-REPROCESO':
                    operaciones.objects.filter(id=idop[i]).update(reproceso=request.POST[ops[i]])
                elif request.POST['c2'] == 'HUMEDAD':
                    operaciones.objects.filter(id=idop[i]).update(humedad=request.POST[ops[i]])
                elif request.POST['c2'] == 'PH':
                    operaciones.objects.filter(id=idop[i]).update(ph=request.POST[ops[i]])                                                                              
        # ********************************************    
        # Inicio de cabecera 
        # ******************************************** 
        now = datetime.now()  # current date and time
        fecha1 = now.strftime("%Y-%m-%d")
        if kword != None and kword > 1:                                               
            batchs1 = operaciones.objects.filter(idfabricacion = None,idlote=kword).first()
            if batchs1:
                Sem = batchs1.receta_nombre
                idsem = batchs1.receta_id
                idlote = batchs1.idlote
                data1 = batchs1.hora[0:20].replace(" ", "").replace(":","").replace("-","")
                fechatxt2 = datetime.strptime(data1,"%Y%m%d%H%M%S%f")
                fecha2 = fechatxt2.strftime("%Y-%m-%d")
                fecha3 = fechatxt2.strftime("%Y%m%d")
                if Sem == None or Sem =="":
                    Sem = "NO EXISTE EN M.MATERIALES"
                if idlote==None:
                    idlote = 0
            else:
                Sem = "NO EXISTE EN M.MATERIALES"
                idlote = 0
                idsem = 0
                fechatxt2 = None
                    
            batchs2 = operaciones.objects.filter(idfabricacion = None,idlote__gt=0,hora__startswith = fecha3).order_by("id")
            if batchs2:
                listaT = list()
                idl = 0
                for i in batchs2:
                    if i.idlote:                    
                        if idl == 0:
                            listaT.append(i.idlote)
                            idl = i.idlote
                        elif idl != i.idlote:
                            listaT.append(i.idlote)
                            idl = i.idlote                       

            lista1 = em_sp.objects.filter(em__gt = 0).order_by("id")
            lista2 = operaciones.objects.filter(idfabricacion = None,idlote=idlote).order_by("id")
            nolista1 = len(lista1)
            nolista2 = len(lista2)   

            # ********************************************    
            # Fin de cabecera 
            # ********************************************
            # ********************************************    
            # Inicio de cuerpo 
            # ********************************************
            import VisualizacionReporteCremasFuncionX
            resultado = VisualizacionReporteCremasFuncionX.ListarDataTabla(idlote, idsem, idtipo = 0)                
            # ********************************************    
            # Fin de cuerpo 
            # ********************************************                 
        else:
            Sem = "NO EXISTE EN M.MATERIALES"
            idlote = 0

        greeting = {}

        greeting['heading'] = "Producción Actual Diaría En Cremas"+" - Lote: "+ str(idlote)
        greeting['pageview'] = "Fecha: "+ fecha2 +" - "+"Producto: "+ Sem
        greeting['fechatxt'] = fecha1
        greeting['idlotetxt'] = idlote
        greeting['nolista2txt'] = nolista2
        greeting['tabla'] = resultado
        greeting['noturnos'] = listaT
        greeting['nourl'] = 0        

        return render (request,'components/tables/components-edittables1.html',greeting)
     
# ****************************************************    
# Lista los batchs por turno y te premite cerrarlos
# **************************************************** 
class ProductionOrderAddViewX(View):
    form_class = ProductionOrderForm   
    # Metodo que busca y crea las listas para ser mostrada en pantalla
    def get(self , request, kword=None):
        #print('*********GET*********')
        if kword != None and kword > 0:
            # ********************************************    
            # Inicio de cabecera 
            # ******************************************** 
            #print("kword: ",kword)
            now = datetime.now()  # current date and time
            fecha1 = now.strftime("%Y-%m-%d")
            #print("now: ",now) # 2023-09-01 11:42:22.795379
            #print("fecha1: ",fecha1)
            fechatxt1 = now.strftime("%Y-%m-%d %H:%M:%S.%f")
            #print("fecha1: ", fechatxt1)
            idfabricacion = now.strftime("%Y%m%d%H%M%S%f")
            #print("idfabricacion:", idfabricacion)
            batchs1 = operaciones.objects.filter(idfabricacion = None,idlote=kword).first()
            batchs2 = operaciones.objects.filter(idfabricacion = None,idlote=kword).last()
            if batchs1:
                Sem = batchs1.receta_nombre
                idsem = batchs1.receta_id
                idlote = batchs1.idlote
                data1 = batchs1.hora[0:20].replace(" ", "").replace(":","").replace("-","")
                fechatxt2 = datetime.strptime(data1,"%Y%m%d%H%M%S%f")
                fecha2 = fechatxt2.strftime("%Y-%m-%d")
                #print('hora2: ',data1)
                #print('fechatxt2: ',fechatxt2)
                #print('fecha2: ',fecha2)
                if Sem == None or Sem =="":
                    Sem = "NO EXISTE EN M.MATERIALES"
                    idsem = 0
                if idlote==None:
                    idlote = 0
                total = 0
                totalx = 0
                batchs3 = operaciones.objects.filter(idfabricacion = None,idlote=kword)
                for i in batchs3:
                    #print(i.receta_total_kg)
                    if i.receta_total_kg:
                        totalx += i.receta_total_kg
                total = round(totalx,1)
            else:
                Sem = "NO EXISTE EN M.MATERIALES"
                idlote = 0
                idsem = 0
                total = 0
                fechatxt2 = None
            # print("Semi : ",Sem)
            # print("idlote : ",idlote)
            # print("idsem : ",idsem)
            # print("total: ",total)
            if batchs2:
                data2 = batchs2.hora[0:20].replace(" ", "").replace(":","").replace("-","")
                fechatxt3 = datetime.strptime(data2,"%Y%m%d%H%M%S%f")
                #print('hora3: ',data2)                
            else:
                fechatxt3 = None
            #print('fecha3: ',fechatxt3)    
            # ********************************************    
            # Fin de cabecera 
            # ********************************************    
            # Inicio de cuerpo 
            # *********************************************               
            col1 = list()
            col2 = list()
            col3 = list()
            ems = ['em1','em2','em3','em4','em5','em6','em7','em8','em9','em10','em11','em15','em14','reproceso']
            k = 0
            totem1 = totem2 = totem3 = totem4 = totem5 = totem6 = totem7 = totem8 = totem9 = totem10 = totem11 = 0
            totem15 = totem14 = totrep = 0
            lista1 = em_sp.objects.filter(em__gt = 0,em__lt = 17).order_by("id").exclude(em = 3).exclude(em = 4)
            lista2 = operaciones.objects.filter(idfabricacion = None,idlote=kword)            
            nolista1 = len(lista1)
            #print(nolista1)
            #print(lista1)
            #print(lista2)
            x = 0
            for i in lista1:
                rec = rec = RecetasSAP.objects.filter(id_semielaborado = idsem, id_ingrediente = i.ID).first()
                if rec:
                    col1.append(x)
                    col2.append(i.ID)
                    col3.append(0)
                    x += 1
                elif i.ID == 'AGUA':
                    col1.append(x)
                    col2.append(i.ID)
                    col3.append(0)
                    x += 1 
                elif i.ID == 'SE-REPROCESO':
                    col1.append(x)
                    col2.append(i.ID)
                    col3.append(0)
                    x += 1                   
            #print(col1,col2,col3)
            if lista2:
                for i in lista2:
                    if i.em1:
                        totem1 += i.em1
                    if i.em2:
                        totem2 += i.em2
                    if i.em3:
                        totem2 += i.em3
                    if i.em4:
                        totem2 += i.em4
                    if i.em5:
                        totem5 += i.em5
                    if i.em6:
                        totem6 += i.em6
                    if i.em7:
                        totem7 += i.em7
                    if i.em8:
                        totem8 += i.em8
                    if i.em9:
                        totem9 += i.em9
                    if i.em10:
                        totem10 += i.em10
                    if i.em11:
                        totem11 += i.em11                                                
                    if i.em15:
                        totem15 += i.em15
                    if i.em14:
                        totem14 += i.em14
                    if i.reproceso:
                        totrep += i.reproceso                        

            #print(totem1,totem2,totem3,totem4,totem5,totem6,totem7,totem8,totem9,totem10,totem11,totem15,totem14)
            for i in col2:
                #print(i)
                if i == 'MPDC00008':
                    col3[k] = round(totem1,1)
                if i == 'MPDC00004':
                    col3[k] = round(totem2,1)
                if i == 'MPDC00002':
                    col3[k] = round(totem5,1)
                if i == 'AGUA':
                    col3[k] = round(totem6,1)
                if i == 'SE-NEUT001':
                    col3[k] = round(totem7,1)
                if i == 'MPCL00002':
                    col3[k] = round(totem8,1)
                if i == 'MPC000022':
                    col3[k] = round(totem9,1)
                if i == 'MPD000044':
                    col3[k] = round(totem10,1)
                if i == 'MPC000022':
                    col3[k] = round(totem11,1)                                        
                if i == 'MPC000025':
                    col3[k] = round(totem15,1)
                if i == 'MPC000030':
                    col3[k] = round(totem14,1)
                if i == 'SE-REPROCESO':
                    col3[k] = round(totrep,1)                    
                k = k + 1
            #print(col1,col2,col3)
            resultado = zip(col1,col2,col3)
            # ********************************************    
            # Fin de cuerpo 
            # ********************************************
             
            greeting = {}

            greeting['heading'] = "Producción Diaría En Cremas"+" - "+"Lote: "+ str(idlote)
            greeting['pageview'] = "Fecha: "+ fecha2 +" - "+"Producto: "+ Sem
            greeting['fechatxt'] = fecha1
            greeting['fechatxt1'] = str(fechatxt3)[0:22]
            greeting['fechatxt2'] = str(fechatxt2)[0:22]
            greeting['fechatxt3'] = str(fechatxt3)[0:22]
            greeting['idfabricaciontxt'] = idfabricacion[0:16]
            greeting['idlotetxt'] = idlote
            greeting['idsemtxt'] = idsem
            greeting['totaltxt'] = round(total,2)
            greeting['tabla'] = resultado
            greeting['nourl'] = 0
           
        return render (request,'components/orders/components-addorder1.html',greeting)
    
    # Metodo que se ejecuta antes de validar y guardar los datos
    def post(self , request, kword=None):       
        #print('*********POST*********')
        if kword != None and kword > 0:
            # ********************************************    
            # Inicio de datos para la tabla 1
            # ******************************************** 
            #print("kword: ",kword)
            now = datetime.now()  # current date and time
            fecha1 = now.strftime("%Y-%m-%d")
            #print("now: ",now) # 2023-09-01 11:42:22.795379
            #print("fecha1: ",fecha1)
            fechatxt1 = now.strftime("%Y-%m-%d %H:%M:%S.%f")
            #print("fecha1: ", fechatxt1)
            idfabricacion = now.strftime("%Y%m%d%H%M%S%f")
            #print("idfabricacion:", idfabricacion)
            batchs1 = operaciones.objects.filter(idfabricacion = None,idlote=kword).first()
            batchs2 = operaciones.objects.filter(idfabricacion = None,idlote=kword).last()
            if batchs1:
                Sem = batchs1.receta_nombre
                idsem = batchs1.receta_id
                idlote = batchs1.idlote
                data1 = batchs1.hora[0:20].replace(" ", "").replace(":","").replace("-","")
                fechatxt2 = datetime.strptime(data1,"%Y%m%d%H%M%S%f")
                fecha2 = fechatxt2.strftime("%Y-%m-%d")
                #print('hora2: ',data1)
                #print('fecha2: ',fechatxt2)
                if Sem == None or Sem =="":
                    Sem = "NO EXISTE EN M.MATERIALES"
                    idsem = 0
                if idlote==None:
                    idlote = 0
                total = 0

                batchs3 = operaciones.objects.filter(idfabricacion = None,idlote=kword)
                for i in batchs3:
                    #print(i.receta_total_kg)
                    if i.receta_total_kg:
                        total += round(i.receta_total_kg,1)
            else:
                Sem = "NO EXISTE EN M.MATERIALES"
                idlote = 0
                idsem = 0
                total = 0
                fechatxt2 = None
            #print("Semi : ",Sem)
            #print("idlote : ",idlote)
            #print("idsem : ",idsem)
            #print('fecha2: ',fechatxt2)
            #print("total: ",total) 

            if batchs2:
                data2 = batchs2.hora[0:20].replace(" ", "").replace(":","").replace("-","")
                fechatxt3 = datetime.strptime(data2,"%Y%m%d%H%M%S%f")
                #print('hora3: ',data2)
                #print('fecha3: ',fechatxt3)
            else:
                fechatxt3 = None
            #print('fecha3: ',fechatxt3)
            # creo un nuevo registro con los datos en la tabla
            if Sem == "NO EXISTE EN M.MATERIALES":
                idM =  False
            else:
                idM = MaestroDeMateriales.objects.get(id = idsem)
            print("idM: ",idM)
            if idM:               
                obj, created = ProductionOrders1_SAP.objects.get_or_create(
                        series = idlote,
                        itemcode = idM,
                        status = "boposPlanned",
                        type = "S",
                        plannedqty = total,
                        postdate = fechatxt3,
                        startdate = fechatxt2,
                        duedate = fechatxt3,
                        comments = idfabricacion,
                        warehouse = 16
                )
            # # Verifico si lo creo o ya existe 
            if created:
                # Si lo creo, sigo en la misma Url
                print("Se creo un nuevo registro")
            else:
                # Si no, redireciona a otra Url
                print("No se creo un nuevo registro")
            # ********************************************    
            # Fin de los datos de la tabla 1 
            # ********************************************    
            # Inicio de los datos de la tabla 2
            # ********************************************* 
            col1 = list()
            col2 = list()
            col3 = list()
            ems = ['em1','em2','em3','em4','em5','em6','em7','em8','em9','em10','em11','em15','em14','reproceso']
            k = 0
            totem1 = totem2 = totem3 = totem4 = totem5 = totem6 = totem7 = totem8 = totem9 = totem10 = totem11 = 0
            totem15 = totem14 = totrep = 0
            lista1 = em_sp.objects.filter(em__gt = 0,em__lt = 17).order_by("id").exclude(em = 3).exclude(em = 4)
            lista2 = operaciones.objects.filter(idfabricacion = None,idlote=kword)
            nolista1 = len(lista1)
            #print(nolista1)
            #print(lista1)
            #print(lista2)
            x = 0
            for i in lista1:
                rec = RecetasSAP.objects.filter(id_semielaborado = idsem, id_ingrediente = i.ID).first()
                if rec:
                    col1.append(x)
                    col2.append(i.ID)
                    col3.append(0)
                    x += 1
                elif i.ID == 'AGUA':
                    col1.append(x)
                    col2.append(i.ID)
                    col3.append(0)
                    x += 1 
                elif i.ID == 'SE-REPROCESO':
                    col1.append(x)
                    col2.append(i.ID)
                    col3.append(0)
                    x += 1 
            #print(col1,col2,col3)
            if lista2:
                for i in lista2:
                    if i.em1:
                        totem1 += i.em1
                    if i.em2:
                        totem2 += i.em2
                    if i.em3:
                        totem2 += i.em3
                    if i.em4:
                        totem2 += i.em4
                    if i.em5:
                        totem5 += i.em5
                    if i.em6:
                        totem6 += i.em6
                    if i.em7:
                        totem7 += i.em7
                    if i.em8:
                        totem8 += i.em8
                    if i.em9:
                        totem9 += i.em9
                    if i.em10:
                        totem10 += i.em10
                    if i.em11:
                        totem11 += i.em11                                                
                    if i.em15:
                        totem15 += i.em15
                    if i.em14:
                        totem14 += i.em14
                    if i.reproceso:
                        totrep += i.reproceso

            #print(totem1,totem2,totem3,totem4,totem5,totem6,totem7,totem8,totem9,totem15,totem14)
            for i in col2:
                #print(i)
                if i == 'MPDC00008':
                    col3[k] = round(totem1,1)
                if i == 'MPDC00004':
                    col3[k] = round(totem2,1)
                if i == 'MPDC00002':
                    col3[k] = round(totem5,1)
                if i == 'AGUA':
                    col3[k] = round(totem6,1)
                if i == 'SE-NEUT001':
                    col3[k] = round(totem7,1)
                if i == 'MPCL00002':
                    col3[k] = round(totem8,1)
                if i == 'MPC000022':
                    col3[k] = round(totem9,1)
                if i == 'MPD000044':
                    col3[k] = round(totem10,1)
                if i == 'MPC000022':
                    col3[k] = round(totem11,1)                                        
                if i == 'MPC000025':
                    col3[k] = round(totem15,1)
                if i == 'MPC000030':
                    col3[k] = round(totem14,1)
                if i == 'SE-REPROCESO':
                    col3[k] = round(totrep,1)                    
                k = k + 1
            #print(col1,col2,col3)
            resultado = zip(col1,col2,col3)            
            # Crear los registros en la tabla 2
            # Se crea un array para guardar los datos
            insumos = []
            if ProductionOrders1_SAP.objects.filter(series = idlote).exists():
                idPo1 = ProductionOrders1_SAP.objects.get(series = idlote)
                #print("id Prod1: ",idPo1)
                items = 0
                for i in resultado:
                    #print(i[0],i[1],i[2])
                    dato1 = i[0]
                    dato2 = MaestroDeMateriales.objects.filter(id__contains = i[1]).first()
                    dato3 = i[2]
                    #print(dato1)
                    #print(dato2)
                    #print(dato3)
                    
                    if MaestroDeMateriales.objects.filter(id__contains = i[1]).exists() and dato3 > 0:
                        insumo = ProductionOrders2_SAP(
                            parentkey = idPo1,
                            linenum = items,
                            itemcode = dato2,
                            plannedqty = dato3,
                            issuetype = "im_Manual",
                            warehouse = 16,
                            itemtype = 16
                            )                      
                        # Se adiciona cada uno de los datos del for en el array
                        insumos.append(insumo)
                        items = items+1
                # Despues de creado el array se guarda todos los datos en la tabla
                ProductionOrders2_SAP.objects.bulk_create(insumos)

                # Se coloca el id de fabricacion en cada registro guardado
                operaciones.objects.filter(idfabricacion = None,idlote=kword).update(idfabricacion = idfabricacion[0:16])
        
        # Se Busca los Batchs mas viejos que no se han cerrados    
        now = datetime.now()  # current date and time
        fecha1 = now.strftime("%Y-%m-%d") 

        batchs = operaciones.objects.filter(idfabricacion = None,idlote__gt=0).first()
        ultimoRegistro = batchs.hora[0:20].replace(" ", "").replace(":","").replace("-","")
        fechatxt = ultimoRegistro[0:8]

        fecha = fechatxt
        dato = datetime.strptime(fecha,"%Y%m%d")

        fecha2 = dato.strftime("%Y-%m-%d")
        fecha3 = dato.strftime("%Y%m%d")

        Sem = batchs.receta_nombre
        idlote = batchs.idlote

        if Sem == None or Sem =="":
            Sem = "NO EXISTE EN M.MATERIALES"
        if idlote==None:
            idlote = 0

        batchs2 = operaciones.objects.filter(idfabricacion = None,idlote__gt=0,hora__startswith = fecha3).order_by("id")
        if batchs2:
            listaT = list()
            idl = 0
            for i in batchs2:
                if i.idlote:                    
                    if idl == 0:
                        listaT.append(i.idlote)
                        idl = i.idlote
                    elif idl != i.idlote:
                        listaT.append(i.idlote)
                        idl = i.idlote

        lista1 = em_sp.objects.filter(em__gt = 0).order_by("id")
        lista2 = operaciones.objects.filter(idfabricacion = None,idlote=idlote).order_by("id")
        nolista1 = len(lista1)
        nolista2 = len(lista2)
        # ********************************************    
        # Inicio de creacion de la tabla resultado 
        # ******************************************** 
        import VisualizacionReporteCremasFuncionX
        resultado = VisualizacionReporteCremasFuncionX.ListarDataTabla(idlote, idsem, idtipo = 0)  
        # ********************************************    
        # Fin de creacion de la tabla resultado 
        # ******************************************** 

        greeting = {}

        greeting['heading'] = "Producción Actual Diaría En Cremas"+" - Lote: "+ str(idlote)
        greeting['pageview'] = "Fecha: "+ fecha2 +" - "+"Producto: "+ Sem
        greeting['fechatxt'] = fecha2
        greeting['idlotetxt'] = idlote
        greeting['nolista2txt'] = nolista2
        greeting['tabla'] = resultado
        greeting['noturnos'] = listaT
        greeting['nourl'] = 0

        return render (request,'components/tables/components-edittables1.html',greeting)   

# ****************************************************    
# Listar los Batchs por dia y lote (Actuales)
# **************************************************** 
class ListarTabla1View1X(View):
    # Metodo que busca y crea las listas para ser mostrada en pantalla
    def get(self , request, kword=None):
        #print('*********GET*********')
        # ********************************************    
        # Inicio de cabecera 
        # ******************************************** 
        now = datetime.now()  # current date and time
        fecha1 = now.strftime("%Y-%m-%d")
        #print('fecha1: ',fecha1)
        if kword ==1:
            # ********************************************    
            # Datos para la tabla
            # ******************************************** 
            batchs1 = operaciones.objects.filter(idfabricacion = None,idlote__gt=0).first()
            if batchs1:
                Sem = batchs1.receta_nombre
                idsem = batchs1.receta_id
                idlote = batchs1.idlote
                data1 = batchs1.hora[0:20].replace(" ", "").replace(":","").replace("-","")
                fechatxt2 = datetime.strptime(data1,"%Y%m%d%H%M%S%f")
                fecha2 = fechatxt2.strftime("%Y-%m-%d")
                fecha3 = fechatxt2.strftime("%Y%m%d")
                #print('hora:',batchs1.hora)
                #print('hora2: ',data1)
                #print('fechatxt2: ',fechatxt2)
                #print('fecha2: ',fecha2)
                #print('fecha3: ',fecha3)
                if Sem == None or Sem =="":
                    Sem = "NO EXISTE EN M.MATERIALES"
                    idsem = 0
                if idlote==None:
                    idlote = 0
            else:
                Sem = "NO EXISTE EN M.MATERIALES"
                idlote = 0
                idsem = 0
                fechatxt2 = None
            batchs2 = operaciones.objects.filter(idfabricacion = None,idlote__gt=0,hora__startswith = fecha3).order_by("id")
            if batchs2:
                listaT = list()
                idl = 0
                for i in batchs2:
                    if i.idlote:                    
                        if idl == 0:
                            listaT.append(i.idlote)
                            idl = i.idlote
                        elif idl != i.idlote:
                            listaT.append(i.idlote)
                            idl = i.idlote                       
                #print("listaturno: ",listaT)            
            #print("Semi : ",Sem)
            #print("idlote : ",idlote)
            #print("idsem : ",idsem)
            lista1 = em_sp.objects.filter(em__gt = 0).order_by("id")
            lista2 = operaciones.objects.filter(idfabricacion = None,idlote=idlote).order_by("id")
            nolista1 = len(lista1)
            nolista2 = len(lista2)
            #print(nolista1)
            #print(nolista2)
            #print(lista1)
            #print(lista2)
            #print("listaturno: ",listaT)
            # ********************************************    
            # Fin de cabecera 
            # ********************************************
            # ********************************************    
            # Inicio de cuerpo 
            # ********************************************
            import VisualizacionReporteCremasFuncionX
            resultado = VisualizacionReporteCremasFuncionX.ListarDataTabla(idlote, idsem, idtipo = 0)                
            # ********************************************    
            # Fin de cuerpo 
            # ********************************************  
        elif kword != None and kword > 1:
            batchs1 = operaciones.objects.filter(idfabricacion = None,idlote=kword).first()
            if batchs1:
                Sem = batchs1.receta_nombre
                idsem = batchs1.receta_id
                idlote = batchs1.idlote
                data1 = batchs1.hora[0:20].replace(" ", "").replace(":","").replace("-","")
                fechatxt2 = datetime.strptime(data1,"%Y%m%d%H%M%S%f")
                fecha2 = fechatxt2.strftime("%Y-%m-%d")
                fecha3 = fechatxt2.strftime("%Y%m%d")
                #print('hora:',batchs1.hora)
                #print('hora2: ',data1)
                #print('fechatxt2: ',fechatxt2)
                #print('fecha2: ',fecha2)
                #print('fecha3: ',fecha3)
                if Sem == None or Sem =="":
                    Sem = "NO EXISTE EN M.MATERIALES"
                if idlote==None:
                    idlote = 0
            else:
                Sem = "NO EXISTE EN M.MATERIALES"
                idlote = 0
                idsem = 0

            batchs2 = operaciones.objects.filter(idfabricacion = None,idlote__gt=0,hora__startswith = fecha3).order_by("id")
            if batchs2:
                listaT = list()
                idl = 0
                for i in batchs2:
                    if i.idlote:                    
                        if idl == 0:
                            listaT.append(i.idlote)
                            idl = i.idlote
                        elif idl != i.idlote:
                            listaT.append(i.idlote)
                            idl = i.idlote                       
                #print("listaturno: ",listaT)            
            #print("Semi : ",Sem)
            #print("idlote : ",idlote)
            #print("idsem : ",idsem)
            lista1 = em_sp.objects.filter(em__gt = 0).order_by("id")
            lista2 = operaciones.objects.filter(idfabricacion = None,idlote=idlote).order_by("id")
            nolista1 = len(lista1)
            nolista2 = len(lista2)
            #print(nolista1)
            #print(nolista2)
            #print(lista1)
            #print(lista2)
            #print("listaturno: ",listaT)
            # ********************************************    
            # Fin de cabecera 
            # ********************************************
            # ********************************************    
            # Inicio de cuerpo 
            # ********************************************
            import VisualizacionReporteCremasFuncionX
            resultado = VisualizacionReporteCremasFuncionX.ListarDataTabla(idlote, idsem, idtipo = 0)                 
            # ********************************************    
            # Fin de cuerpo 
            # ********************************************                
        else:
            Sem = "NO EXISTE EN M.MATERIALES"
            idlote = 0
            idsem = 0
            fechatxt2 = None
            #print("Semi : ",Sem)
            #print("idlote : ",idlote)
            #print("idsem : ",idsem)
                  
        greeting = {}

        greeting['heading'] = "Producción Actual Diaría En Cremas"+" - Lote: "+ str(idlote)
        greeting['pageview'] = "Fecha: "+ fecha2 +" - "+"Producto: "+ Sem
        greeting['fechatxt'] = fecha2
        greeting['idlotetxt'] = idlote
        greeting['nolista2txt'] = nolista2
        greeting['tabla'] = resultado
        greeting['noturnos'] = listaT
        greeting['nourl'] = 1        
        return render (request,'components/tables/components-viewtables11.html',greeting) 
    
    # Metodo que se ejecuta antes de validar y listar los datos
    def post(self, request, kword = None):
        #print('*********POST*********')
        # ********************************************    
        # Datos para la tabla
        # ******************************************** 

        # ********************************************    
        # Inicio de cabecera 
        # ********************************************        
        now = datetime.now()  # current date and time
        fecha1 = now.strftime("%Y-%m-%d")
        fecha = request.POST.get('fecha')
        #print("Fecha1 input: ",fecha)
        dato = datetime.strptime(fecha,"%Y%m%d")
        fecha2 = dato.strftime("%Y-%m-%d")
        fecha3 = dato.strftime("%Y%m%d")
        #print("fecha2:", fecha2)
        #print("fecha3:", fecha3)       
        batchs1 = operaciones.objects.filter(hora__contains = fecha, idfabricacion = None).first()
        if batchs1:
            Sem = batchs1.receta_nombre
            idsem = batchs1.receta_id
            idlote = batchs1.idlote
            #print("Semi1 : ",Sem)
            #print("idsem : ",idsem)
            #print("idlote1 : ",idlote)
            if Sem == None or Sem =="":
                Sem = "NO EXISTE EN M.MATERIALES"
                idsem = 0
            if idlote==None:
                idlote = 0
        else:
            Sem = "NO EXISTE EN M.MATERIALES"
            idlote = 0
            idsem = 0   
        batchs2 = operaciones.objects.filter(idfabricacion = None,idlote__gt=0,hora__startswith = fecha3).order_by("id")
        #print("batchs2: ",batchs2)
        if batchs2:
            listaT = list()
            idl = 0
            for i in batchs2:
                if i.idlote:                    
                    if idl == 0:
                        listaT.append(i.idlote)
                        idl = i.idlote
                    elif idl != i.idlote:
                        listaT.append(i.idlote)
                        idl = i.idlote                       
            #print("listaturno: ",listaT)
        else:
            listaT = list() 
        lista1 = em_sp.objects.filter(em__gt = 0).order_by("id")
        lista2 = operaciones.objects.filter(idfabricacion = None,idlote=idlote).order_by("id")
        nolista1 = len(lista1)
        nolista2 = len(lista2)
        #print(nolista1)
        #print(nolista2)
        #print(lista1)
        #print(lista2)
        #print("listaturno: ",listaT)        
        # ********************************************    
        # Fin de cabecera 
        # ********************************************
        # ********************************************    
        # Inicio de cuerpo 
        # ********************************************
        import VisualizacionReporteCremasFuncionX
        resultado = VisualizacionReporteCremasFuncionX.ListarDataTabla(idlote, idsem, idtipo = 0)                 
        # ********************************************    
        # Fin de cuerpo 
        # ********************************************  
              
        greeting = {}

        greeting['heading'] = "Producción Actual Diaría En Cremas"+" - Lote: "+ str(idlote)
        greeting['pageview'] = "Fecha: "+ fecha2 +" - "+"Producto: "+ Sem
        greeting['fechatxt'] = fecha1
        greeting['idlotetxt'] = idlote
        greeting['nolista2txt'] = nolista2
        greeting['tabla'] = resultado
        greeting['noturnos'] = listaT
        greeting['nourl'] = 1    
        return render (request,'components/tables/components-viewtables11.html',greeting)

# ****************************************************
# ****************************************************    
# Listar los Batchs por dia y lote
class ListarTabla1View2X(View):
    # Metodo que busca y crea las listas para ser mostrada en pantalla
    def get(self , request, kword=None):
        #print('*********GET*********')
        # ********************************************    
        # Inicio de cabecera 
        # ******************************************** 
        now = datetime.now()  # current date and time
        fecha1 = now.strftime("%Y-%m-%d")
        #print('fecha1: ',fecha1)
        if kword ==1:
            # ********************************************    
            # Datos para la tabla
            # ********************************************
            batchs1 = operaciones.objects.filter(idlote__gt=0).exclude(idfabricacion = None).last()
            if batchs1:
                Sem = batchs1.receta_nombre
                idsem = batchs1.receta_id
                idlote = batchs1.idlote
                data1 = batchs1.hora[0:20].replace(" ", "").replace(":","").replace("-","")
                fechatxt2 = datetime.strptime(data1,"%Y%m%d%H%M%S%f")
                fecha2 = fechatxt2.strftime("%Y-%m-%d")
                fecha3 = fechatxt2.strftime("%Y%m%d")
                #print('hora:',batchs1.hora)
                #print('hora2: ',data1)
                #print('fechatxt2: ',fechatxt2)
                #print('fecha2: ',fecha2)
                #print('fecha3: ',fecha3)
                if Sem == None or Sem =="":
                    Sem = "NO EXISTE EN M.MATERIALES"
                    idsem = 0
                if idlote==None:
                    idlote = 0
            else:
                Sem = "NO EXISTE EN M.MATERIALES"
                idlote = 0
                idsem = 0

            batchs2 = operaciones.objects.filter(idlote__gt=0,hora__startswith = fecha3).exclude(idfabricacion = None).order_by("id")
            if batchs2:
                listaT = list()
                idl = 0
                for i in batchs2:
                    if i.idlote:                    
                        if idl == 0:
                            listaT.append(i.idlote)
                            idl = i.idlote
                        elif idl != i.idlote:
                            listaT.append(i.idlote)
                            idl = i.idlote                       
                #print("listaturno: ",listaT)            
            #print("Semi : ",Sem)
            #print("idlote : ",idlote)
            #print("idsem : ",idsem)

            lista1 = em_sp.objects.filter(em__gt = 0).order_by("id")
            lista2 = operaciones.objects.filter(idlote=idlote).exclude(idfabricacion = None).order_by("id")
            nolista1 = len(lista1)
            nolista2 = len(lista2)
            #print(nolista1)
            #print(nolista2)
            #print(lista1)
            #print(lista2)
            #print("listaturno: ",listaT)
            # ********************************************    
            # Fin de cabecera 
            # ********************************************
            # ********************************************    
            # Inicio de cuerpo 
            # ********************************************
            import VisualizacionReporteCremasFuncionX
            resultado = VisualizacionReporteCremasFuncionX.ListarDataTabla(idlote, idsem, idtipo = 1)                
            # ********************************************    
            # Fin de cuerpo 
            # ********************************************  
        elif kword != None and kword > 1:
            batchs1 = operaciones.objects.filter(idlote=kword).exclude(idfabricacion = None).first()
            if batchs1:
                Sem = batchs1.receta_nombre
                idsem = batchs1.receta_id
                idlote = batchs1.idlote
                data1 = batchs1.hora[0:20].replace(" ", "").replace(":","").replace("-","")
                fechatxt2 = datetime.strptime(data1,"%Y%m%d%H%M%S%f")
                fecha2 = fechatxt2.strftime("%Y-%m-%d")
                fecha3 = fechatxt2.strftime("%Y%m%d")
                #print('hora:',batchs1.hora)
                #print('hora2: ',data1)
                #print('fechatxt2: ',fechatxt2)
                #print('fecha2: ',fecha2)
                #print('fecha3: ',fecha3)
                if Sem == None or Sem =="":
                    Sem = "NO EXISTE EN M.MATERIALES"
                    idsem = 0
                if idlote==None:
                    idlote = 0
            else:
                Sem = "NO EXISTE EN M.MATERIALES"
                idlote = 0
                idsem = 0

            batchs2 = operaciones.objects.filter(idlote__gt=0,hora__startswith = fecha3).exclude(idfabricacion = None).order_by("id")
            if batchs2:
                listaT = list()
                idl = 0
                for i in batchs2:
                    if i.idlote:                    
                        if idl == 0:
                            listaT.append(i.idlote)
                            idl = i.idlote
                        elif idl != i.idlote:
                            listaT.append(i.idlote)
                            idl = i.idlote                       
                #print("listaturno: ",listaT)            
            #print("Semi : ",Sem)
            #print("idlote : ",idlote)
            #print("idsem : ",idsem)
            lista1 = em_sp.objects.filter(em__gt = 0).order_by("id")
            lista2 = operaciones.objects.filter(idlote=idlote).exclude(idfabricacion = None).order_by("id")
            nolista1 = len(lista1)
            nolista2 = len(lista2)
            #print(nolista1)
            #print(nolista2)
            #print(lista1)
            #print(lista2)
            #print("listaturno: ",listaT)
            # ********************************************    
            # Fin de cabecera 
            # ********************************************
            # ********************************************    
            # Inicio de cuerpo 
            # ********************************************
            import VisualizacionReporteCremasFuncionX
            resultado = VisualizacionReporteCremasFuncionX.ListarDataTabla(idlote, idsem, idtipo = 1)                 
            # ********************************************    
            # Fin de cuerpo 
            # ********************************************                
        else:
            Sem = "NO EXISTE EN M.MATERIALES"
            idlote = 0
            idsem = 0
            #print("Semi : ",Sem)
            #print("idlote : ",idlote)
            #print("idsem : ",idsem)
                  
        greeting = {}

        greeting['heading'] = "Producción Historica Diaría En Cremas"+" - Lote: "+ str(idlote)
        greeting['pageview'] = "Fecha: "+ fecha2 +" - "+"Producto: "+ Sem
        greeting['fechatxt'] = fecha2
        greeting['idlotetxt'] = idlote
        greeting['nolista2txt'] = nolista2
        greeting['tabla'] = resultado
        greeting['noturnos'] = listaT
        greeting['nourl'] = 2          
        return render (request,'components/tables/components-viewtables21.html',greeting) 

    # Metodo que se ejecuta antes de validar y lista los datos
    def post(self, request, kword = None):
        #print('*********POST*********')
        # ********************************************    
        # Datos para la tabla
        # ******************************************** 

        # ********************************************    
        # Inicio de cabecera 
        # ********************************************        
        now = datetime.now()  # current date and time
        fecha1 = now.strftime("%Y-%m-%d")
        fecha = request.POST.get('fecha')
        #print("Fecha1 input: ",fecha)
        dato = datetime.strptime(fecha,"%Y%m%d")
        fecha2 = dato.strftime("%Y-%m-%d")
        fecha3 = dato.strftime("%Y%m%d")
        #print("fecha2:", fecha2)
        #print("fecha3:", fecha3)
        Sem = None
        idlote = None        
        batchs1 = operaciones.objects.filter(hora__contains = fecha).exclude(idfabricacion = None).first()
        if batchs1:
            Sem = batchs1.receta_nombre
            idsem = batchs1.receta_id
            idlote = batchs1.idlote
            #print("Semi1 : ",Sem)
            #print("idlote1 : ",idlote)
            if Sem == None or Sem =="":
                Sem = "NO EXISTE EN M.MATERIALES"
                idsem = 0
            if idlote==None:
                idlote = 0
        else:
            Sem = "NO EXISTE EN M.MATERIALES"
            idlote = 0
            idsem = 0
    
        batchs2 = operaciones.objects.filter(idlote__gt=0,hora__startswith = fecha3).exclude(idfabricacion = None).order_by("id")
        #print("batchs2: ",batchs2)
        if batchs2:
            listaT = list()
            idl = 0
            for i in batchs2:
                if i.idlote:                    
                    if idl == 0:
                        listaT.append(i.idlote)
                        idl = i.idlote
                    elif idl != i.idlote:
                        listaT.append(i.idlote)
                        idl = i.idlote                       
            #print("listaturno: ",listaT)
        else:
            listaT = list() 
        #print("Semi2 : ",Sem)
        #print("idlote2 : ",idlote)
        lista1 = em_sp.objects.filter(em__gt = 0).order_by("id")
        lista2 = operaciones.objects.filter(idlote=idlote).exclude(idfabricacion = None).order_by("id")
        nolista1 = len(lista1)
        nolista2 = len(lista2)
        #print(nolista1)
        #print(nolista2)
        #print(lista1)
        #print(lista2)
        #print("listaturno: ",listaT)        
        # ********************************************    
        # Fin de cabecera 
        # ********************************************
        # ********************************************    
        # Inicio de cuerpo 
        # ********************************************
        import VisualizacionReporteCremasFuncionX
        resultado = VisualizacionReporteCremasFuncionX.ListarDataTabla(idlote, idsem, idtipo = 1)                         
        # ********************************************    
        # Fin de cuerpo 
        # ********************************************  
              
        greeting = {}

        greeting['heading'] = "Producción Historica Diaría En Cremas"+" - Lote: "+ str(idlote)
        greeting['pageview'] = "Fecha: "+ fecha2 +" - "+"Producto: "+ Sem
        greeting['fechatxt'] = fecha1
        greeting['idlotetxt'] = idlote
        greeting['nolista2txt'] = nolista2
        greeting['tabla'] = resultado
        greeting['noturnos'] = listaT
        greeting['nourl'] = 2        
        return render (request,'components/tables/components-viewtables21.html',greeting)

# *********************************************************************************
# *********************************************************************************




###################################################################################################
###################################################################################################
###################################################################################################
###################################################################################################
# Editar la tabla de batchs por dia y lote
###################################################################################################

class EditableTablesView(View):
    def get(self , request, kword=None):
        #print('*********GET*********')
        # ********************************************    
        # Inicio de cabecera 
        # ******************************************** 
        now = datetime.now()  # current date and time
        fecha1 = now.strftime("%Y-%m-%d")
        #print('fecha1: ',fecha1)
        if kword ==1:
            # ********************************************    
            # Datos para la tabla
            # ******************************************** 
            batchs1 = operaciones.objects.filter(idfabricacion = None,idlote__gt=0).first()
            if batchs1:
                Sem = batchs1.receta_nombre
                idsem = batchs1.receta_id
                idlote = batchs1.idlote
                data1 = batchs1.hora[0:20].replace(" ", "").replace(":","").replace("-","")
                fechatxt2 = datetime.strptime(data1,"%Y%m%d%H%M%S%f")
                fecha2 = fechatxt2.strftime("%Y-%m-%d")
                fecha3 = fechatxt2.strftime("%Y%m%d")
                #print('hora:',batchs1.hora)
                #print('hora2: ',data1)
                #print('fechatxt2: ',fechatxt2)
                #print('fecha2: ',fecha2)
                #print('fecha3: ',fecha3)
                if Sem == None or Sem =="":
                    Sem = "NO EXISTE EN M.MATERIALES"
                if idlote==None:
                    idlote = 0
            else:
                Sem = "NO EXISTE EN M.MATERIALES"
                idlote = 0
                idsem = 0
                fechatxt2 = None
            batchs2 = operaciones.objects.filter(idfabricacion = None,idlote__gt=0,hora__startswith = fecha3).order_by("id")
            if batchs2:
                listaT = list()
                idl = 0
                for i in batchs2:
                    if i.idlote:                    
                        if idl == 0:
                            listaT.append(i.idlote)
                            idl = i.idlote
                        elif idl != i.idlote:
                            listaT.append(i.idlote)
                            idl = i.idlote                       
                #print("listaturno: ",listaT)            
            #print("Semi : ",Sem)
            #print("idlote : ",idlote)
            #print("idsem : ",idsem)
            #print("total: ",total)
            lista1 = em_sp.objects.filter(em__gt = 0).order_by("id")
            lista2 = operaciones.objects.filter(idfabricacion = None,idlote=idlote).order_by("id")
            nolista1 = len(lista1)
            nolista2 = len(lista2)
            #print(nolista1)
            #print(nolista2)
            #print(lista1)
            #print(lista2)
            #print("listaturno: ",listaT)
            # ********************************************    
            # Fin de cabecera 
            # ********************************************
            # ********************************************    
            # Inicio de cuerpo 
            # ********************************************
            import VisualizacionReporteCremasFuncion
            resultado = VisualizacionReporteCremasFuncion.ListarDataTabla(idlote)                
            # ********************************************    
            # Fin de cuerpo 
            # ********************************************  
        elif kword != None and kword > 1:
            batchs1 = operaciones.objects.filter(idfabricacion = None,idlote=kword).first()
            if batchs1:
                Sem = batchs1.receta_nombre
                idsem = batchs1.receta_id
                idlote = batchs1.idlote
                data1 = batchs1.hora[0:20].replace(" ", "").replace(":","").replace("-","")
                fechatxt2 = datetime.strptime(data1,"%Y%m%d%H%M%S%f")
                fecha2 = fechatxt2.strftime("%Y-%m-%d")
                fecha3 = fechatxt2.strftime("%Y%m%d")
                #print('hora:',batchs1.hora)
                #print('hora2: ',data1)
                #print('fechatxt2: ',fechatxt2)
                #print('fecha2: ',fecha2)
                #print('fecha3: ',fecha3)
                if Sem == None or Sem =="":
                    Sem = "NO EXISTE EN M.MATERIALES"
                if idlote==None:
                    idlote = 0
            else:
                Sem = "NO EXISTE EN M.MATERIALES"
                idlote = 0
                idsem = 0
                fechatxt2 = None
            batchs2 = operaciones.objects.filter(idfabricacion = None,idlote__gt=0,hora__startswith = fecha3).order_by("id")
            if batchs2:
                listaT = list()
                idl = 0
                for i in batchs2:
                    if i.idlote:                    
                        if idl == 0:
                            listaT.append(i.idlote)
                            idl = i.idlote
                        elif idl != i.idlote:
                            listaT.append(i.idlote)
                            idl = i.idlote                       
                #print("listaturno: ",listaT)            
            #print("Semi : ",Sem)
            #print("idlote : ",idlote)
            #print("idsem : ",idsem)
            #print("total: ",total)
            lista1 = em_sp.objects.filter(em__gt = 0).order_by("id")
            lista2 = operaciones.objects.filter(idfabricacion = None,idlote=idlote).order_by("id")
            nolista1 = len(lista1)
            nolista2 = len(lista2)
            #print(nolista1)
            #print(nolista2)
            #print(lista1)
            #print(lista2)
            #print("listaturno: ",listaT)
            # ********************************************  
            # Fin de cabecera 
            # ********************************************
            # ********************************************
            # Inicio de cuerpo 
            # ********************************************
            import VisualizacionReporteCremasFuncion
            resultado = VisualizacionReporteCremasFuncion.ListarDataTabla(idlote)                
            # ********************************************    
            # Fin de cuerpo 
            # ******************************************** 
        else:
            Sem = "NO EXISTE EN M.MATERIALES"
            idlote = 0
            idsem = 0
            total = 0
            fechatxt2 = None
            #print("Semi : ",Sem)
            #print("idlote : ",idlote)
            #print("idsem : ",idsem)
            #print("total: ",total)

        greeting = {}

        greeting['heading'] = "Producción Actual Diaría En Cremas"+" - Lote: "+ str(idlote)
        greeting['pageview'] = "Fecha: "+ fecha2 +" - "+"Producto: "+ Sem
        greeting['fechatxt'] = fecha2
        greeting['idlotetxt'] = idlote
        greeting['nolista2txt'] = nolista2
        greeting['tabla'] = resultado
        greeting['noturnos'] = listaT
        greeting['nourl'] = 0

        return render (request,'components/tables/components-edittables.html',greeting)
    
class TablesUpdateView(View):

    def get(self , request, kword=None, knum=None):
        #print('*********GET*********')
        #print("kword: ",kword)
        #print("knum: ",knum)
        # ********************************************    
        # Inicio de cabecera 
        # ******************************************** 
        now = datetime.now()  # current date and time
        fecha1 = now.strftime("%Y-%m-%d")
        #print('fecha1: ',fecha1)
        if kword != None and kword > 1:                                               
            batchs1 = operaciones.objects.filter(idfabricacion = None,idlote=kword).first()
            if batchs1:
                Sem = batchs1.receta_nombre
                idsem = batchs1.receta_id
                idlote = batchs1.idlote
                data1 = batchs1.hora[0:20].replace(" ", "").replace(":","").replace("-","")
                fechatxt2 = datetime.strptime(data1,"%Y%m%d%H%M%S%f")
                fecha2 = fechatxt2.strftime("%Y-%m-%d")
                fecha3 = fechatxt2.strftime("%Y%m%d")
                if Sem == None or Sem =="":
                    Sem = "NO EXISTE EN M.MATERIALES"
                if idlote==None:
                    idlote = 0
            else:
                Sem = "NO EXISTE EN M.MATERIALES"
                idlote = 0
                idsem = 0
                fechatxt2 = None
                    
            lista1 = em_sp.objects.filter(em__gt = 0).order_by("id")
            lista2 = operaciones.objects.filter(idfabricacion = None,idlote=idlote).order_by("id")
            nolista1 = len(lista1)
            nolista2 = len(lista2)
            #print("nolista1: ",nolista1)
            if knum !=None and knum <= nolista1:
                if knum <= 15:
                    nofila = knum
                else:
                    nofila = 0
            #print("nofila: ", nofila)
            # ********************************************    
            # Fin de cabecera 
            # ********************************************
            # ********************************************    
            # Inicio de cuerpo 
            # ********************************************
            import VisualizacionReporteCremasFuncion
            resultado = VisualizacionReporteCremasFuncion.ListarDataTabla(idlote)                
            # ********************************************    
            # Fin de cuerpo 
            # ********************************************                 
        else:
            Sem = "NO EXISTE EN M.MATERIALES"
            idlote = 0
            #print("Semi : ",Sem)
            #print("idlote : ",idlote)

        greeting = {}

        greeting['heading'] = "Producción Actual Diaría En Cremas"+" - Lote: "+ str(idlote)
        greeting['pageview'] = "Fecha: "+ fecha2 +" - "+"Producto: "+ Sem
        greeting['fechatxt'] = fecha1
        greeting['idlotetxt'] = idlote
        greeting['nolista2txt'] = nolista2
        greeting['nofilatxt'] = nofila
        greeting['tabla'] = resultado
        greeting['nourl'] = 0

        return render (request,'components/tables/components-editablefila.html',greeting)
    
    # Metodo que se ejecuta antes de validar y guardar los datos
    def post(self, request, kword=None, knum=None):
        #self.object = self.get_object()
        #print('*********POST*********')
        #print(request.POST) # Se crea como un diccionario
        #print(request.POST['c5']) # Se consulta como un diccionario
        #print("kword: ",kword)
        #print("knum: ",knum)
        if kword:
            idlote = kword
            idf = knum
            lista1 = operaciones.objects.filter(idfabricacion = None,idlote=idlote).order_by("id")
        else:
            Sem = "NO EXISTE EN M.MATERIALES"
            idlote = 0   
            lista1 = 0
            idf = 0
        nolista1 = len(lista1)
        #print("nolista1: ",nolista1)
        if nolista1 > 20:
            nolista1 = 20
        ems = ['em1','em2','em3','em4','em5','em6','em7','em8','em9','em10','em11','em15','em14','reproceso','em16','humedad','ph']
        ops = ['c5','c6','c7','c8','c9','c10','c11','c12','c13','c14',
               'c15','c16','c17','c18','c19','c20','c21','c22','c23','c24']
        idop = list()
        if lista1:
            for i in lista1:
                idop.append(i.id)
        #print("idop: ",idop)
        noidop = len(idop)
        #print("noidop: ",noidop)
        # Reviso cual fila fue Editada para indicar a que 'em' se le debe cargar
        if idf == 0: # Va para los em1
            for i in range(0,nolista1):
                if idop[i]:
                    operaciones.objects.filter(id=idop[i]).update(em1=request.POST[ops[i]])
        if idf == 1: # Va para los em2
            for i in range(0,nolista1):
                if idop[i]:
                    operaciones.objects.filter(id=idop[i]).update(em2=request.POST[ops[i]])
        if idf == 2: # Va para los em3
            for i in range(0,nolista1):
                if idop[i]:
                    operaciones.objects.filter(id=idop[i]).update(em3=request.POST[ops[i]])
        if idf == 3: # Va para los em4
            for i in range(0,nolista1):
                if idop[i]:
                    operaciones.objects.filter(id=idop[i]).update(em4=request.POST[ops[i]])
        if idf == 4: # Va para los em5
            for i in range(0,nolista1):
                if idop[i]:
                    operaciones.objects.filter(id=idop[i]).update(em5=request.POST[ops[i]])
        if idf == 5: # Va para los em6
            for i in range(0,nolista1):
                if idop[i]:
                    operaciones.objects.filter(id=idop[i]).update(em6=request.POST[ops[i]])
        if idf == 6: # Va para los em7
            for i in range(0,nolista1):
                if idop[i]:
                    operaciones.objects.filter(id=idop[i]).update(em7=request.POST[ops[i]])
        if idf == 7: # Va para los em8
            for i in range(0,nolista1):
                if idop[i]:
                    operaciones.objects.filter(id=idop[i]).update(em8=request.POST[ops[i]])
        if idf == 8: # Va para los em9
            for i in range(0,nolista1):
                if idop[i]:
                    operaciones.objects.filter(id=idop[i]).update(em9=request.POST[ops[i]])
        if idf == 9: # Va para los em10
            for i in range(0,nolista1):
                if idop[i]:
                    operaciones.objects.filter(id=idop[i]).update(em10=request.POST[ops[i]])
        if idf == 10: # Va para los em11
            for i in range(0,nolista1):
                if idop[i]:
                    operaciones.objects.filter(id=idop[i]).update(em11=request.POST[ops[i]])
        if idf == 11: # Va para los em15
            for i in range(0,nolista1):
                if idop[i]:
                    operaciones.objects.filter(id=idop[i]).update(em15=request.POST[ops[i]])
        if idf == 12: # Va para los em14
            for i in range(0,nolista1):
                if idop[i]:
                    operaciones.objects.filter(id=idop[i]).update(em14=request.POST[ops[i]])
        if idf == 13: # Va para los reproceso
            for i in range(0,nolista1):
                if idop[i]:
                    operaciones.objects.filter(id=idop[i]).update(reproceso=request.POST[ops[i]])                    
        if idf == 14: # Va para los humedad
            for i in range(0,nolista1):
                if idop[i]:
                    operaciones.objects.filter(id=idop[i]).update(humedad=request.POST[ops[i]])
        if idf == 15: # Va para los ph
            for i in range(0,nolista1):
                if idop[i]:
                    operaciones.objects.filter(id=idop[i]).update(ph=request.POST[ops[i]])
        # ********************************************    
        # Inicio de cabecera 
        # ******************************************** 
        now = datetime.now()  # current date and time
        fecha1 = now.strftime("%Y-%m-%d")

        if kword != None and kword > 1:                                               
            batchs1 = operaciones.objects.filter(idfabricacion = None,idlote=kword).first()
            if batchs1:
                Sem = batchs1.receta_nombre
                idlote = batchs1.idlote
                data1 = batchs1.hora[0:20].replace(" ", "").replace(":","").replace("-","")
                fechatxt2 = datetime.strptime(data1,"%Y%m%d%H%M%S%f")
                fecha2 = fechatxt2.strftime("%Y-%m-%d")
                fecha3 = fechatxt2.strftime("%Y%m%d")
                if Sem == None or Sem =="":
                    Sem = "NO EXISTE EN M.MATERIALES"
                if idlote==None:
                    idlote = 0
            else:
                Sem = "NO EXISTE EN M.MATERIALES"
                idlote = 0
                idsem = 0
                fechatxt2 = None
                    
            batchs2 = operaciones.objects.filter(idfabricacion = None,idlote__gt=0,hora__startswith = fecha3).order_by("id")
            if batchs2:
                listaT = list()
                idl = 0
                for i in batchs2:
                    if i.idlote:                    
                        if idl == 0:
                            listaT.append(i.idlote)
                            idl = i.idlote
                        elif idl != i.idlote:
                            listaT.append(i.idlote)
                            idl = i.idlote                       

            lista1 = em_sp.objects.filter(em__gt = 0).order_by("id")
            lista2 = operaciones.objects.filter(idfabricacion = None,idlote=idlote).order_by("id")
            nolista1 = len(lista1)
            nolista2 = len(lista2)   

            # ********************************************    
            # Fin de cabecera 
            # ********************************************
            # ********************************************    
            # Inicio de cuerpo 
            # ********************************************
            import VisualizacionReporteCremasFuncion
            resultado = VisualizacionReporteCremasFuncion.ListarDataTabla(idlote)                
            # ********************************************    
            # Fin de cuerpo 
            # ********************************************                 
        else:
            Sem = "NO EXISTE EN M.MATERIALES"
            idlote = 0

        greeting = {}

        greeting['heading'] = "Producción Actual Diaría En Cremas"+" - Lote: "+ str(idlote)
        greeting['pageview'] = "Fecha: "+ fecha2 +" - "+"Producto: "+ Sem
        greeting['fechatxt'] = fecha1
        greeting['idlotetxt'] = idlote
        greeting['nolista2txt'] = nolista2
        greeting['tabla'] = resultado
        greeting['noturnos'] = listaT
        greeting['nourl'] = 0        

        return render (request,'components/tables/components-edittables.html',greeting) 
             
###################################################################################################
###################################################################################################
###################################################################################################

class ProductionOrderAddView(View):
    form_class = ProductionOrderForm   

    def get(self , request, kword=None):
        #print('*********GET*********')
        if kword != None and kword > 0:
            # ********************************************    
            # Inicio de cabecera 
            # ******************************************** 
            #print("kword: ",kword)
            now = datetime.now()  # current date and time
            fecha1 = now.strftime("%Y-%m-%d")
            #print("now: ",now) # 2023-09-01 11:42:22.795379
            #print("fecha1: ",fecha1)
            fechatxt1 = now.strftime("%Y-%m-%d %H:%M:%S.%f")
            #print("fecha1: ", fechatxt1)
            idfabricacion = now.strftime("%Y%m%d%H%M%S%f")
            #print("idfabricacion:", idfabricacion)
            batchs1 = operaciones.objects.filter(idfabricacion = None,idlote=kword).first()
            batchs2 = operaciones.objects.filter(idfabricacion = None,idlote=kword).last()
            if batchs1:
                Sem = batchs1.receta_nombre
                idsem = batchs1.receta_id
                idlote = batchs1.idlote
                data1 = batchs1.hora[0:20].replace(" ", "").replace(":","").replace("-","")
                fechatxt2 = datetime.strptime(data1,"%Y%m%d%H%M%S%f")
                fecha2 = fechatxt2.strftime("%Y-%m-%d")
                #print('hora2: ',data1)
                #print('fechatxt2: ',fechatxt2)
                #print('fecha2: ',fecha2)
                if Sem == None or Sem =="":
                    Sem = "NO EXISTE EN M.MATERIALES"
                if idlote==None:
                    idlote = 0
                total = 0
                totalx = 0
                batchs3 = operaciones.objects.filter(idfabricacion = None,idlote=kword)
                for i in batchs3:
                    #print(i.receta_total_kg)
                    if i.receta_total_kg:
                        totalx += i.receta_total_kg
                total = round(totalx,1)
            else:
                Sem = "NO EXISTE EN M.MATERIALES"
                idlote = 0
                idsem = 0
                total = 0
                fechatxt2 = None
            #print("Semi : ",Sem)
            #print("idlote : ",idlote)
            #print("idsem : ",idsem)
            #print("total: ",total)
            if batchs2:
                data2 = batchs2.hora[0:20].replace(" ", "").replace(":","").replace("-","")
                fechatxt3 = datetime.strptime(data2,"%Y%m%d%H%M%S%f")
                #print('hora3: ',data2)                
            else:
                fechatxt3 = None
            #print('fecha3: ',fechatxt3)    
            # ********************************************    
            # Fin de cabecera 
            # ********************************************    
            # Inicio de cuerpo 
            # *********************************************               
            col1 = list()
            col2 = list()
            col3 = list()
            ems = ['em1','em2','em3','em4','em5','em6','em7','em8','em9','em10','em11','em15','em14','reproceso']
            k = 0
            totem1 = totem2 = totem3 = totem4 = totem5 = totem6 = totem7 = totem8 = totem9 = totem10 = totem11 = 0
            totem15 = totem14 = totrep = 0
            lista1 = em_sp.objects.filter(em__gt = 0,em__lt = 17).order_by("id").exclude(em = 3).exclude(em = 4)
            lista2 = operaciones.objects.filter(idfabricacion = None,idlote=kword)
            nolista1 = len(lista1)
            #print(nolista1)
            #print(lista1)
            #print(lista2)
            x = 0
            for i in lista1:
                #col1.append(i.em)
                col1.append(x)
                col2.append(i.ID)
                col3.append(0)
                x += 1
            #print(col1,col2,col3)
            if lista2:
                for i in lista2:
                    if i.em1:
                        totem1 += i.em1
                    if i.em2:
                        totem2 += i.em2
                    if i.em3:
                        totem2 += i.em3
                    if i.em4:
                        totem2 += i.em4
                    if i.em5:
                        totem5 += i.em5
                    if i.em6:
                        totem6 += i.em6
                    if i.em7:
                        totem7 += i.em7
                    if i.em8:
                        totem8 += i.em8
                    if i.em9:
                        totem9 += i.em9
                    if i.em10:
                        totem10 += i.em10
                    if i.em11:
                        totem11 += i.em11                                                
                    if i.em15:
                        totem15 += i.em15
                    if i.em14:
                        totem14 += i.em14
                    if i.reproceso:
                        totrep += i.reproceso                        

            #print(totem1,totem2,totem3,totem4,totem5,totem6,totem7,totem8,totem9,totem10,totem11,totem15,totem14)
            for i in col1:
                #print(i)
                if i == 0:
                    col3[k] = round(totem1,1)
                if i == 1:
                    col3[k] = round(totem2,1)
                if i == 2:
                    col3[k] = round(totem5,1)
                if i == 3:
                    col3[k] = round(totem6,1)
                if i == 4:
                    col3[k] = round(totem7,1)
                if i == 5:
                    col3[k] = round(totem8,1)
                if i == 6:
                    col3[k] = round(totem9,1)
                if i == 7:
                    col3[k] = round(totem10,1)
                if i == 8:
                    col3[k] = round(totem11,1)                                        
                if i == 9:
                    col3[k] = round(totem15,1)
                if i == 10:
                    col3[k] = round(totem14,1)
                if i == 11:
                    col3[k] = round(totrep,1)                    
                k = k + 1
            #print(col1,col2,col3)
            resultado = zip(col1,col2,col3)
            # ********************************************    
            # Fin de cuerpo 
            # ********************************************
             
            greeting = {}

            greeting['heading'] = "Producción Diaría En Cremas"+" - "+"Lote: "+ str(idlote)
            greeting['pageview'] = "Fecha: "+ fecha2 +" - "+"Producto: "+ Sem
            greeting['fechatxt'] = fecha1
            greeting['fechatxt1'] = str(fechatxt3)[0:22]
            greeting['fechatxt2'] = str(fechatxt2)[0:22]
            greeting['fechatxt3'] = str(fechatxt3)[0:22]
            greeting['idfabricaciontxt'] = idfabricacion[0:16]
            greeting['idlotetxt'] = idlote
            greeting['idsemtxt'] = idsem
            greeting['totaltxt'] = round(total,2)
            greeting['tabla'] = resultado
            greeting['nourl'] = 0
           
        return render (request,'components/orders/components-addorder.html',greeting)
    
    
    def post(self , request, kword=None):       
        #print('*********POST*********')
        if kword != None and kword > 0:
            # ********************************************    
            # Inicio de datos para la tabla 1
            # ******************************************** 
            #print("kword: ",kword)
            now = datetime.now()  # current date and time
            fecha1 = now.strftime("%Y-%m-%d")
            #print("now: ",now) # 2023-09-01 11:42:22.795379
            #print("fecha1: ",fecha1)
            fechatxt1 = now.strftime("%Y-%m-%d %H:%M:%S.%f")
            #print("fecha1: ", fechatxt1)
            idfabricacion = now.strftime("%Y%m%d%H%M%S%f")
            #print("idfabricacion:", idfabricacion)
            batchs1 = operaciones.objects.filter(idfabricacion = None,idlote=kword).first()
            batchs2 = operaciones.objects.filter(idfabricacion = None,idlote=kword).last()
            if batchs1:
                Sem = batchs1.receta_nombre
                idsem = batchs1.receta_id
                idlote = batchs1.idlote
                data1 = batchs1.hora[0:20].replace(" ", "").replace(":","").replace("-","")
                fechatxt2 = datetime.strptime(data1,"%Y%m%d%H%M%S%f")
                fecha2 = fechatxt2.strftime("%Y-%m-%d")
                #print('hora2: ',data1)
                #print('fecha2: ',fechatxt2)
                if Sem == None or Sem =="":
                    Sem = "NO EXISTE EN M.MATERIALES"
                if idlote==None:
                    idlote = 0
                total = 0

                batchs3 = operaciones.objects.filter(idfabricacion = None,idlote=kword)
                for i in batchs3:
                    #print(i.receta_total_kg)
                    if i.receta_total_kg:
                        total += round(i.receta_total_kg,1)
            else:
                Sem = "NO EXISTE EN M.MATERIALES"
                idlote = 0
                idsem = 0
                total = 0
                fechatxt2 = None
            #print("Semi : ",Sem)
            #print("idlote : ",idlote)
            #print("idsem : ",idsem)
            #print('fecha2: ',fechatxt2)
            #print("total: ",total) 

            if batchs2:
                data2 = batchs2.hora[0:20].replace(" ", "").replace(":","").replace("-","")
                fechatxt3 = datetime.strptime(data2,"%Y%m%d%H%M%S%f")
                #print('hora3: ',data2)
                #print('fecha3: ',fechatxt3)
            else:
                fechatxt3 = None
            #print('fecha3: ',fechatxt3)
            # creo un nuevo registro con los datos en la tabla
            if Sem == "NO EXISTE EN M.MATERIALES":
                idM =  False
            else:
                idM = MaestroDeMateriales.objects.get(id = idsem)
            print("idM: ",idM)
            if idM:
                obj, created = ProductionOrders1_SAP.objects.get_or_create(
                        series = idlote,
                        itemcode = idM,
                        status = "boposPlanned",
                        type = "S",
                        plannedqty = total,
                        postdate = fechatxt3,
                        startdate = fechatxt2,
                        duedate = fechatxt3,
                        comments = idfabricacion,
                        warehouse = 16
                )
            # # Verifico si lo creo o ya existe 
            # if created:
            #     # Si lo creo, sigo en la misma Url
            #     print("Se creo un nuevo registro")
            # else:
            #     # Si no, redireciona a otra Url
            #     print("No se creo un nuevo registro")
            # ********************************************    
            # Fin de los datos de la tabla 1 
            # ********************************************    
            # Inicio de los datos de la tabla 2
            # ********************************************* 
            col1 = list()
            col2 = list()
            col3 = list()
            ems = ['em1','em2','em3','em4','em5','em6','em7','em8','em9','em10','em11','em15','em14','reproceso']
            k = 0
            totem1 = totem2 = totem3 = totem4 = totem5 = totem6 = totem7 = totem8 = totem9 = totem10 = totem11 = 0
            totem15 = totem14 = totrep = 0
            lista1 = em_sp.objects.filter(em__gt = 0,em__lt = 17).order_by("id").exclude(em = 3).exclude(em = 4)
            lista2 = operaciones.objects.filter(idfabricacion = None,idlote=kword)
            nolista1 = len(lista1)
            #print(nolista1)
            #print(lista1)
            #print(lista2)
            x = 0
            for i in lista1:
                #col1.append(i.em)
                col1.append(x)
                col2.append(i.ID)
                col3.append(0)
                x += 1
            #print(col1,col2,col3)
            if lista2:
                for i in lista2:
                    if i.em1:
                        totem1 += i.em1
                    if i.em2:
                        totem2 += i.em2
                    if i.em3:
                        totem2 += i.em3
                    if i.em4:
                        totem2 += i.em4
                    if i.em5:
                        totem5 += i.em5
                    if i.em6:
                        totem6 += i.em6
                    if i.em7:
                        totem7 += i.em7
                    if i.em8:
                        totem8 += i.em8
                    if i.em9:
                        totem9 += i.em9
                    if i.em10:
                        totem10 += i.em10
                    if i.em11:
                        totem11 += i.em11                                                
                    if i.em15:
                        totem15 += i.em15
                    if i.em14:
                        totem14 += i.em14
                    if i.reproceso:
                        totrep += i.reproceso

            #print(totem1,totem2,totem3,totem4,totem5,totem6,totem7,totem8,totem9,totem15,totem14)
            for i in col1:
                #print(i)
                if i == 0:
                    col3[k] = round(totem1,1)
                if i == 1:
                    col3[k] = round(totem2,1)
                if i == 2:
                    col3[k] = round(totem5,1)
                if i == 3:
                    col3[k] = round(totem6,1)
                if i == 4:
                    col3[k] = round(totem7,1)
                if i == 5:
                    col3[k] = round(totem8,1)
                if i == 6:
                    col3[k] = round(totem9,1)
                if i == 7:
                    col3[k] = round(totem10,1)
                if i == 8:
                    col3[k] = round(totem11,1)                                        
                if i == 9:
                    col3[k] = round(totem15,1)
                if i == 10:
                    col3[k] = round(totem14,1)
                if i == 11:
                    col3[k] = round(totrep,1)                    
                k = k + 1
            #print(col1,col2,col3)
            resultado = zip(col1,col2,col3)
            # Crear los registros en la tabla 2
            # Se crea un array para guardar los datos
            insumos = []
            if ProductionOrders1_SAP.objects.filter(series = idlote).exists():
                idPo1 = ProductionOrders1_SAP.objects.get(series = idlote)
                #print("id Prod1: "idPo1)
                items = 0
                for i in resultado:
                    #print(i[0],i[1],i[2])
                    dato1 = i[0]
                    dato2 = MaestroDeMateriales.objects.filter(id__contains = i[1]).first()
                    dato3 = i[2]
                    #print(dato1)
                    #print(dato2)
                    #print(dato3)
                    
                    if MaestroDeMateriales.objects.filter(id__contains = i[1]).exists() and dato3 > 0:
                        insumo = ProductionOrders2_SAP(
                            parentkey = idPo1,
                            linenum = items,
                            itemcode = dato2,
                            plannedqty = dato3,
                            issuetype = "im_Manual",
                            warehouse = 16,
                            itemtype = 16
                            )                      
                        # Se adiciona cada uno de los datos del for en el array
                        insumos.append(insumo)
                        items = items+1
                # Despues de creado el array se guarda todos los datos en la tabla
                ProductionOrders2_SAP.objects.bulk_create(insumos)

                # Se coloca el id de fabricacion en cada registro guardado
                operaciones.objects.filter(idfabricacion = None,idlote=kword).update(idfabricacion = idfabricacion[0:16])
        
        # Se Busca los Batchs mas viejos que no se han cerrados    
        now = datetime.now()  # current date and time
        fecha1 = now.strftime("%Y-%m-%d") 

        batchs = operaciones.objects.filter(idfabricacion = None,idlote__gt=0).first()
        ultimoRegistro = batchs.hora[0:20].replace(" ", "").replace(":","").replace("-","")
        fechatxt = ultimoRegistro[0:8]

        fecha = fechatxt
        dato = datetime.strptime(fecha,"%Y%m%d")

        fecha2 = dato.strftime("%Y-%m-%d")
        fecha3 = dato.strftime("%Y%m%d")

        Sem = batchs.receta_nombre
        idlote = batchs.idlote

        if Sem == None or Sem =="":
            Sem = "NO EXISTE EN M.MATERIALES"
        if idlote==None:
            idlote = 0

        batchs2 = operaciones.objects.filter(idfabricacion = None,idlote__gt=0,hora__startswith = fecha3).order_by("id")
        if batchs2:
            listaT = list()
            idl = 0
            for i in batchs2:
                if i.idlote:                    
                    if idl == 0:
                        listaT.append(i.idlote)
                        idl = i.idlote
                    elif idl != i.idlote:
                        listaT.append(i.idlote)
                        idl = i.idlote

        lista1 = em_sp.objects.filter(em__gt = 0).order_by("id")
        lista2 = operaciones.objects.filter(idfabricacion = None,idlote=idlote).order_by("id")
        nolista1 = len(lista1)
        nolista2 = len(lista2)

        import VisualizacionReporteCremasFuncion
        resultado = VisualizacionReporteCremasFuncion.ListarDataTabla(idlote) 

        greeting = {}

        greeting['heading'] = "Producción Actual Diaría En Cremas"+" - Lote: "+ str(idlote)
        greeting['pageview'] = "Fecha: "+ fecha2 +" - "+"Producto: "+ Sem
        greeting['fechatxt'] = fecha2
        greeting['idlotetxt'] = idlote
        greeting['nolista2txt'] = nolista2
        greeting['tabla'] = resultado
        greeting['noturnos'] = listaT
        greeting['nourl'] = 3

        return render (request,'components/tables/components-edittables.html',greeting)   
                
# ****************************************************
# **************************************************** 
# ****************************************************
# ****************************************************    
# Listar los Batchs por dia y lote
class ListarTabla1View1(View):
    def get(self , request, kword=None):
        #print('*********GET*********')
        # ********************************************    
        # Inicio de cabecera 
        # ******************************************** 
        now = datetime.now()  # current date and time
        fecha1 = now.strftime("%Y-%m-%d")
        #print('fecha1: ',fecha1)
        if kword ==1:
            # ********************************************    
            # Datos para la tabla
            # ******************************************** 
            batchs1 = operaciones.objects.filter(idfabricacion = None,idlote__gt=0).first()
            if batchs1:
                Sem = batchs1.receta_nombre
                idsem = batchs1.receta_id
                idlote = batchs1.idlote
                data1 = batchs1.hora[0:20].replace(" ", "").replace(":","").replace("-","")
                fechatxt2 = datetime.strptime(data1,"%Y%m%d%H%M%S%f")
                fecha2 = fechatxt2.strftime("%Y-%m-%d")
                fecha3 = fechatxt2.strftime("%Y%m%d")
                #print('hora:',batchs1.hora)
                #print('hora2: ',data1)
                #print('fechatxt2: ',fechatxt2)
                #print('fecha2: ',fecha2)
                #print('fecha3: ',fecha3)
                if Sem == None or Sem =="":
                    Sem = "NO EXISTE EN M.MATERIALES"
                if idlote==None:
                    idlote = 0
            else:
                Sem = "NO EXISTE EN M.MATERIALES"
                idlote = 0
                idsem = 0
                fechatxt2 = None
            batchs2 = operaciones.objects.filter(idfabricacion = None,idlote__gt=0,hora__startswith = fecha3).order_by("id")
            if batchs2:
                listaT = list()
                idl = 0
                for i in batchs2:
                    if i.idlote:                    
                        if idl == 0:
                            listaT.append(i.idlote)
                            idl = i.idlote
                        elif idl != i.idlote:
                            listaT.append(i.idlote)
                            idl = i.idlote                       
                #print("listaturno: ",listaT)            
            #print("Semi : ",Sem)
            #print("idlote : ",idlote)
            #print("idsem : ",idsem)
            #print("total: ",total)
            lista1 = em_sp.objects.filter(em__gt = 0).order_by("id")
            lista2 = operaciones.objects.filter(idfabricacion = None,idlote=idlote).order_by("id")
            nolista1 = len(lista1)
            nolista2 = len(lista2)
            #print(nolista1)
            #print(nolista2)
            #print(lista1)
            #print(lista2)
            #print("listaturno: ",listaT)
            # ********************************************    
            # Fin de cabecera 
            # ********************************************
            # ********************************************    
            # Inicio de cuerpo 
            # ********************************************
            import VisualizacionReporteCremasFuncion
            resultado = VisualizacionReporteCremasFuncion.ListarDataTabla(idlote)                
            # ********************************************    
            # Fin de cuerpo 
            # ********************************************  
        elif kword != None and kword > 1:
            batchs1 = operaciones.objects.filter(idfabricacion = None,idlote=kword).first()
            if batchs1:
                Sem = batchs1.receta_nombre
                idsem = batchs1.receta_id
                idlote = batchs1.idlote
                data1 = batchs1.hora[0:20].replace(" ", "").replace(":","").replace("-","")
                fechatxt2 = datetime.strptime(data1,"%Y%m%d%H%M%S%f")
                fecha2 = fechatxt2.strftime("%Y-%m-%d")
                fecha3 = fechatxt2.strftime("%Y%m%d")
                #print('hora:',batchs1.hora)
                #print('hora2: ',data1)
                #print('fechatxt2: ',fechatxt2)
                #print('fecha2: ',fecha2)
                #print('fecha3: ',fecha3)
                if Sem == None or Sem =="":
                    Sem = "NO EXISTE EN M.MATERIALES"
                if idlote==None:
                    idlote = 0
            else:
                Sem = "NO EXISTE EN M.MATERIALES"
                idlote = 0
                idsem = 0
                fechatxt2 = None
            batchs2 = operaciones.objects.filter(idfabricacion = None,idlote__gt=0,hora__startswith = fecha3).order_by("id")
            if batchs2:
                listaT = list()
                idl = 0
                for i in batchs2:
                    if i.idlote:                    
                        if idl == 0:
                            listaT.append(i.idlote)
                            idl = i.idlote
                        elif idl != i.idlote:
                            listaT.append(i.idlote)
                            idl = i.idlote                       
                #print("listaturno: ",listaT)            
            #print("Semi : ",Sem)
            #print("idlote : ",idlote)
            #print("idsem : ",idsem)
            #print("total: ",total)
            lista1 = em_sp.objects.filter(em__gt = 0).order_by("id")
            lista2 = operaciones.objects.filter(idfabricacion = None,idlote=idlote).order_by("id")
            nolista1 = len(lista1)
            nolista2 = len(lista2)
            #print(nolista1)
            #print(nolista2)
            #print(lista1)
            #print(lista2)
            #print("listaturno: ",listaT)
            # ********************************************    
            # Fin de cabecera 
            # ********************************************
            # ********************************************    
            # Inicio de cuerpo 
            # ********************************************
            import VisualizacionReporteCremasFuncion
            resultado = VisualizacionReporteCremasFuncion.ListarDataTabla(idlote)                
            # ********************************************    
            # Fin de cuerpo 
            # ********************************************                
        else:
            Sem = "NO EXISTE EN M.MATERIALES"
            idlote = 0
            idsem = 0
            total = 0
            fechatxt2 = None
            #print("Semi : ",Sem)
            #print("idlote : ",idlote)
            #print("idsem : ",idsem)
            #print("total: ",total)
                  
        greeting = {}

        greeting['heading'] = "Producción Actual Diaría En Cremas"+" - Lote: "+ str(idlote)
        greeting['pageview'] = "Fecha: "+ fecha2 +" - "+"Producto: "+ Sem
        greeting['fechatxt'] = fecha2
        greeting['idlotetxt'] = idlote
        greeting['nolista2txt'] = nolista2
        greeting['tabla'] = resultado
        greeting['noturnos'] = listaT
        greeting['nourl'] = 1        
        return render (request,'components/tables/components-viewtables1.html',greeting) 

    def post(self, request, kword = None):
        #print('*********POST*********')
        # ********************************************    
        # Datos para la tabla
        # ******************************************** 

        # ********************************************    
        # Inicio de cabecera 
        # ********************************************        
        now = datetime.now()  # current date and time
        fecha1 = now.strftime("%Y-%m-%d")
        fecha = request.POST.get('fecha')
        #print("Fecha1 input: ",fecha)
        dato = datetime.strptime(fecha,"%Y%m%d")
        fecha2 = dato.strftime("%Y-%m-%d")
        fecha3 = dato.strftime("%Y%m%d")
        #print("fecha2:", fecha2)
        #print("fecha3:", fecha3)
        Sem = None
        idlote = None        
        batchs1 = operaciones.objects.filter(hora__contains = fecha, idfabricacion = None).first()
        if batchs1:
            Sem = batchs1.receta_nombre
            idlote = batchs1.idlote
            #print("Semi1 : ",Sem)
            #print("idlote1 : ",idlote)
        if Sem == None or Sem =="":
            Sem = "NO EXISTE EN M.MATERIALES"
        if idlote==None:
            idlote = 0
        batchs2 = operaciones.objects.filter(idfabricacion = None,idlote__gt=0,hora__startswith = fecha3).order_by("id")
        #print("batchs2: ",batchs2)
        if batchs2:
            listaT = list()
            idl = 0
            for i in batchs2:
                if i.idlote:                    
                    if idl == 0:
                        listaT.append(i.idlote)
                        idl = i.idlote
                    elif idl != i.idlote:
                        listaT.append(i.idlote)
                        idl = i.idlote                       
            #print("listaturno: ",listaT)
        else:
            listaT = list() 
        #print("Semi2 : ",Sem)
        #print("idlote2 : ",idlote)
        lista1 = em_sp.objects.filter(em__gt = 0).order_by("id")
        lista2 = operaciones.objects.filter(idfabricacion = None,idlote=idlote).order_by("id")
        nolista1 = len(lista1)
        nolista2 = len(lista2)
        #print(nolista1)
        #print(nolista2)
        #print(lista1)
        #print(lista2)
        #print("listaturno: ",listaT)        
        # ********************************************    
        # Fin de cabecera 
        # ********************************************
        # ********************************************    
        # Inicio de cuerpo 
        # ********************************************
        import VisualizacionReporteCremasFuncion
        resultado = VisualizacionReporteCremasFuncion.ListarDataTabla(idlote)                
        # ********************************************    
        # Fin de cuerpo 
        # ********************************************  
              
        greeting = {}

        greeting['heading'] = "Producción Actual Diaría En Cremas"+" - Lote: "+ str(idlote)
        greeting['pageview'] = "Fecha: "+ fecha2 +" - "+"Producto: "+ Sem
        greeting['fechatxt'] = fecha1
        greeting['idlotetxt'] = idlote
        greeting['nolista2txt'] = nolista2
        greeting['tabla'] = resultado
        greeting['noturnos'] = listaT
        greeting['nourl'] = 1    
        return render (request,'components/tables/components-viewtables1.html',greeting)

# ****************************************************
# ****************************************************    
# Listar los Batchs por dia y lote
class ListarTabla1View2(View):
    def get(self , request, kword=None):
        #print('*********GET*********')
        # ********************************************    
        # Inicio de cabecera 
        # ******************************************** 
        now = datetime.now()  # current date and time
        fecha1 = now.strftime("%Y-%m-%d")
        #print('fecha1: ',fecha1)
        if kword ==1:
            # ********************************************    
            # Datos para la tabla
            # ********************************************
            batchs1 = operaciones.objects.filter(idlote__gt=0).exclude(idfabricacion = None).last()
            if batchs1:
                Sem = batchs1.receta_nombre
                idsem = batchs1.receta_id
                idlote = batchs1.idlote
                data1 = batchs1.hora[0:20].replace(" ", "").replace(":","").replace("-","")
                fechatxt2 = datetime.strptime(data1,"%Y%m%d%H%M%S%f")
                fecha2 = fechatxt2.strftime("%Y-%m-%d")
                fecha3 = fechatxt2.strftime("%Y%m%d")
                #print('hora:',batchs1.hora)
                #print('hora2: ',data1)
                #print('fechatxt2: ',fechatxt2)
                #print('fecha2: ',fecha2)
                #print('fecha3: ',fecha3)
                if Sem == None or Sem =="":
                    Sem = "NO EXISTE EN M.MATERIALES"
                if idlote==None:
                    idlote = 0
            else:
                Sem = "NO EXISTE EN M.MATERIALES"
                idlote = 0
                idsem = 0
                fechatxt2 = None
            batchs2 = operaciones.objects.filter(idlote__gt=0,hora__startswith = fecha3).exclude(idfabricacion = None).order_by("id")
            if batchs2:
                listaT = list()
                idl = 0
                for i in batchs2:
                    if i.idlote:                    
                        if idl == 0:
                            listaT.append(i.idlote)
                            idl = i.idlote
                        elif idl != i.idlote:
                            listaT.append(i.idlote)
                            idl = i.idlote                       
                #print("listaturno: ",listaT)            
            #print("Semi : ",Sem)
            #print("idlote : ",idlote)
            #print("idsem : ",idsem)
            #print("total: ",total)
            lista1 = em_sp.objects.filter(em__gt = 0).order_by("id")
            lista2 = operaciones.objects.filter(idlote=idlote).exclude(idfabricacion = None).order_by("id")
            nolista1 = len(lista1)
            nolista2 = len(lista2)
            #print(nolista1)
            #print(nolista2)
            #print(lista1)
            #print(lista2)
            #print("listaturno: ",listaT)
            # ********************************************    
            # Fin de cabecera 
            # ********************************************
            # ********************************************    
            # Inicio de cuerpo 
            # ********************************************
            import VisualizacionReporteCremasFuncion
            resultado = VisualizacionReporteCremasFuncion.ListarDataTabla2(idlote)                
            # ********************************************    
            # Fin de cuerpo 
            # ********************************************  
        elif kword != None and kword > 1:
            batchs1 = operaciones.objects.filter(idlote=kword).exclude(idfabricacion = None).first()
            if batchs1:
                Sem = batchs1.receta_nombre
                idsem = batchs1.receta_id
                idlote = batchs1.idlote
                data1 = batchs1.hora[0:20].replace(" ", "").replace(":","").replace("-","")
                fechatxt2 = datetime.strptime(data1,"%Y%m%d%H%M%S%f")
                fecha2 = fechatxt2.strftime("%Y-%m-%d")
                fecha3 = fechatxt2.strftime("%Y%m%d")
                #print('hora:',batchs1.hora)
                #print('hora2: ',data1)
                #print('fechatxt2: ',fechatxt2)
                #print('fecha2: ',fecha2)
                #print('fecha3: ',fecha3)
                if Sem == None or Sem =="":
                    Sem = "NO EXISTE EN M.MATERIALES"
                if idlote==None:
                    idlote = 0
            else:
                Sem = "NO EXISTE EN M.MATERIALES"
                idlote = 0
                idsem = 0
                fechatxt2 = None
            batchs2 = operaciones.objects.filter(idlote__gt=0,hora__startswith = fecha3).exclude(idfabricacion = None).order_by("id")
            if batchs2:
                listaT = list()
                idl = 0
                for i in batchs2:
                    if i.idlote:                    
                        if idl == 0:
                            listaT.append(i.idlote)
                            idl = i.idlote
                        elif idl != i.idlote:
                            listaT.append(i.idlote)
                            idl = i.idlote                       
                #print("listaturno: ",listaT)            
            #print("Semi : ",Sem)
            #print("idlote : ",idlote)
            #print("idsem : ",idsem)
            #print("total: ",total)
            lista1 = em_sp.objects.filter(em__gt = 0).order_by("id")
            lista2 = operaciones.objects.filter(idlote=idlote).exclude(idfabricacion = None).order_by("id")
            nolista1 = len(lista1)
            nolista2 = len(lista2)
            #print(nolista1)
            #print(nolista2)
            #print(lista1)
            #print(lista2)
            #print("listaturno: ",listaT)
            # ********************************************    
            # Fin de cabecera 
            # ********************************************
            # ********************************************    
            # Inicio de cuerpo 
            # ********************************************
            import VisualizacionReporteCremasFuncion
            resultado = VisualizacionReporteCremasFuncion.ListarDataTabla2(idlote)                
            # ********************************************    
            # Fin de cuerpo 
            # ********************************************                
        else:
            Sem = "NO EXISTE EN M.MATERIALES"
            idlote = 0
            idsem = 0
            total = 0
            fechatxt2 = None
            #print("Semi : ",Sem)
            #print("idlote : ",idlote)
            #print("idsem : ",idsem)
            #print("total: ",total)
                  
        greeting = {}

        greeting['heading'] = "Producción Historica Diaría En Cremas"+" - Lote: "+ str(idlote)
        greeting['pageview'] = "Fecha: "+ fecha2 +" - "+"Producto: "+ Sem
        greeting['fechatxt'] = fecha2
        greeting['idlotetxt'] = idlote
        greeting['nolista2txt'] = nolista2
        greeting['tabla'] = resultado
        greeting['noturnos'] = listaT
        greeting['nourl'] = 2          
        return render (request,'components/tables/components-viewtables2.html',greeting) 

    def post(self, request, kword = None):
        #print('*********POST*********')
        # ********************************************    
        # Datos para la tabla
        # ******************************************** 

        # ********************************************    
        # Inicio de cabecera 
        # ********************************************        
        now = datetime.now()  # current date and time
        fecha1 = now.strftime("%Y-%m-%d")
        fecha = request.POST.get('fecha')
        #print("Fecha1 input: ",fecha)
        dato = datetime.strptime(fecha,"%Y%m%d")
        fecha2 = dato.strftime("%Y-%m-%d")
        fecha3 = dato.strftime("%Y%m%d")
        #print("fecha2:", fecha2)
        #print("fecha3:", fecha3)
        Sem = None
        idlote = None        
        batchs1 = operaciones.objects.filter(hora__contains = fecha).exclude(idfabricacion = None).first()
        if batchs1:
            Sem = batchs1.receta_nombre
            idlote = batchs1.idlote
            #print("Semi1 : ",Sem)
            #print("idlote1 : ",idlote)
        if Sem == None or Sem =="":
            Sem = "NO EXISTE EN M.MATERIALES"
        if idlote==None:
            idlote = 0
        batchs2 = operaciones.objects.filter(idlote__gt=0,hora__startswith = fecha3).exclude(idfabricacion = None).order_by("id")
        #print("batchs2: ",batchs2)
        if batchs2:
            listaT = list()
            idl = 0
            for i in batchs2:
                if i.idlote:                    
                    if idl == 0:
                        listaT.append(i.idlote)
                        idl = i.idlote
                    elif idl != i.idlote:
                        listaT.append(i.idlote)
                        idl = i.idlote                       
            #print("listaturno: ",listaT)
        else:
            listaT = list() 
        #print("Semi2 : ",Sem)
        #print("idlote2 : ",idlote)
        lista1 = em_sp.objects.filter(em__gt = 0).order_by("id")
        lista2 = operaciones.objects.filter(idlote=idlote).exclude(idfabricacion = None).order_by("id")
        nolista1 = len(lista1)
        nolista2 = len(lista2)
        #print(nolista1)
        #print(nolista2)
        #print(lista1)
        #print(lista2)
        #print("listaturno: ",listaT)        
        # ********************************************    
        # Fin de cabecera 
        # ********************************************
        # ********************************************    
        # Inicio de cuerpo 
        # ********************************************
        import VisualizacionReporteCremasFuncion
        resultado = VisualizacionReporteCremasFuncion.ListarDataTabla2(idlote)                
        # ********************************************    
        # Fin de cuerpo 
        # ********************************************  
              
        greeting = {}

        greeting['heading'] = "Producción Historica Diaría En Cremas"+" - Lote: "+ str(idlote)
        greeting['pageview'] = "Fecha: "+ fecha2 +" - "+"Producto: "+ Sem
        greeting['fechatxt'] = fecha1
        greeting['idlotetxt'] = idlote
        greeting['nolista2txt'] = nolista2
        greeting['tabla'] = resultado
        greeting['noturnos'] = listaT
        greeting['nourl'] = 2        
        return render (request,'components/tables/components-viewtables2.html',greeting)

# *********************************************************************************
# *********************************************************************************
# *********************************************************************************
# *********************************************************************************
# *********************************************************************************
# *********************************************************************************
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

    