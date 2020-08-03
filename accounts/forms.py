from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from relpi_mi_back import settings

from .models import User


class UserAdminCreationForm(forms.ModelForm):
    """
    A form for creating new users. Includes all the required
    fields, plus a repeated password.
    """
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('email','full_name','birth_date','cidade')

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Senhas não coinscidem!")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(UserAdminCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserAdminChangeForm(forms.ModelForm):

    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ('email', 'password', 'active', 'admin','full_name','birth_date','cidade')

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]


class DateInput(forms.DateInput):
    input_type = 'date'


class RegisterForm(forms.ModelForm):

    SRS = 'Santa Rita do Sapucai'

    CIDADES = [
        (SRS,'Santa Rita do Sapucai')
    ]

    full_name = forms.CharField(max_length=255)
    birth_date = forms.DateField(input_formats=['%Y-%m-%d'],widget=DateInput)
    cidade = forms.ChoiceField(
        choices=CIDADES
    )
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('email','full_name','birth_date','cidade')
        labels = {
            "birth_date":"Data de nascimento",
            "full_name":"Nome completo"
        }

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Senhas não coincidem!")
        return password2

    def save(self, commit=True):
        user = super(RegisterForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        user.active = True #Confirmação de email
        if commit:
            user.save()
        return user

