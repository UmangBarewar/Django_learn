from django.contrib import admin
from .models import Fav_Anime,Stream,Anime_Review,Censor_Certificate

class Review_inline(admin.TabularInline):
    model = Anime_Review

class Fav_AnimeAdmin(admin.ModelAdmin):
    # this is done and seen mostly while modifying the admin
    list_display=('name','genre')
    inlines=[Review_inline]

class StreamAdmin(admin.ModelAdmin):
    list_display=('name','origin')
    filter_horizontal=('anime',)

class CertificateAdmin(admin.ModelAdmin):
    list_display=('issue_date','certificate_no')
# Register your models here.
admin.site.register(Fav_Anime,Fav_AnimeAdmin)
admin.site.register(Stream,StreamAdmin)
admin.site.register(Censor_Certificate,CertificateAdmin)
