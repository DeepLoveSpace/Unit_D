from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from allauth.account.forms import SignupForm
from django.contrib.auth.models import Group
from django.core.mail import EmailMultiAlternatives


class SignUpForm(UserCreationForm):
    email = forms.EmailField(label='Email')
    first_name = forms.CharField(label='Имя')
    last_name = forms.CharField(label='Фамилия')

    class Meta:
        model = User
        fields = (
            "username",
            "first_name",
            "last_name",
            "email",
            "password1",
            "password2",
        )



class CustomSignupForm(SignupForm):
    def save(self, request):
        user = super().save(request)
        authors_grupp = Group.objects.get(name='authors')
        user.groups.add(authors_grupp)

        subject = 'Добро пожаловать в наш новостной портал!'
        text = f'{user.username}, вы успешно зарегистрировались на сайте!'
        html = (
            f'<a>{user.username}</a>, вы успешно зарегистрировались на сайте новостей: '
            f'<a href="http://127.0.0.1:8000/news"></a>!'
        )
        msg = EmailMultiAlternatives(
            subject=subject, body=text, from_email=None, to=[user.email]
        )
        msg.attach_alternative(html, "text/html")
        msg.send()

        return user