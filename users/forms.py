from django import forms
from .models import User


class UserForm(forms.ModelForm):
    first_name = forms.CharField(required=True, label='* First name')
    last_name = forms.CharField(required=True, label='* Last name')
    email = forms.EmailField(label='Email')
    phone_num = forms.CharField(
        widget=forms.TextInput(attrs={'type': 'tel', 'maxlength': 11, }),
        label='* Phone number',
        required=True
    )
    password = forms.CharField(widget=forms.PasswordInput(), required=True, label='* Password')
    password2 = forms.CharField(widget=forms.PasswordInput, required=True, label='* Confirm password')
    default_pickup_addr = forms.CharField(required=True)

    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'phone_num', 'password', 'password2']

    def clean_password2(self, *args, **kwargs):
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')

        if password != password2:
            raise forms.ValidationError("Emails must match.")

        email_qs = User.objects.filter(email=email)
        if email_qs:
            raise forms.ValidationError("This E-mail has already been registered")

        return password


# class UserEditForm(forms.ModelForm):
