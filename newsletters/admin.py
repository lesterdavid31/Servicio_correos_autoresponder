from django.contrib import admin
from .models import NewsLettersUser, NewsLetter
# Register your models here.

admin.site.register(NewsLettersUser)
admin.site.register(NewsLetter)

