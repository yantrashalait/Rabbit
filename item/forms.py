from django import forms
from item.models import Message, OrderInfo

class ContactForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['full_name', 'email', 'phone_number', 'address', 'message']

class ShopForm(forms.ModelForm):
    class Meta:
        model = OrderInfo
        fields = ['product_name', 'email', 'phone_number', 'quantity', 'address', 'note']
