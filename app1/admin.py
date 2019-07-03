from django.contrib import admin
from .models import Fuck1

class AdminModify(admin.ModelAdmin):
    list_display = ('title', 'author', 'publish')
    list_filter = ('publish', 'author')
    search_fields = ('title', 'body')
    raw_id_fields = ('author',)
    date_hierarchy = 'publish'
    ordering = ['-publish', 'author']


admin.site.register(Fuck1, AdminModify)



# Register your models here.
