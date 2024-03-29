from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_view, name='index'),
    path('movie/<int:pk>/detail/',views.DetailMovieView.as_view(),name='detail-movie'),
    path('movie/<int:movie_id>/review', views.CreateReviewView.as_view(),name='review'),
    path('movie/search',views.DiarySearch.as_view(),name='search'),
    path('japan/',views.JapanMovieView.as_view(),name='japan'),
    path('world/',views.WorldMovieView.as_view(),name='world'),
    path('anime/',views.AnimeMovieView.as_view(),name='anime'),
    path('review/<int:pk>/delete/',views.DeleteReviewView.as_view(),name='delete-review'),
]