# Generated by Django 3.2.4 on 2021-06-29 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estetico', '0002_auto_20210629_1245'),
    ]

    operations = [
        migrations.AddField(
            model_name='special',
            name='text',
            field=models.CharField(max_length=250, null=True, verbose_name=''),
        ),
    ]
