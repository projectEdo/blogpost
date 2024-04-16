from django.db import models
from django.contrib.auth.models import User

class Articles(models.Model):
	author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор', null=True, blank=True)
	title = models.CharField('Название', max_length=50)
	anons = models.CharField('Анонс', max_length=250)
	full_text = models.TextField('Блог')
	image = models.ImageField('Изображение', null=True, blank=True, upload_to='images/')
	date = models.DateTimeField('Дата публикации')

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return f'/blogs/{self.id}'

	class Meta:
		verbose_name = 'Блог'
		verbose_name_plural = 'Блоги'


class Comment(models.Model):
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	article = models.ForeignKey(Articles, on_delete=models.CASCADE)
	text = models.TextField('Коммент', max_length=500)
	date_created = models.DateTimeField('Дата публикации')	

	class Meta:
		verbose_name = 'Коммент'
		verbose_name_plural = 'Комментарии'