from django.contrib import admin
from miniblog.models import Blog, BlogInstance, Blogger, BlogComment

# Register models

# admin.site.register(Blog)
# Register the Admin classes for Blog using the decorator
@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    pass

# admin.site.register(BlogInstance)
# Register the Admin classes for BookInstance using the decorator
@admin.register(BlogInstance) 
class BlogInstanceAdmin(admin.ModelAdmin):
    pass

# Define the admin class
# admin.site.register(Blogger)
class BloggerAdmin(admin.ModelAdmin):
    pass
# Register the admin class with the associated model
admin.site.register(Blogger, BloggerAdmin)

admin.site.register(BlogComment)