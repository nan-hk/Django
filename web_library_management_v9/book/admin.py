from django.contrib import admin
from book.models import Book, Borrow, Category
# Register your models here.


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    pass


class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'publisher', 'rentalStatus', 'summary', 'releaseDate', 'category')


@admin.register(Borrow)
class BorrowAdmin(admin.ModelAdmin):
    pass


class BookInstanceAdmin(admin.ModelAdmin):
    list_filter = ('status', 'due_back')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass
# @admin.register(BookInstance)
# class BookInstanceAdmin(admin.ModelAdmin):
#     list_display = ('book', 'status', 'borrower', 'due_back', 'id')
#     list_filter = ('status', 'due_back')
#
#     fieldsets = (
#         (None, {
#             'fields': ('book', 'imprint', 'id')
#         }),
#         ('Availability', {
#             'fields': ('status', 'due_back', 'borrower')
#         }),
#     )
