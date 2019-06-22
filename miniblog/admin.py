from django.contrib import admin
from miniblog.models import Blog, BlogInstance, Blogger, BlogComment

# Register models

admin.site.register(Blog)
admin.site.register(BlogInstance)
admin.site.register(Blogger)
admin.site.register(BlogComment)