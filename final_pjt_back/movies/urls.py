from django.urls import path
from . import views

app_name = 'movies'
urlpatterns = [
    path('', views.movielist, name='movielist'),
    path('<int:movie_pk>/', views.moviedetail, name='moviedetail'),
    path('<int:movie_pk>/reviews/', views.review_create),
    path('<int:movie_pk>/reviews_read/', views.review_read),
    path('reviews/<int:review_pk>/', views.review_detail_update_delete),
    path('recommend/', views.movie_recommend),
    # path('api-token-auth/', obtain_jwt_token),
]
