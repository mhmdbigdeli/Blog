from django.urls import path 
from . import views

app_name = "blog"
#https://docs.djangoproject.com/en/5.0/topics/http/urls/
urlpatterns = [
    path('blog/', views.index, name="index"),
    path('posts/', views.post_list, name="post_list"),
    path('posts/<int:id>', views.post_detail, name="post_detail")
]

