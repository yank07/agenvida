from django.contrib import admin

# Register your models here.

# Register your models here.


from mainApp.models import *
from django.contrib.auth.models import User


class PropositoAdmin(admin.ModelAdmin):
    #fields = ('vinculacion', 'proposito', 'mes_ano', 'usuario')
    list_display = [ "proposito", "mes_ano"]


class UsersAdmin(admin.ModelAdmin):
    #fields = ('vinculacion', 'proposito', 'mes_ano', 'usuario')
    list_display = [ "username", "first_name", "last_login"]
    

class VinculacionAdmin(admin.ModelAdmin):
    fields = ('vinculacion')

admin.site.register(Vinculacion)
admin.site.register(Proposito, PropositoAdmin)
admin.site.unregister(User)
admin.site.register(User, UsersAdmin )
admin.site.register(Marcacion)

admin.site.register(PropositoParticular)


