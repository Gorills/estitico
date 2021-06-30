from django.contrib import admin
from django.db import models
from django import forms
from .models import Post
from ckeditor_uploader.widgets import CKEditorUploadingWidget
# Register your models here.


class PostAdminForm(forms.ModelForm):
    
    text = forms.CharField(label='Пост', widget=CKEditorUploadingWidget())
    class Meta:
        model = Post
        fields = '__all__'

class PostAdmin(admin.ModelAdmin):
    form = PostAdminForm
    list_display = ('title', 'date')
    prepopulated_fields = {'slug': ('title',)}
    save_on_top = True
    save_as = True



admin.site.register(Post, PostAdmin)