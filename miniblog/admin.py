from django.contrib import admin
from miniblog.models import Blog, BlogInstance, Blogger, BlogReader, BlogComment

# Register models

# admin.site.register(Blog)
# Register the Admin classes for Blog using the decorator
@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    pass

# admin.site.register(BlogInstance)
# Register the Admin classes for BlogInstance using the decorator
@admin.register(BlogInstance) 
class BlogInstanceAdmin(admin.ModelAdmin):
    list_display = ('blog', 'blog_title', 'blogger', 'blog_entry_date')

# Register the Admin class for Blogger
# admin.site.register(Blogger)
class BloggerAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'bio')
# Register the admin class with the associated model
admin.site.register(Blogger, BloggerAdmin)

# Register the Admin class for BlogReader 
class BlogReaderAdmin(admin.ModelAdmin):
    list_display = ('user_name', 'profile_description')
# Register the admin class with the associated model
admin.site.register(BlogReader, BlogReaderAdmin)

# Register the Admin class for BlogComment
class BlogCommentAdmin(admin.ModelAdmin):
    list_display = ('user_name', 'blog_entry', 'comment_date')
admin.site.register(BlogComment)