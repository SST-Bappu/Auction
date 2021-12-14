from django import forms
from django.contrib.admin.widgets import AdminDateWidget,AdminTimeWidget
from django.forms import widgets
from .models import *

class AuctionForm(forms.ModelForm):
    class Meta:
        model = auctionItem
        fields = ['product_name','description','min_bid','photo','end_date']
        widgets = {
            'end_date': widgets.DateInput(attrs={'type':'date'}),
        }
    

        
