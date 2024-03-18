from django import forms
# Models de la BD Empleado
from .models import producciondiaria
class ContactForm(forms.Form):
    name = forms.CharField(label='Nombre')
    email = forms.EmailField(label='Correo electrónico')
    #message = forms.CharField(label='Mensaje', widget=forms.Textarea)
    message = forms.CharField(label='Mensaje')

class TablaProdDiariaForm(forms.ModelForm):

    class Meta:

        model = producciondiaria
        fields = (
            'id','codigo','Nombre','setpoint',
            'op1','op2','op3','op4','op5','op6','op7','op8','op9','op10',
            'op11','op12','op13','op14','op15','op16','op17','op18','op19','op20'
            )
        widgets = {
            'codigo' : forms.TextInput(attrs={'disabled': 'true'}),
            'Nombre' : forms.TextInput(attrs={'disabled': 'true'}),
            'setpoint' : forms.TextInput(attrs={'disabled': 'true'}),
            }
        
class ProductionOrderForm(forms.Form):
    series = forms.IntegerField(label='Series')
    itemcode = forms.CharField(label='ProductNo')
    status = forms.CharField(label='ProductionOrderStatus')
    type = forms.CharField(label='Type')
    plannedqty = forms.DecimalField(label='PlannedQty')
    postdate = forms.DateTimeField(label='OrderDate')
    startdate = forms.DateTimeField(label='StartDate')
    duedate = forms.DateTimeField(label='DueDate')
    comments = forms.CharField(label='Remarks')
    warehouse = forms.CharField(label='Warehouse')
    linenum = forms.IntegerField(label='LineNum')
    itemcode = forms.CharField(label='ItemNo')
    plannedqty2 = forms.DecimalField(label='PlannedQty')
    issuetype = forms.CharField(label='ProductionOrderIssueType')
    warehouse = forms.CharField(label='Warehouse')
    itemtype = forms.IntegerField(label='ItemType')
    stageid = forms.IntegerField(label='StageId')