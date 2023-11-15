from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from app.models import Book, Publisher, User

admin.site.register(Book)
admin.site.register(Publisher)
admin.site.register(User, UserAdmin)
