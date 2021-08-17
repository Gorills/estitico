# Generated by Django 3.2.4 on 2021-08-08 07:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('estetico', '0002_remove_special_specialist'),
    ]

    operations = [
        migrations.AddField(
            model_name='special',
            name='spec',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='special', to='estetico.specialist'),
        ),
    ]