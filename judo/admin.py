from django.contrib import admin
#from langex.models import User
from django.contrib.auth.models import User
from judo.models import UserProfile,Item, FAQ, Price



class UserAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('user',)}
    #list_display = ('username', 'email', 'age')
class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'itemPrice', 'picture')

class PriceAdmin(admin.ModelAdmin):
    list_display = ('item', 'id', 'price')

admin.site.register(UserProfile,UserAdmin)
admin.site.register(Item, ItemAdmin)
admin.site.register(FAQ)
admin.site.register(Price, PriceAdmin)
