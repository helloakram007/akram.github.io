from django.contrib import admin
from .models import Contact,Blog,Portfolio,Files

# Register your models here.
admin.site.register(Contact)
admin.site.register(Portfolio)
admin.site.register(Files)
@admin.register(Blog)

class BlogAdmin(admin.ModelAdmin):
    class Media:
        js= ('tinyInject.js',)