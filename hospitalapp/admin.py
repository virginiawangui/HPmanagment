from django.contrib import admin
from hospitalapp.models import users,product,member,message

# Register your models here.
admin.site.register(users)
admin.site.register(product)
admin.site.register(member)
admin.site.register(message)