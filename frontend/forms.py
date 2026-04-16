from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={
            'placeholder': 'Your Name',
            'class': 'tp-contact-input'
        })
    )
    
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'placeholder': 'Email Here',
            'class': 'tp-contact-input'
        })
    )
    
    message = forms.CharField(
        widget=forms.Textarea(attrs={
            'placeholder': 'Message Here',
            'class': 'tp-contact-input'
        })
    )