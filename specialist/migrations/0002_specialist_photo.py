# Generated by Django 3.2.4 on 2021-07-13 05:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('specialist', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='specialist',
            name='photo',
            field=models.ImageField(null=True, upload_to='images/specialist', verbose_name='Фотография'),
        ),
    ]
