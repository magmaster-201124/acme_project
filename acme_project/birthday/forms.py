from django import forms

from .models import Birthday


class BirthdayForm(forms.ModelForm):

    # Все настройки задаём в подклассе Meta.
    class Meta:
        # Указываем модель, на основе которой должна строиться форма.
        model = Birthday
        # Указываем, что надо отобразить все поля.
        fields = '__all__'
        # Все настройки задаём в подклассе Meta.
        widgets = {
            'birthday': forms.DateInput(attrs={'type': 'date'})
        }
