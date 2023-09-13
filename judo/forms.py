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