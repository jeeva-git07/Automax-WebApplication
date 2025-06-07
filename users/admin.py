from django.contrib import admin
from .models import Profile,Location

class ProfilAdmin(admin.ModelAdmin):
    pass

class LocationAdmin(admin.ModelAdmin):
    pass

admin.site.register(Profile,ProfilAdmin)
admin.site.register(Location,LocationAdmin)