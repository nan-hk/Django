from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from datetime import date


class Book(models.Model):
    id = models.IntegerField(primary_key=True, help_text='Unique ID for this particular book across whole library')
    title = models.CharField(max_length=64)
    author = models.CharField(max_length=20)
    publisher = models.CharField(max_length=20)
    rentalStatus = models.IntegerField()
    summary = models.CharField(max_length=200)
    releaseDate = models.DateField()
    category = models.CharField(max_length=20)
    genre = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True)

    class Meta:
        ordering = ['releaseDate']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('book-detail', args=[str(self.id)])


class Borrow(models.Model):
    """Model representing a specific copy of a book (i.e. that can be borrowed from the library)."""
    id = models.AutoField(primary_key=True, help_text='Unique ID for this particular book across whole library')
    due_back = models.DateField(null=True, blank=True)
    borrower = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='user', null=True, blank=True)
    borrow_date = models.DateField(null=True, blank=True)
    return_date = models.DateField(null=True, blank=True)
    book = models.ForeignKey('Book', on_delete=models.CASCADE, related_name='book', null=True, blank=True)

    @property
    def is_overdue(self):
        if self.due_back and date.today() > self.due_back:
            return True
        return False

    LOAN_STATUS = (
        ('d', 'Maintenance'),
        ('o', 'On loan'),
        ('a', 'Available'),
        ('r', 'Reserved'),
    )

    status = models.CharField(
        max_length=1,
        choices=LOAN_STATUS,
        blank=True,
        default='d',
        help_text='Book availability')

    class Meta:
        ordering = ['due_back']
        permissions = (("can_mark_returned", "Set book as returned"),)

    def __str__(self):
        """String for representing the Model object."""
        return '{0} ({1})'.format(self.id, self.book.title)


class Category(models.Model):
    """Model representing a book genre."""
    name = models.CharField(max_length=200, help_text='Enter a book genre (e.g. Science Fiction)')

    def __str__(self):
        """String for representing the Model object."""
        return self.name
