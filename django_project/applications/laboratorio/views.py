# Import REST FRAMEWORK
from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    RetrieveAPIView,
    DestroyAPIView,
    UpdateAPIView,
    RetrieveUpdateAPIView
)
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework import status
from rest_framework.response import Response
# Import Django
from django.shortcuts import render
from django.contrib import messages
from django.views.generic import (
    View, 
    ListView, 
    DetailView,
    CreateView,
    TemplateView,
    UpdateView,
    DeleteView
    )
from django.contrib.auth.models import User
# Local Serializers
from .serializers import (
    ReporteLABSerializer
    )
# Import datetime  
from datetime import date, datetime, timedelta
# Local Models de la BD
from .models import (
    ReporteLAB
    )
# Create your views here.
# ********************************************************************************************
# ********************************************************************************************
# List View from ReporteLAB for range fecha SAP in an Url
class ListaReporteLAB_API1(ListAPIView):
    serializer_class = ReporteLABSerializer
    def get_queryset(self):
        fecha1 = self.kwargs['fecha1']
        dato1 = datetime.strptime(fecha1,"%Y-%m-%d")
        fecha2 = self.kwargs['fecha2']
        dato2 = datetime.strptime(fecha2,"%Y-%m-%d")
        if dato1 and dato2: 
            if dato2 > dato1: return ReporteLAB.objects.reporte_range_datetime_1(dato1,dato2)
            else: return ReporteLAB.objects.reporte_range_datetime_1(dato2,dato1)
        else: return Response({'error':' No se envio fechas validas'}, status = status.HTTP_400_BAD_REQUEST)

# List View from ReporteLAB for range fecha SAP in an Url
class ListaReporteLAB_API2(ListAPIView):
    serializer_class = ReporteLABSerializer
    # Paquete que desencripta y autentifica el usuario atreves de un token
    authentication_classes = (TokenAuthentication,)
    permission_classes = [IsAuthenticated,]
    def get_queryset(self):
        # Recuperar usuario
        usuario = self.request.user
        # Valido si esta activo el usuario
        if usuario.is_active:
            fecha1 = self.kwargs['fecha1']
            dato1 = datetime.strptime(fecha1,"%Y-%m-%d")
            fecha2 = self.kwargs['fecha2']
            dato2 = datetime.strptime(fecha2,"%Y-%m-%d")
            if dato1 and dato2: 
                if dato2 > dato1: return ReporteLAB.objects.reporte_range_datetime_1(dato1,dato2)
                else: return ReporteLAB.objects.reporte_range_datetime_1(dato2,dato1)
            else: return Response({'error':' No se envio fechas validas'}, status = status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'Error':'Este usuario no puede iniciar sesion'}, status = status.HTTP_401_UNAUTHORIZED)
# ********************************************************************************************
# ********************************************************************************************