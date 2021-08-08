from django.contrib import admin
from django.db import models
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms

from .models import Services, ServicesImage, Procedures, Specialist, Special, SpecialImage, Departments
# Register your models here.

class ServicesAdminForm(forms.ModelForm):
    testimony = forms.CharField(label='Показания', widget=CKEditorUploadingWidget())
    contraindications = forms.CharField(label='Противопоказания', widget=CKEditorUploadingWidget())
    class Meta:
        model = Services
        fields = '__all__'



class ServicesImageAdmin(admin.TabularInline):
   
    model = ServicesImage
    extra = 0
    min_num = 0


class SpecialistAdmin(admin.TabularInline):
    model = Specialist
    extra = 0
    min_num = 0
    max_num = 1


class SpecialistAdminReader(admin.ModelAdmin):
    list_display = ('title', 'services')

admin.site.register(Specialist, SpecialistAdminReader)


class ServicesAdmin(admin.ModelAdmin):
    form = ServicesAdminForm
    list_display = ('title', 'id')
    prepopulated_fields = {'slug': ('title',)}
    save_as = True
    save_on_top = True
    inlines = [
        ServicesImageAdmin, 
        SpecialistAdmin,

    ]


admin.site.register(Services, ServicesAdmin)



class DepartmentsAdmin(admin.ModelAdmin):
    pass


admin.site.register(Departments, DepartmentsAdmin)



class ProceduresAdmin(admin.ModelAdmin):
    list_display = ('title', 'time', 'sessions', 'price', 'services')
    save_as = True
    save_on_top = True
    


admin.site.register(Procedures, ProceduresAdmin)









class SpecialImageAdmin(admin.TabularInline):
   
    model = SpecialImage
    extra = 0
    min_num = 0





class SpecialAdmin(admin.ModelAdmin):
 
    list_display = ('title', )
    save_as = True
    save_on_top = True
    prepopulated_fields = {'slug': ('title',)}
    inlines = [
        SpecialImageAdmin, 
        

    ]


admin.site.register(Special, SpecialAdmin)