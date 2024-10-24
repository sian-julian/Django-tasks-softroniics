from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(user)
admin.site.register(Book)
admin.site.register(Employee)
admin.site.register(Product)

class customeradmin(admin.ModelAdmin):
    list_display = ('first_name','last_name','address','id',)
    search_fields =('first_name',)
    list_filter =('id',)
admin.site.register(Customer,customeradmin)
admin.site.site_header='MY_SITE'
admin.site.site_title='django site'

class blogadmin(admin.ModelAdmin):
    list_display=('title','content','author',)
    search_fields=('title',)
    list_filter=('id',)
admin.site.register(Blog,blogadmin)
admin.site.register(productmodel)

admin.site.register(category)
admin.site.register(employ)

admin.site.register(Publisher)
class Bookadmin(admin.ModelAdmin):
    list_display=('title','isbn','publisher',)
    search_fields=('title','isbn',)
    list_filter=('pub_date',)
admin.site.register(Bookm,Bookadmin)

admin.site.register(Course)
class Studentadmin(admin.ModelAdmin):
    list_display=('first_name','last_name','course',)
    search_fields=('first_name','last_name',)
    list_filter=('course')
admin.site.register(Student)

admin.site.register(Organizer)
admin.site.register(Event)




