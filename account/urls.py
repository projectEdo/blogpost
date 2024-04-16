from django.urls import path
from . import views

urlpatterns = [
	path('', views.account, name='logout'),
	path('regist', views.regist_user, name='sign-up'),
	path('login', views.user_login, name='login'),
]