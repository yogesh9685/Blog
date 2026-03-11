from django.contrib import admin
from .models import Category , Post
from django.contrib.admin import ModelAdmin
@admin.register(Category)
class CategoryAdmin(ModelAdmin):
      list_display = ( 'title' , 'url' , 'description' , 'image_tag')
      search_fields = ('tittle' ,)


class PostAdmin(ModelAdmin):
      list_display = ( 'tittle', 'content')
      search_fields = ('title',)
      list_filter = ('cat',)
admin.site.register(Post , PostAdmin)