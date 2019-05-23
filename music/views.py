#from django.shortcuts import render,get_object_or_404
#from django.http import Http404
 
#from django.http import HttpResponse
#from django.template import loader
#from .models import Album,Song

from django.views import generic
from .models import Album
from django.views.generic.edit import CreateView,DeleteView,UpdateView


class IndexView(generic.ListView):
	template_name='music/index.html'
	context_object_name= 'all_albums'


	def get_queryset(self):
		return Album.objects.all()

class DetailView(generic.DetailView):
	model=Album
	template_name='music/detail.html'

class AlbumCreate(CreateView):
	model=Album
	fields=['artist','album_title','album_logo','genre']


