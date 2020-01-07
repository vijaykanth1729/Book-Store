from django.urls import path
from .views import create_book, home, update_book, detail_book, delete_book
app_name = 'books'
urlpatterns = [
    path('', home, name='home'),
    path('<int:id>/', detail_book, name='detail'),
    path('create/', create_book,name='create'),
    path('<int:id>/update/', update_book, name='update'),
    path('<int:id>/delete/', delete_book, name='delete')
]

