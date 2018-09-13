from django.contrib import admin

# Register your models here

from .models import Song, List, Song_in_List, Played_Song, Distance_to_List, Distance_to_User, Distance

admin.site.register(Song)
admin.site.register(List)
admin.site.register(Song_in_List)
admin.site.register(Played_Song)
admin.site.register(Distance)
admin.site.register(Distance_to_User)
admin.site.register(Distance_to_List)



