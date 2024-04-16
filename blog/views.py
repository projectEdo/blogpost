from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import Articles, Comment
from .forms import ArticlesForm, CommentForm
from django.views.generic import UpdateView, DeleteView


def blogs_home(request):
	blogs = Articles.objects.order_by('-date')
	return render(request, 'blog/blogs_home.html', {'blogs' : blogs})


class BlogsUpdateView(UpdateView):
	model = Articles
	template_name = 'blog/create.html'

	form_class = ArticlesForm


class BlogsDeleteView(DeleteView):
	model = Articles
	success_url = '/blogs'
	template_name = 'blog/blog-delete.html'


def detail_blog(request, pk):
	article = get_object_or_404(Articles, pk=pk)
	if request.method == 'POST':
		if 'comment_create' in request.POST:
			form = CommentForm(request.POST)
			if form.is_valid():
				comm = form.save(commit=False)
				comm.author = request.user
				comm.article = article
				comm.date_created = timezone.now()
				form.save()	
				return redirect('blog-detail', pk=pk)
	form = CommentForm()

	comment = Comment.objects.filter(article = article).order_by('-date_created');

	data = {
		'comment' : comment,
		'form' : form,
		'article' : article,
	}

	return render (request, 'blog/datails_view.html', data)


def create(request):
	error = ''
	if request.method == 'POST':
		form = ArticlesForm(request.POST, request.FILES)
		if form.is_valid():
			art = form.save(commit=False)
			art.author = request.user
			art.date = timezone.now()
			form.save()
			return redirect('blogs_home')
		else:
			error = 'Форма была неверной'

	form = ArticlesForm()

	data = {
		'form' : form,
		'error' : error
	}

	return render(request, 'blog/create.html', data)


# Главная страница
def index(request):
	return render(request, 'blog/index.html') 

