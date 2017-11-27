from django import forms
from .models import User


class UserForm(forms.ModelForm):
    first_name = forms.CharField(required=True, label='* First name')
    last_name = forms.CharField(required=True, label='* Last name')
    email = forms.EmailField(required=True, label='* Email')
    phone_num = forms.CharField(
        widget=forms.TextInput(attrs={'type': 'tel', 'maxlength': 11, }),
        label='* Phone number',
        required=True
    )
    password = forms.CharField(
        widget=forms.PasswordInput(),
        required=True,
        label='* Password'
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(),
        required=True,
        label='* Confirm password'
    )
    default_pickup_addr = forms.CharField(required=False)

    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'phone_num', 'password', 'password2']

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(UserForm, self).__init__(*args, **kwargs)

    def clean_password2(self, *args, **kwargs):
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')

        if password != password2:
            raise forms.ValidationError("passwords must match.")

        return password

    def clean_email(self, *args, **kwargs):
        email = self.cleaned_data.get('email')

        # if not self.request.user.is_authenticated:
        email_qs = User.objects.filter(email=email)
        if email_qs:
            raise forms.ValidationError("This e-mail has already been registered")

        return email


# class UserEditForm(forms.ModelForm):
