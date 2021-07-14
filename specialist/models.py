from django.db import models
from django.urls import reverse

# Create your models here.


class Specialist(models.Model):
    name = models.CharField(max_length=100, verbose_name='ФИО')
    photo = models.ImageField(upload_to='images/specialist', verbose_name='Фотография', null=True)
    specialty = models.CharField(max_length=150, verbose_name='Специальность')
    profile = models.TextField(verbose_name='Профайл')

    slug = models.SlugField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("specialist_detail", kwargs={"slug": self.slug})
    

    class Meta:
        verbose_name = 'Специалист'
        verbose_name_plural = 'Специалисты'