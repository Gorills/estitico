from django.db import models
from django.urls import reverse
# Create your models here.

class Services(models.Model):
    title = models.CharField(max_length=350, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    slug = models.SlugField(verbose_name='URL')
    testimony = models.TextField(verbose_name='Показания')
    contraindications = models.TextField(verbose_name='Противопоказания')
    meta_title = models.CharField(max_length=350, verbose_name='Мета заголовок', blank=True, null=True)
    meta_description = models.CharField(max_length=500, verbose_name='Мета описание', blank=True, null=True)
    meta_keywords = models.CharField(max_length=500, verbose_name='Ключевые слова', blank=True, null=True)


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('services_detail', kwargs={'slug': self.slug})
    
    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'


class ServicesImage(models.Model):
    services = models.ForeignKey(Services, related_name='images', verbose_name='Услуга', on_delete=models.CASCADE)
    photo = models.ImageField(verbose_name='Изображение', upload_to = 'images/services')
    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'


class Specialist(models.Model):
    title = models.CharField(max_length=700, verbose_name='Заголовок')
    text = models.TextField(verbose_name='Текст')
    services = models.ForeignKey(Services, related_name='specialists', verbose_name='Услуга', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Мнение специалиста'
        verbose_name_plural = 'Мнение специалиста'


class Procedures(models.Model):
    services = models.ForeignKey(Services, related_name='procedures', verbose_name='Услуга', on_delete=models.CASCADE)
    title = models.CharField(max_length=350, verbose_name='Название')
    time = models.CharField(max_length=150, verbose_name='Время сеанса')
    sessions = models.CharField(max_length=250, verbose_name='Количество сеансов')
    price = models.CharField(max_length=200 ,verbose_name='Цена')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Процедура'
        verbose_name_plural = 'Процедуры'

class Special(models.Model):

    title = models.CharField(max_length=350, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    slug = models.SlugField(verbose_name='URL')
    testimony = models.TextField(verbose_name='Показания')
    contraindications = models.TextField(verbose_name='Противопоказания')
    services = models.ForeignKey(Services, related_name='specials', verbose_name='Услуга', on_delete=models.CASCADE)
    procedure = models.ForeignKey(Procedures, related_name='specials_procedure', verbose_name='Процедура', on_delete=models.PROTECT)
    specialist = models.ForeignKey(Specialist, related_name='specials_specialist', verbose_name='Мнение специалиста', on_delete=models.PROTECT)
    price = models.CharField(max_length=200, verbose_name='Цена со скидкой', null=True, blank=True )
    sessions = models.CharField(max_length=150, verbose_name='Количество сеансов / процент скидки', null=True)
    meta_title = models.CharField(max_length=350, verbose_name='Мета заголовок', blank=True, null=True)
    meta_description = models.CharField(max_length=500, verbose_name='Мета описание', blank=True, null=True)
    meta_keywords = models.CharField(max_length=500, verbose_name='Ключевые слова', blank=True, null=True)
    text = models.CharField(max_length=250, verbose_name='Текст под скидкой', null=True)
    procent = models.BooleanField(null=True, default=False, verbose_name='Скидка в процентах')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('special_detail', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = 'Специальное предложение'
        verbose_name_plural = 'Специальные предложения'





class SpecialImage(models.Model):
    special = models.ForeignKey(Special, related_name='images', verbose_name='Акция', on_delete=models.CASCADE)
    photo = models.ImageField(verbose_name='Изображение', upload_to = 'images/special')
    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'


class Departments(models.Model):
    title = models.CharField(max_length=350, verbose_name='Название')
    time = models.CharField(max_length=300, verbose_name='Время работы')
    address = models.CharField(max_length=300, verbose_name='Адрес')
    metro = models.CharField(max_length=300, verbose_name='Метро рядом')
    photo = models.ImageField(upload_to='images/departaments')
    services = models.ManyToManyField(Services, verbose_name='Услуги', related_name='departaments')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Филиал'
        verbose_name_plural = 'Филиалы'