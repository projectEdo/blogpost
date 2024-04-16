from django.shortcuts import render, redirect
from .forms import LoginUserForm, SignForm
from django.contrib.auth import authenticate, login, logout

def account(request):

	if request.user.is_authenticated:
		logout(request)

	return render(request, 'blog/index.html', {'title' : 'Главная'})



# Регистрация пользователя
def regist_user(request):
	error = ''
	if request.method == 'POST':
		form = SignForm(request.POST)
		if form.is_valid():
			cd = form.cleaned_data
			new_user = form.save(commit=False)
			new_user.set_password(cd['password'])
			form.save()
			return redirect('login')
		else:
			error = 'Форма была неверной'

	form = SignForm()

	data = {
		'form' : form,
		'error' : error
	}

	return render(request, 'account/regist.html', data)



# Авторизация пользователя
def user_login(request):
	error = ''
	if request.method == 'POST':
		next_url = request.POST.get('next', '/')
		form = LoginUserForm(request.POST)
		if form.is_valid():
			cd = form.cleaned_data
			user = authenticate(request, username=cd['username'], password=cd['password'])
			if user and user.is_active:
				login(request, user)
				return redirect(next_url)
			else: 
				error = 'Пользователь не найден!'
		else: 
			error = 'Пользователь не найден!'
			
	data = {
		'form' : LoginUserForm(),
		'title' : 'Войти',
		'error' : error
	}
	return render(request, 'account/login.html', data)
