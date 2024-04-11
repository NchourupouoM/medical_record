from django.contrib import admin
from authentication.models import User

# Register your models here.


class userAdmin(admin.ModelAdmin):
    list_display = ('id','first_name','last_name','role','date_naissance','sex','telephone')


admin.site.register(User,userAdmin)