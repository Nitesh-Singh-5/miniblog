from django.contrib import admin
from .models import Post,Profile
# Register your models here.
@admin.register(Post)
class PostModelAdmin(admin.ModelAdmin):
    list_display=['id','title','description']


from .models import contact

@admin.register(contact)
class UserAdmin(admin.ModelAdmin):
    list_display=('id','name','email','message')

admin.site.register(Profile)