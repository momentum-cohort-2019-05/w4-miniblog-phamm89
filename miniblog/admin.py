from django.contrib import admin
from miniblog.models import Blog, Blogger, BlogReader, BlogComment

# Register models

# Register BlogComment as an inline to the Blog
class BlogCommentInline(admin.TabularInline):
    model = BlogComment

# Register the Admin classes for Blog using the decorator
@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('blog_title', 'blogger', 'blog_entry_date')
    fields = ['blog_title', 'blogger', 'blog_entry_date', 'blog_entry']
    inlines = [BlogCommentInline]

# Register the Admin class for Blogger
class BloggerAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'bio')
    fields = ['first_name', 'last_name', 'bio']
    
# Register the admin class with the associated model
admin.site.register(Blogger, BloggerAdmin)

# Register the Admin class for BlogReader 
class BlogReaderAdmin(admin.ModelAdmin):
    list_display = ('user_name', 'profile_description')
    fields = ['user_name', 'profile_description']
# Register the admin class with the associated model
admin.site.register(BlogReader, BlogReaderAdmin)

# Register the Admin class for BlogComment
class BlogCommentAdmin(admin.ModelAdmin):
    list_display = ('blog_entry', 'user_name', 'comment', 'comment_date')
    fields = ['blog_entry', 'user_name', 'comment', 'comment_date']
admin.site.register(BlogComment, BlogCommentAdmin)