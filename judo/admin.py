from django.contrib import admin
#from langex.models import User
from django.contrib.auth.models import User
from judo.models import UserProfile,Item, FAQ



class UserAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('user',)}
    #list_display = ('username', 'email', 'age')
class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'picture')

admin.site.register(UserProfile,UserAdmin)
admin.site.register(Item, ItemAdmin)
admin.site.register(FAQ)
