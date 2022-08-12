from cProfile import label
from distutils.command.upload import upload
from email.policy import default
from enum import unique
from django import forms 
from .models import *
from .forms import *


class Signup(forms.ModelForm):
    gender = (('M', 'Male'), ('F', 'Female'))
    gender_select = forms.ChoiceField(widget = forms.RadioSelect, choices=gender)
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'', 'required':True}),label='Password', max_length=20)
    confirm_password = forms.CharField(widget = forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'', 'required':True}), label='Confirm Password', max_length=20)

    class Meta:
        model = CustomUser()
        fields = ['__all__']

        def check_passwords(self):
            # Checking that the two password entries match
            password = self.cleaned_data.get('password')
            password2 = self.cleaned_data.get('confirm_password')
            if password and password2 and password != password2:
                raise forms.ValidationError("Password don't match")
            return password2
        def save(self, commit=True):
            # Save the provided password in hashed format
            user = super().save(commit=False)
            user.set_password(self.cleaned_data["password"])
            if commit:
                user.save()
            return user
    
    
class login(forms.Form):
    model = login()
    fields = ['__a__']
    email = forms.EmailField(widget = forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Email', 'required':True}), label='Email', max_length=50)
    password = forms.CharField(widget = forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Password', 'required':True}), label='Password', max_length=50)


class Create_Event_class(forms.Form):
    model = Create_Event
    fields = '__a__'
    event_names = [('business', 'Business Meeting'),
    ('wedding', 'Wedding Ceremony'), 
    ('child', 'Child Dedication'), 
    ('burial', 'Funeral Ceremony'), 
    ('engage', 'Engagement Party'), 
    ('shower', 'Bridal Shower'),
    ('bachelor', 'Bachelor/Bachelorette Party'),
    ('birthday', 'Birthday Party'),
    ('divorce', 'Divorce Party')]

    nature_of_event = forms.CharField(widget = forms.Select(choices=event_names), label='Nature of Event')

    title_of_event = forms.CharField(widget = forms.TextInput(attrs={'class':'form-control', 'required':True}), label='Title of Event', max_length=100)

    number_of_guests = forms.IntegerField(widget = forms.NumberInput(attrs={'class':'form-control', 'required':True}), label='Number of Guests')

    address = forms.CharField(widget = forms.Textarea(attrs={'required':True}), max_length=100)

    date_time = forms.DateTimeField(widget = forms.widgets.DateTimeInput(attrs={'type':'datetime-local'}), label= 'Date et Time')

    hash_tag = forms.CharField(widget = forms.TextInput(attrs={'class':'form-control', 'placeholder':'YOLO 2022'}), label = 'Hashtag/Code')

    rsvp = forms.IntegerField(widget = forms.TextInput(attrs={'class':'form-control', 'placeholder':'Number to Call', 'required':True}), label='R S V P')

    flyer_image = forms.ImageField()

    def __str__(self):
        return (self.flyer_image, self.title_of_event, self.hash_tag, self.address, self.rsvp)


    # flyer_image = forms.ImageField(widget= forms.ImageField())
        # def __init__(self):
        #     super().__init__()
        #     self.fields['state'].queryset = State.objects.none()
        #     self.fields['city'].queryset = City.objects.none()
      
            
