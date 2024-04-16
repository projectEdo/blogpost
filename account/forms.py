from django.contrib.auth.models import User
from django.forms import ModelForm, TextInput, Form, CharField, PasswordInput



class SignForm(ModelForm):

	password = CharField(label='Пароль', widget=PasswordInput(attrs={
				'class' : 'form-input',
				'placeholder' : 'Пароль'
			})) # Поле 'Пароль'
	
	password_two = CharField(label='Повторный пароль', widget=PasswordInput(attrs={
				'class' : 'form-input',
				'placeholder' : 'Повторите пароль'
			})) # Поле 'Повторите пароль'

	class Meta:
		

		model = User
		fields = ['username', 'first_name']

		widgets = {
			'first_name' : TextInput(attrs={
				'class' : 'form-input',
				'placeholder' : 'Имя',
			}), # Виджет для поля 'Имя'
			'username' : TextInput(attrs={
				'class' : 'form-input',
				'placeholder' : 'Логин'
			}), # Виджет для поля 'Логин'
		}



# Форма для авторизации пользователей
class LoginUserForm(Form):
	username = CharField(label='Логин', widget=TextInput(attrs={
		'class': 'form-input',
		'placeholder' : 'Логин'
		})) # Поле 'Логин' 

	password = CharField(label='Пароль', widget=PasswordInput(attrs={
		'class' : 'form-input',
		'placeholder' : 'Пароль'
	})) # Поле 'Пароль'