from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from import_export.admin import ImportExportModelAdmin, ExportMixin
from import_export import resources

# Register your models here.


# para CKEDITOR

from django import forms
from ckeditor.widgets import CKEditorWidget


# Register your models here.


from mainApp.models import Proposito, Vinculacion, Oracion, Marcacion,UserPerfil
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
    


class UserResource(resources.ModelResource):
    #fields = ('username', 'first_name', 'last_login')
    #inlines = (UserPerfilAdmin, )
    #list_display = ( "username", "first_name", "last_login")

    class Meta:
        model = User
        export_order = ('username', 'first_name', 'last_name', 'email', 'date_joined','last_login')


class UserAdmin(ExportMixin, UserAdmin ):
    resource_class = UserResource
    pass



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
