from django import forms

from .models import *


class addstudent(forms.ModelForm):
    class Meta:
        model = StudentRecords
        fields = ['sname', 'fname', 'mname', 'gender', 'clas', 'roll', 'paper1', 'paper2', 'paper3', 'paper4', 'paper5']
        widgets = {
            'sname': forms.TextInput(attrs={'placeholder':'Enter student"s Name', 'class':'form-control'}),
            'fname': forms.TextInput(attrs={'placeholder': 'Enter Father"s Name', 'class': 'form-control'}),
            'mname': forms.TextInput(attrs={'placeholder': 'Enter Mother"s Name', 'class': 'form-control'}),
            'gender': forms.Select(attrs={'class': 'form-control'}),
            'clas': forms.TextInput(attrs={'placeholder':'Class', 'class': 'form-control'}),
            'roll': forms.TextInput(attrs={'placeholder':'Roll No.', 'class': 'form-control'}),
            'paper1': forms.TextInput(attrs={'placeholder':'Marks of Paper1', 'class': 'form-control'}),
            'paper2': forms.TextInput(attrs={'placeholder':'Marks of Paper2', 'class': 'form-control'}),
            'paper3': forms.TextInput(attrs={'placeholder':'Marks of Paper3', 'class': 'form-control'}),
            'paper4': forms.TextInput(attrs={'placeholder':'Marks of Paper4', 'class': 'form-control'}),
            'paper5': forms.TextInput(attrs={'placeholder':'Marks of Paper5', 'class': 'form-control'})
        }