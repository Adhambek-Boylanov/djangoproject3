from django import forms
from .models import  Room,Deal,User


class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = "__all__"

class DealForm(forms.ModelForm):
    class Meta:
        model = Deal
        fields = "__all__"


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = "__all__"