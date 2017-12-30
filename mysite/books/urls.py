from django.urls import path

from . import views

urlpatterns = [
    path('publishers/', views.PublisherList.as_view(), name='publisher-list'),
    path('publishers/<int:pk>/', views.PublisherDetail.as_view(), name='publisher-detail'),
    
    path('books/', views.BookList.as_view(), name='book-list'),
    path('books/<publisher>/', 
        views.PublisherBookList.as_view, 
        name='publisher-book-list'),

    path('authors/<int:pk>/', 
        views.AuthorDetailView.as_view(), 
        name='author-detail'),
]