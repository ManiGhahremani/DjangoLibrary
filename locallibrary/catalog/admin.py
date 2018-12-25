from django.contrib import admin

# Register your models here.

from catalog.models import Author, Genre, Language, Book, BookInstance

# We have commented out the ones that are overwritten using admin functions.
#admin.site.register(Book)
admin.site.register(Language)
#admin.site.register(BookInstance)
admin.site.register(Genre)
#admin.site.register(Author)
# Define the admin class

class AuthorAdmin(admin.ModelAdmin):
    list_display=('last_name','first_name','date_of_birth','date_of_death')

# Register the admin class with the associated model
admin.site.register(Author, AuthorAdmin)

# Register the Admin classes for Book using the decorator
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display=('title','author','display_genre')

# Register the Admin classes for BookInstace using the decorator
@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_display=('book','status','due_back','id')
