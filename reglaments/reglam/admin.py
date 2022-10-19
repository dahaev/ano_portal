from django.contrib import admin
from .models import *


class TypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'reg_type')
    search_fields = ('reg_type',)
    prepopulated_fields = {'reg_slug': ('reg_type',)}


class ReglamentAdmin(admin.ModelAdmin):
    list_display = ('id', 'reg_name', 'reg_status', 'reg_dep', 'reg_type')
    search_fields = ('reg_name', 'reg_status')
    prepopulated_fields = {'slug': ('reg_name',)}
    list_display_links = ('id', 'reg_name')


class ReglamentDepartmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'reg_dep')
    search_fields = ('id', 'reg_dep')
    prepopulated_fields = {'reg_slug': ('reg_dep',)}


class ReglamentDepartmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'reg_dep')
    search_fields = ('id', 'reg_dep')
    prepopulated_fields = {'reg_slug': ('reg_dep',)}

class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('id', 'name')
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(ReglamentsType, TypeAdmin)
admin.site.register(Reglaments, ReglamentAdmin)
admin.site.register(ReglamentsDepartment, ReglamentDepartmentAdmin)
admin.site.register(News, NewsAdmin)
