from .models import Articles, Comment
from django.forms import ModelForm, TextInput, Textarea, FileInput, ClearableFileInput

class ArticlesForm(ModelForm):
	class Meta:
		model = Articles
		fields = ['title', 'anons', 'full_text', 'image']

		widgets = {
			'title' : TextInput(attrs={
				'class' : 'form-control',
				'placeholder' : 'Название блога',
			}),
			'anons' : TextInput(attrs={
				'class' : 'form-control',
				'placeholder' : 'Анонс блога',
			}),
			'full_text' : Textarea(attrs={
				'class' : 'form-control',
				'placeholder' : 'Текст блога'
			}),
			'image' : ClearableFileInput(attrs={
				'class' : 'form-image',
				'placeholder' : 'Изображение'
			})
		}

class CommentForm(ModelForm):
	class Meta:
		model = Comment
		fields = ['text']

		widgets = {
			'text' : Textarea(attrs={
				'class' : 'comment-input',
				'placeholder' : 'Текст комментария'
			})
		}
