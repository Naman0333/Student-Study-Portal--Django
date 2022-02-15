from django import forms
from . models import *
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from string import punctuation

class NotesForm(forms.ModelForm):
    class Meta:
        model = Notes
        fields = ['title','description']

    def clean(self):
        cleaned_Data = super().clean()
        title = self.cleaned_data.get('title')
        if title.startswith('abc') or title.startswith('ABC'):
            raise forms.ValidationError('Enter valid title')
        for i in punctuation:
            if i in title:
                raise forms.ValidationError('Special Character not allowed')

class DateInput(forms.DateInput):
    input_type = 'date'

class HomeworkForm(forms.ModelForm):
    class Meta:
        model = Homework
        widgets = {'due' : DateInput()}
        fields = ['subject','title','description','due','is_finished']

class DashboardForm(forms.Form):
    text = forms.CharField(max_length=100, label='Enter your search')

class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['title','is_finished']

    def clean(self):
        cleaned_Data = super().clean()
        title = self.cleaned_data.get('title')
        if title.startswith('abc') or title.startswith('ABC'):
            raise forms.ValidationError('Enter valid title')
        for i in punctuation:
            if i in title:
                raise forms.ValidationError('Special Character not allowed')


class ConversionForm(forms.Form):
    CHOICES = [('length','Length'),('mass','Mass')]
    measurement = forms.ChoiceField(choices=CHOICES,widget=forms.RadioSelect)

class ConversionLengthForm(forms.Form):
    CHOICES = [('yard','Yard'),('foot','Foot')]
    input = forms.CharField(required=False,label=False,widget=forms.TextInput(
        attrs={'type':'number','placeholder':"Enter the number"}
    ))
    measure1 = forms.CharField(
        label="",widget=forms.Select(choices=CHOICES)
    )
    measure2 = forms.CharField(
        label="",widget=forms.Select(choices=CHOICES)
    )

class ConversionMassForm(forms.Form):
    CHOICES = [('pound','Pound'),('kilogram','Kilogram')]
    input = forms.CharField(required=False,label=False,widget=forms.TextInput(
        attrs={'type':'number','placeholder':"Enter the number"}
    ))
    measure1 = forms.CharField(
        label="",widget=forms.Select(choices=CHOICES)
    )
    measure2 = forms.CharField(
        label="",widget=forms.Select(choices=CHOICES)
    )
class UserRegistrationForm(UserCreationForm):
    mobile_no = forms.CharField(max_length=10, required=True,widget=forms.TextInput(attrs={'placeholder': 'Not Required +91'}),help_text='Enter valid mobile number, please.')
    class Meta:
        model = User
        fields =['username','password1','password2','mobile_no']

    def clean(self):
        cleaned_data = super().clean()
        username = self.cleaned_data.get('username')
        mobile_no = self.cleaned_data.get('mobile_no')
        if username.startswith('ABC') or username.startswith('abc') or (username.isdigit()) or len(username)<4:
            raise forms.ValidationError('Invalid Username')
        if mobile_no.isdigit() == False or len(mobile_no) < 10 or username.startswith('012345'):
            raise forms.ValidationError('Invalid mobile_no')
        for i in punctuation:
            if i in mobile_no:
                raise forms.ValidationError('Special Character not allowed in Mobile no.')


