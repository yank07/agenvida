from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from import_export.admin import ImportExportModelAdmin, ExportMixin
from import_export import resources
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

UserAdmin.list_display += ('last_login','date_joined',)  # don't forget the commas


admin.site.register(Vinculacion)



admin.site.register(UserPerfil)

admin.site.register(Proposito, PropositoAdmin)
admin.site.unregister(User)
admin.site.register(User, UsersAdmin )
admin.site.register(Marcacion)

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


admin.site.unregister(User)
admin.site.register(User, UserAdmin)



