from django.db import models
from django.utils.html import format_html

#catagory
class Category(models.Model):
    cat_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    description  = models.CharField(max_length=100)
    url  = models.CharField(max_length=100)
    image = models.ImageField(upload_to='media/')
    add_date = models.DateTimeField(auto_now_add=True , null=True)
    
    def image_tag(self):
     if self.image:
        return format_html(
            '<img src="{}" style="width:40px;height:40px;" />',
            self.image.url
        )
     return "No Image"

#Post
class Post(models.Model):
    post_id   = models.AutoField(primary_key = True)
    tittle = models.CharField(max_length= 200)
    content = models.TextField()
    url  = models.CharField(max_length=100)
    cat = models.ForeignKey(Category , on_delete = models.CASCADE)
    Image = models.ImageField(upload_to  = 'post/')