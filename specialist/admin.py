from django.contrib import admin
from django.contrib.admin.sites import site
from .models import Specialist
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget

class SpecialistForm(forms.ModelForm):
    profile = forms.CharField(label='Профайл', widget=CKEditorUploadingWidget())
    class Meta:
        model = Specialist
        fields = '__all__'

class SpecialistAdmin(admin.ModelAdmin):
    form = SpecialistForm
    prepopulated_fields = {'slug': ('name', 'specialty')}
    save_as = True
    save_on_top = True
    list_display = ('name', 'specialty')
    

admin.site.register(Specialist, SpecialistAdmin)