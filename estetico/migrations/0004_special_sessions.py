# Generated by Django 3.2.4 on 2021-06-29 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estetico', '0003_special_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='special',
            name='sessions',
            field=models.CharField(max_length=150, null=True, verbose_name='Количество сеансов / процент скидки'),
        ),
    ]