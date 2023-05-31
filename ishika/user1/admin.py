from django.contrib import admin
from user1.models import *
class UserAdmin(admin.ModelAdmin) :
    list_display=('user_name',
    'user_email',
    'user_contact',
    'user_password',
    'user_city',
    'user_state',
    'user_pincode')
    list_filter=['user_city']
    search_fields=['user_name']
admin.site.register(user1,UserAdmin)





class CategoryRegister(admin.ModelAdmin):
    list_display=['categoryname','img']
    list_filter=['categoryname']
admin.site.register(Category,CategoryRegister)

class productregister(admin.ModelAdmin):
    list_display=['name','price','description']
    list_filter=['name']

admin.site.register(Product,productregister)


