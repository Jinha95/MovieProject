from django.urls import path
from . import views

from rest_framework_jwt.views import obtain_jwt_token

app_name = 'community'
urlpatterns = [
    path('', views.article_read, name='article_read'),
    path('articles/create/', views.article_create, name='article_create'),
    path('<int:article_pk>/', views.article_update_delete_detail, name='article_update_delete_detail'),
    
    path('articles/<int:article_pk>/comments/', views.comment_create),
    path('<int:article_pk>/comments/', views.comment_read),
    path('comments/<int:comment_pk>/', views.comment_detail_update_delete),

    path('api-token-auth/', obtain_jwt_token),
]