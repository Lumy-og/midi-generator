from .models import Midi1
from django.forms import ModelForm, TextInput



class Music1(ModelForm):
    class Meta:
        model= Midi1
        fields=["tempo", "instrument", "repeats", "track", "mood"]

        widgets = {


            "track": TextInput(attrs={
                'class': "form-control me-2",
                'placeholder': "track",
                "type": "text"

            }),

            "tempo": TextInput(attrs={
                'class': "form-control me-2",
                'placeholder': "Введите темп",
                "type": "text"
            }),

            "instrument": TextInput(attrs={
                'class': "form-control me-2",
                'placeholder': "Выберите инструмент",
                "type": "text"

            }),

            "repeats": TextInput(attrs={
                'class': "form-control me-2",
                'placeholder': "Введите кол-во повторений",
                "type": "text"

            }),

            "mood": TextInput(attrs={
                'class': "form-control me-2",
                'placeholder': "Выберите настроение",
                "type": "text"

            }),

        }



class Music2(ModelForm):
    class Meta:
        model= Midi1
        fields=["tempo", "instrument", "repeats", "track", "mood"]

        widgets = {


            "track": TextInput(attrs={
                'class': "form-control input-default",
                'placeholder': "track",
                "type": "text"

            }),

            "tempo": TextInput(attrs={
                'class': "form-control input-default",
                'placeholder': "Введите темп",
                "type": "text"
            }),

            "instrument": TextInput(attrs={
                'class': "form-control input-default",
                'placeholder': "Выберите инструмент",
                "type": "text"

            }),

            "repeats": TextInput(attrs={
                'class': "form-control input-default",
                'placeholder': "Введите кол-во повторений",
                "type": "text"

            }),

            "mood": TextInput(attrs={
                'class': "form-control",
                'placeholder': "Выберите настроение",
                "type": "text"

            }),

        }