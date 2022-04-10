from django import forms
from .models import *

from .models import Contact

# class ContactForm(forms.ModelForm):
#     class Meta:
#         model = Syrfull
#         fields = '__all__'
        # widgets = {
        #     'title' : forms.TextInput(attrs={'class':'form-control'}),
        #     'text': forms.TextInput(attrs={'class': 'form-control'}),
        #     'video': forms.FilePathField(attrs={'class': 'form-control'}),
        #     # 'promo': forms.Textarea(attrs={'class': 'form-control'}),
        #
        # }



# creating a form
class ContactForm(forms.ModelForm):
    # create meta class
    class Meta:
        # specify model to be used
        model = Syrfull

        # specify fields to be used
        fields = '__all__'


