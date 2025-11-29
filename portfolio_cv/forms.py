from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(
        label="Nombre",
        max_length=80,
        widget=forms.TextInput(attrs={
            "class": "w-full border border-gray-700 rounded px-3 py-2 bg-gray-900/40 text-gray-100",
            "placeholder": "Tu nombre",
        }),
    )
    email = forms.EmailField(
        label="Correo",
        widget=forms.EmailInput(attrs={
            "class": "w-full border border-gray-700 rounded px-3 py-2 bg-gray-900/40 text-gray-100",
            "placeholder": "tucorreo@ejemplo.com",
        }),
    )
    message = forms.CharField(
        label="Mensaje",
        widget=forms.Textarea(attrs={
            "class": "w-full border border-gray-700 rounded px-3 py-2 bg-gray-900/40 text-gray-100 h-32",
            "placeholder": "Cuéntame en qué te puedo ayudar",
        }),
    )
