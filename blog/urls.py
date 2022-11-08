from django.urls import path

from .views import index

app_name = 'blog'
urlpatterns = [
   # path('', index, name='index'),
    #path('<int:article_id>/', views.detail, name='detail'),
]