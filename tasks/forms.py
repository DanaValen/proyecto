from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields =['title', 'descripcion', 'important']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'write a title' }),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'write a description'}),
            'important': forms.CheckboxInput(attrs={'class': 'form-check-input text-center'})
}