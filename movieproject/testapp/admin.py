from django.contrib import admin
from testapp.models import  movie
class MovieAdmin(admin.ModelAdmin):
      list_display = ['rdate','moviename','hero','heroine','rating']

admin.site.register(movie,MovieAdmin)