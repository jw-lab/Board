from django import forms

def mobile_validator(value):
    if len(str(value)) != 11:
        raise forms.ValidationError('error')
