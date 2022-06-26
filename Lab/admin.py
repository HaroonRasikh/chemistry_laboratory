from typing import Tuple

from django.contrib import admin
from .models import Material
from .models import Experiment
from .forms import *
#from django.contrib.auth.admin import UserAdmin
#from django.contrib.auth.models import Group,User # Groupu listeden kaldırmak için
#from django.utils.html import format_html
#from django.contrib.auth import User
# Register your models here.
#admin.site.unregister(Group) # ve burada Groupu kaldırabiliyoruz
#admin.site.unregister(User)
#from django.contrib.admin.utils import flatten_fieldsets

class InvoiceAdmin(admin.ModelAdmin):
   list_display = ['adi','miktar','Materialtype','kati','sivi','deger']
   form = MalzemeForm  # burada form kullammamiziz sebebi ise fieldlerini sayisini azaltabiliriz forms.py dan 
   #list_filter = ['name']
   #search_fields = ['name', 'invoice_number']
admin.site.register(Material, InvoiceAdmin)











# class BaseReadOnlyAdminMixin:
#     def has_add_permission(self, request):
#         if request.user.is_staff:
#             if request.user.is_superuser:
#                 return []
#             else:
#                 return [f.name for f in self.model._meta.fields]

#     def has_change_permission(self, request, obj=None):
#         def has_add_permission(self, request):
#             if request.user.is_staff:
#                 if request.user.is_superuser:
#                     return []
#                 else:
#                     return [f.name for f in self.model._meta.fields]

#     def has_delete_permission(self, request, obj=None):
#         def has_add_permission(self, request):
#             if request.user.is_staff:
#                 if request.user.is_superuser:
#                     return []
#                 else:
#                     return [f.name for f in self.model._meta.fields]










# class typeFun(admin.ModelAdmin):
# 	search_fields = type.SearchFields
# 	list_display = type.DisplayFields
# 	#exclude = ('is_deleted',)
# admin.site.register(type,typeFun)

# class MaterialAdmin(admin.ModelAdmin):
# 	search_fields = Material.searchfields
# 	list_display = Material.listdisplay
# 	#list_editable = Material.listeditable
# 	list_filter = Material.listfilter
	#readonly_fields = ['adi','miktar','malzemetürü','özgünlük']

# def get_readonly_fields(self, request, obj=None):
#     if request.user.is_staff:
#         if request.user.is_superuser:
#             return []
#         else:
#             return [f.name for f in self.model._meta.fields]











# 	def get_readonly_fields(self, request, obj=None):
#         if request.user.is_superuser:
#             return []
#         return self.readonly_fields
#admin.site.register(Material,MaterialAdmin)

@admin.register(Experiment)
class ExperimentAdmin(admin.ModelAdmin):
	list_display = Experiment.DisplayFields
	search_fields = Experiment.SearchFields
   # list_display  = ('adi', 'Malzemeler', 'description','is_verified')
    #readonly_fields = [field.name for field in ClassName._meta.fields]
#	search_fields = ('adi',)
