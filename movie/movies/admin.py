from django.contrib import admin
from movies.models import Film, Actor

# Register your models here.
admin.site.register(Film)
admin.site.register(Actor)