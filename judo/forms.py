from django import forms
from judo.models import FAQ, UserProfile,Item
from django.contrib.auth.models import User

class FAQForm(forms.ModelForm):
    class Meta:
        model = FAQ
        fields = ('question', 'answer')

    def __init__(self, *args, **kwargs):
        super(FAQForm, self).__init__(*args, **kwargs)
        self.fields['question'].widget.attrs.update({'class': 'form-control'})
        self.fields['answer'].widget.attrs.update({'class': 'form-control', 'rows': 4})

class FAQEditForm(forms.ModelForm):
    class Meta:
        model = FAQ
        fields = ('question', 'answer')

    def __init__(self, *args, **kwargs):
        super(FAQEditForm, self).__init__(*args, **kwargs)
        self.fields['question'].widget.attrs.update({'class': 'form-control'})
        self.fields['answer'].widget.attrs.update({'class': 'form-control', 'rows': 4})

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('name', 'price', 'picture')

class EditItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('name', 'price', 'picture')  # Include the fields you want to edit

    def __init__(self, *args, **kwargs):
        super(EditItemForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'form-control'})
        self.fields['price'].widget.attrs.update({'class': 'form-control'})
        self.fields['picture'].widget.attrs.update({'class': 'form-control-file'})