from django.forms import ModelForm
from .models import Customer, Category
from django import forms
from .models import Splitter


class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = ('service_id', 'name', 'address', 'phone', 'parent'
                  )
        labels = {
            'name': 'Customer Name',
            'service_id': 'Service ID',
            'splitter32': '32 way splitter',
            'phone': 'Phone',
            'ont': 'ONT Number',
        }


class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = (
            'parent', 'name', 'location', 'description', 'status', 'slug', 'sn'
        )

        labels = {
            'parent': 'Parent',
            'description': 'Description',
            'location': 'Location'
        }


class SplitterForm(forms.ModelForm):
    class Meta:
        model = Splitter
        fields = ['location', 'name', 'parent']
