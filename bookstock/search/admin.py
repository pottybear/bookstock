from django.contrib import admin
from search.models import Author, Publisher, Book, Url

admin.site.register(Author)
admin.site.register(Publisher)
admin.site.register(Book)
admin.site.register(Url)
