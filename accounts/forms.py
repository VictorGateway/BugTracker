from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser
from django import forms
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.forms import AuthenticationForm

class CustomChangeForm(UserChangeForm):
    class Meta(UserChangeForm):
        model=CustomUser
        fields=("email", "company", "position", )

        widgets = {
            'username'  : forms.Textarea(attrs={'class': 'usernamefield'}),
            'password'  : forms.PasswordInput(attrs={'class': 'passwordfield'}),
        }

        def __init__(self, *args, **kwargs):
            super(CustomChangeForm, self).__init__(*args, **kwargs)
            self.fields['username'].widget.attrs['class'] = 'emailfield'
            self.fields['password'].widget.attrs['class'] = 'passwordfield'

class CustomCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model=CustomUser
        fields= ('email','first_name', 'last_name', 'company' , 'password1' ,'password2', 'position' )

        widgets = {
            'email'  : forms.TextInput(attrs={'class': 'emailfield'}),
            'company'  : forms.TextInput(attrs={'class': 'emailfield'}),
            'first_name'  : forms.TextInput(attrs={'class': 'emailfield'}),
            'last_name'  : forms.TextInput(attrs={'class': 'emailfield'}),
            'position'  : forms.TextInput(attrs={'class': 'emailfield'}),
            # 'username'  : forms.TextInput(attrs={'class': 'usernamefield'}),
            # 'email'  : forms.TextInput(attrs={'class': 'usernamefield'}),
        }

    def __init__(self, *args, **kwargs):
        super(CustomCreationForm, self).__init__(*args, **kwargs)

        
        self.fields['password1'].widget.attrs['class'] = 'emailfield'
        self.fields['password2'].widget.attrs['class'] = 'emailfield'