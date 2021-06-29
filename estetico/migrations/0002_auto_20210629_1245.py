# Generated by Django 3.2.4 on 2021-06-29 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estetico', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='procedures',
            options={'verbose_name': 'Процедура', 'verbose_name_plural': 'Процедуры'},
        ),
        migrations.AlterModelOptions(
            name='servicesimage',
            options={'verbose_name': 'Изображение', 'verbose_name_plural': 'Изображения'},
        ),
        migrations.AlterModelOptions(
            name='specialimage',
            options={'verbose_name': 'Изображение', 'verbose_name_plural': 'Изображения'},
        ),
        migrations.AlterModelOptions(
            name='specialist',
            options={'verbose_name': 'Мнение специалиста', 'verbose_name_plural': 'Мнение специалиста'},
        ),
        migrations.AddField(
            model_name='special',
            name='procent',
            field=models.BooleanField(default=False, null=True, verbose_name='Скидка в процентах'),
        ),
        migrations.AlterField(
            model_name='departments',
            name='address',
            field=models.CharField(max_length=300, verbose_name='Адрес'),
        ),
        migrations.AlterField(
            model_name='departments',
            name='metro',
            field=models.CharField(max_length=300, verbose_name='Метро рядом'),
        ),
        migrations.AlterField(
            model_name='departments',
            name='time',
            field=models.CharField(max_length=300, verbose_name='Время работы'),
        ),
        migrations.AlterField(
            model_name='servicesimage',
            name='photo',
            field=models.ImageField(upload_to='images/services', verbose_name='Изображение'),
        ),
        migrations.AlterField(
            model_name='specialimage',
            name='photo',
            field=models.ImageField(upload_to='images/special', verbose_name='Изображение'),
        ),
    ]
