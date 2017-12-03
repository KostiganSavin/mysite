from django import forms
from .models import CustomerCommentModel

class CustomerCommentForm(forms.ModelForm):

    class Meta:
        model = CustomerCommentModel
        