from django.contrib import admin
from .models import *
# Register your models here.

class TradeAdmin(admin.ModelAdmin):

    pass

admin.site.register(Trade, TradeAdmin)

class AuthorAdmin(admin.ModelAdmin):
    pass

admin.site.register(Author, AuthorAdmin)

class CategoryAdmin(admin.ModelAdmin):
    pass

admin.site.register(Category, CategoryAdmin)

class PostAdmin(admin.ModelAdmin):
    pass
admin.site.register(Post, admin.ModelAdmin)