from django import forms
import re
from django.core.exceptions import ValidationError

class RegisterForm(forms.Form):
    username = forms.CharField(label="Логін", max_length=100)
    password = forms.CharField(label="Пароль", widget=forms.PasswordInput)

    def clean_password(self):
        password = self.cleaned_data['password']

        if len(password) < 8:
            raise ValidationError("Пароль повинен містити щонайменше 8 символів.\nПароль повинен містити хоча б одну велику літеру.\nПароль повинен містити хоча б одну цифру.")
        if not re.search(r'[A-Z]', password):
            raise ValidationError("Пароль повинен містити хоча б одну велику літеру.\nПароль повинен містити хоча б одну цифру.")
        if not re.search(r'\d', password):
            raise ValidationError("Пароль повинен містити хоча б одну цифру.")

        return password