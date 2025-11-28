from django.urls  import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('create-book', views.createBook, name='createBook'),
    path('read-books', views.readBooks, name='readBooks')
]