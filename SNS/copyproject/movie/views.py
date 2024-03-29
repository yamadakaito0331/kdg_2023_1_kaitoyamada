from typing import Any
from django.db.models.query import QuerySet
from django.forms.models import BaseModelForm
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views.generic import DetailView,CreateView,ListView,DeleteView
from .models import Movie,Review
from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Avg
from django.core.paginator import Paginator
from.consts import ITEM_PER_PAGE,ITEM_PER_PAGE2

class DetailMovieView(LoginRequiredMixin,DetailView):
    template_name ='movie/movie_detail.html'
    model = Movie
    def get(self, request, *args, **kwargs):
        movie = self.get_object()
        movie.avg_rating = movie.review_set.aggregate(Avg('rate'))['rate__avg']
        return render(request, 'movie/movie_detail.html', {'object': movie})
def index_view(request):
    object_list = Movie.objects.annotate(avg_rating=Avg('review__rate')).order_by('?')
    ranking_list = Movie.objects.annotate(avg_rating=Avg('review__rate')).order_by('-avg_rating') 

    paginator = Paginator(ranking_list,ITEM_PER_PAGE)
    page_number = request.GET.get('page',1)
    page_obj = paginator.page(page_number)
    

    paginator2 = Paginator(object_list,ITEM_PER_PAGE2)
    page_number2 = request.GET.get('page',1)
    page_obj2 = paginator2.page(page_number2)


    

    return render (request, 'movie/index.html',{'object_list': object_list,'ranking_list':ranking_list,'page_obj':page_obj,'page_obj2':page_obj2},)
    

   




class CreateReviewView(LoginRequiredMixin,CreateView):
    model = Review
    fields = ('movie', 'title', 'text','rate')
    template_name = 'movie/review_form.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['movie'] = Movie.objects.get(pk=self.kwargs['movie_id'])
        return context
    
    def form_valid(self, form):
        form.instance.user = self.request.user

        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse('detail-movie',kwargs={'pk': self.object.movie.id})

        
    

class DiarySearch(ListView):
    model = Movie
    template_name = 'movie/index.html'

    def get_queryset(self):
        query = super().get_queryset()
        title = self.request.GET.get('title', None)
        if title:
            query = query.filter(title__icontains=title)
        if title:
            # タイトルでフィルタリング
            query = query.filter(title__icontains=title)
            
            # 平均評価を計算し、結果に追加
            query = query.annotate(avg_rating=Avg('review__rate'))
        
        return query
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["query"] = self.get_queryset()
        context["title"] = self.request.GET.get('title', '')
        return context

class JapanMovieView(ListView):
    template_name = 'movie/japan_list.html'
    model = Movie
    context_object_name = 'japan_list'
    
    def get_queryset(self):
        # 映画に平均評価をアノテート
        queryset = Movie.objects.annotate(avg_rating=Avg('review__rate'))
        return queryset

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
    
class WorldMovieView(ListView):
    template_name = 'movie/world_list.html'
    model = Movie
    context_object_name = 'world_list'

    def get_queryset(self):
        queryset = Movie.objects.annotate(avg_rating=Avg('review__rate'))
        return queryset

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
    
class AnimeMovieView(ListView):
    template_name = 'movie/anime_list.html'
    model = Movie
    context_object_name = 'anime_list'

    def get_queryset(self):
        queryset = Movie.objects.annotate(avg_rating=Avg('review__rate'))
        return queryset

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
     
class DeleteReviewView(DeleteView):
    template_name = 'movie/movie_confirm_delete.html'
    model = Review
    success_url = reverse_lazy('index')