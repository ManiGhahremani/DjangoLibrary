from django.contrib import admin

# Register your models here.

from .models import Author, Genre, Language, Book, BookInstance

# We have commented out the ones that are overwritten using admin functions.
#admin.site.register(Book)
admin.site.register(Language)
#admin.site.register(BookInstance)
admin.site.register(Genre)
#admin.site.register(Author)
# Define the admin class

class BooksInline(admin.TabularInline):
    """Defines format of inline book insertion (used in AuthorAdmin) """
    model=Book

class AuthorAdmin(admin.ModelAdmin):
    """Administration object for Author models.
    Defines:
    - fields to be displayed in list view (list_display)
    - orders fields in detail view (fields), grouping the date fields horizontally
    - adds inline addition of book in author view (inlines) [scroll to the bottom
    of an author page to add books written by him/her]
    """

    list_display=('last_name','first_name','date_of_birth','date_of_death')
    fields=['first_name','last_name', ('date_of_birth', 'date_of_death')]
    inlines=[BooksInline]

# Register the admin author class with the associated model
admin.site.register(Author, AuthorAdmin)

class BookInstanceInline(admin.TabularInline):
    """Defines format of inline book instance insertion used in (BookAdmin)"""
    model = BookInstance


class BookAdmin(admin.ModelAdmin):
    """Administration object for Book models:
    Defines:
    - fields to be displayed in list view (list_display)
    - adds inline addition of book instances in book view (inlines)
    """
    list_display=('title','author','display_genre')
    inlines = [BookInstanceInline]

# Register the admin book class with associated model
admin.site.register(Book, BookAdmin)


class BookInstanceAdmin(admin.ModelAdmin):
    """Administration object for BookInstace models.
    Defines:
    - fields to be displayed in list view (list_display)
    - filters that will be displayed in sidebar (list_filter)
    - grouping of fields into sections (fieldsets)
    """
    list_display=('book','status', 'borrower' ,'due_back','id')
    list_filter=('status', 'due_back')


    fieldsets=(
        (None, {
            'fields': ('book', 'imprint', 'id')
        }),
        ('Availability',{
            'fields': ('status', 'due_back', 'borrower')
        }),
    )

# Register the Admin classes for BookInstace
admin.site.register(BookInstance)
