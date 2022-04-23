from django.contrib import admin

from .models import Category,Movie,Genre,MovieShots,Actor, Rating,RatingStar,Reviews

admin.site.register(Category)
admin.site.register(Movie)
admin.site.register(Genre)
admin.site.register(MovieShots)
admin.site.register(Rating)
admin.site.register(Actor)
admin.site.register(Reviews)
admin.site.register(RatingStar)
