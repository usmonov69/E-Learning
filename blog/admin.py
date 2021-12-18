from django.contrib import admin

from .models import *

admin.site.register(Post)
admin.site.register(Course)
admin.site.register(Comment)  
admin.site.register(Contact)
admin.site.register(CategoryPost)
admin.site.register(CategoryCourse)

