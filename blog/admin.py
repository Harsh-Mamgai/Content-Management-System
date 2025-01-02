from django.contrib import admin
from blog.models import Blog, Comment

# Register your models here.

#This is the way to add custom js and css file in static folder to our models only in django admin. 
class BlogAdmin(admin.ModelAdmin):
    class Media:
        css = {
            "all" : ("css/style.css",)
        }

        js = ("js/sc.js",)

admin.site.register(Blog,BlogAdmin)#we registered our model in django admin
admin.site.register(Comment)

