from django.db import models
from django.urls import reverse

# Create your models here.

class Post(models.Model):
    title = models.CharField(verbose_name='Заголовок', max_length=200)
    text = models.TextField(verbose_name='Текст поста')
    image = models.ImageField(upload_to='images/blog', verbose_name='Изображение')
    slug = models.SlugField()
    date = models.DateField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("blog_detail", kwargs={"slug": self.slug})
    

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'