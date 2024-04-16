from django.urls import path
from . import views
from django.conf.urls.static import static

urlpatterns = [
	path('', views.index, name='home'),


	path('blogs', views.blogs_home, name='blogs_home'),
	path('create', views.create, name='create'),
	path('blogs/<int:pk>', views.detail_blog, name='blog-detail'),
	path('blogs/<int:pk>/update', views.BlogsUpdateView.as_view(), name='blogs-update'),
	path('blogs/<int:pk>/delete', views.BlogsDeleteView.as_view(), name='blogs-delete')
]

