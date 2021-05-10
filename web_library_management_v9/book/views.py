from datetime import date, datetime, timedelta
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from .forms import CreateBookForm
from book.models import Book, Borrow


# Create your views here.


def index(request):
    """View function for home page of site."""
    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html')


class BookList(ListView):
    model = Book


class LoanedBooksAllListView(ListView):
    """Generic class-based view listing all books on loan. Only visible to users with can_mark_returned permission."""
    model = Borrow
    template_name = 'book/bookinstance_list_borrowed_user.html'

    def get_queryset(self):
        return Borrow.objects.filter(status__exact='o').order_by('due_back')


class BookView(DetailView):
    model = Book


class BookCreate(CreateView):
    template_name = 'book/book_create.html'
    model = Book
    fields = '__all__'
    success_url = reverse_lazy('book_list')


class BookUpdate(UpdateView):
    model = Book
    fields = '__all__'
    success_url = reverse_lazy('book_list')


class BookDelete(DeleteView):
    model = Book
    success_url = reverse_lazy('book_list')


def create_new_book(request):
    if request.method == "POST":
        form = CreateBookForm(request.POST)
        if form.is_valid():
            book = form.save(commit=False)
            book.rentalStatus = 0
            book.save()
            return redirect('book_list')
    else:
        form = CreateBookForm()
    return render(request, 'book/book_create.html', {'form': form})


def borrow_book(request, pk):
    book_instance = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        if request.user.is_authenticated:
            book_instance.rentalStatus = 1
            book_instance.save()
            borrow = Borrow(borrower=request.user,
                            due_back=date.today() + timedelta(days=3),
                            borrow_date=date.today(),
                            book=book_instance,
                            status='o'
                            )

            borrow.save()
        return HttpResponseRedirect(reverse('borrowed'))

    context = {
        'book_instance': book_instance,
    }
    return render(request, 'bookinstance_list_borrowed_user.html', context)


def return_book(request, pk):
    book_instance = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        if request.user.is_authenticated:
            book_instance.rentalStatus = 0
            book_instance.book.return_date = date.today()
            book_instance.save()
        return HttpResponseRedirect(reverse('book_list'))

    context = {
        'book_instance': book_instance,
    }
    return render(request, 'book_form.html', context)
