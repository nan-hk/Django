from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('book/', views.BookList.as_view(), name='book_list'),
    path('borrow/<int:pk>', views.borrow_book, name='borrow_book'),
    path('return/<int:pk>', views.return_book, name='return_book'),
    path('view/<int:pk>', views.BookView.as_view(), name='book_view'),
    path('create/', views.create_new_book, name='book_create'),
    path('view/<int:pk>', views.BookView.as_view(), name='book_view'),
    path('edit/<int:pk>', views.BookUpdate.as_view(), name='book_edit'),
    path('delete/<int:pk>', views.BookDelete.as_view(), name='book_delete'),
    path('borrowed/', views.LoanedBooksAllListView.as_view(), name='borrowed'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
