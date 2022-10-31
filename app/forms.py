from typing import Text
from django.forms import ModelForm
from .models import Text

class TextForm(ModelForm):
    class Meta:
        model = Text
        fields = ['text']
