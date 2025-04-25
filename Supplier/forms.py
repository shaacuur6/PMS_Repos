from django.forms import ModelForm,TextInput,Select,DateInput
from Supplier.models import Supplier

class Supplier_Form(ModelForm):
    class Meta:
        model = Supplier
        #fields =['Name','Tel','Gender','Address']
        fields='__all__'
       
        widgets = {
            'Name': TextInput(attrs={
                'class': "form-control",
                'style': 'width: 100%;'
                }),
            'Tel': TextInput(attrs={
                'class': "form-control", 
                'style': 'width: 100%;'
                }),
            'Gender': Select(attrs={
                'class': "form-control", 
                'style': 'width: 100%;'
                }),
            'Address': TextInput(attrs={
                'class': "form-control", 
                'style': 'width: 100%;'
                }),
            'Created_By': Select(attrs={
                'class': "form-control", 
                'style': 'width: 100%;'
                }),
            'Updated_By': Select(attrs={
                'class': "form-control", 
                'style': 'width: 100%;'
                }),
            'Reg_Date': DateInput(attrs={
                'class': "form-control", 
                'type': 'date',
                'style': 'width: 100%;'
                }),
            'Updated_At': DateInput(attrs={
                'class': "form-control", 
                'type': 'date',
                'style': 'width: 100%;'
                }),
            
            
            
                
        }
        