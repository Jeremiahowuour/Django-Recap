from django.urls  import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('create-book', views.createBook, name='createBook'),
    path('read-books', views.readBooks, name='readBooks'),
    path('read-one-book/<str:pk>', views.readOneBook, name='readOneBook'),
    path('update-book/<str:pk>', views.updateBook, name='updateBook'),
    path('delete-book/<str:pk>', views.deleteBook, name='deleteBook'),
]