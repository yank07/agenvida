from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# Register your models here.

# Register your models here.


from mainApp.models import *
from django.contrib.auth.models import User


class PropositoAdmin(admin.ModelAdmin):
    #fields = ('vinculacion', 'proposito', 'mes_ano', 'usuario')
    list_display = [ "proposito", "mes_ano"]






class UserPerfilAdmin(admin.StackedInline):
	model = UserPerfil
	can_delete = False
	fields = ('nacimiento', 'pais')
	verbose_name_plural='Perfiles'


class UsersAdmin(UserAdmin):
    #fields = ('vinculacion', 'proposito', 'mes_ano', 'usuario')
    #list_display = [ "username", "first_name", "last_login"]
    inlines = (UserPerfilAdmin, )




    

class VinculacionAdmin(admin.ModelAdmin):
    fields = ('vinculacion')



admin.site.register(Vinculacion)



admin.site.register(UserPerfil)

admin.site.register(Proposito, PropositoAdmin)
admin.site.unregister(User)
admin.site.register(User, UsersAdmin )
admin.site.register(Marcacion)




