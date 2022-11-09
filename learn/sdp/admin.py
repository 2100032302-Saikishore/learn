from django.contrib import admin

# Register your models here.
from .models import cat,movie,music,marriage
admin.site.register(cat)
admin.site.register(movie)
admin.site.register(music)
admin.site.register(marriage)
# admin.site.register(Musicalconcertm)
# admin.site.register(weddinghalls)