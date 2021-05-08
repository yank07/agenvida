from django.contrib import admin

# Register your models here.

from django.contrib.auth.admin import UserAdmin
from .models import Proposito, Vinculacion, Oracion, Marcacion,UserPerfil
from django.contrib.auth.models import User




class UserPerfilAdmin(admin.StackedInline):
	model = UserPerfil
	can_delete = False
	fields = ('nacimiento', 'pais')
	verbose_name_plural='Perfiles'


class UsersAdmin(UserAdmin):
    #fields = ('vinculacion', 'proposito', 'mes_ano', 'usuario')
    #list_display = [ "username", "first_name", "last_login"]
    inlines = (UserPerfilAdmin, )
    




class OracionAdmin(admin.ModelAdmin):
     list_display = [ "nombre", "contenido"]



UserAdmin.list_display += ('last_login','date_joined',)  # don't forget the commas

admin.site.register(Vinculacion)
admin.site.register(Proposito)
admin.site.register(Marcacion)
admin.site.register(Oracion)
admin.site.register(UserPerfil)
admin.site.unregister(User)
admin.site.register(User, UserAdmin)

