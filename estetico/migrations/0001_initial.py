# Generated by Django 3.2.4 on 2021-08-08 06:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Procedures',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=350, verbose_name='Название')),
                ('time', models.CharField(max_length=150, verbose_name='Время сеанса')),
                ('sessions', models.CharField(max_length=250, verbose_name='Количество сеансов')),
                ('price', models.CharField(max_length=200, verbose_name='Цена')),
            ],
            options={
                'verbose_name': 'Процедура',
                'verbose_name_plural': 'Процедуры',
            },
        ),
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=350, verbose_name='Название')),
                ('description', models.TextField(verbose_name='Описание')),
                ('slug', models.SlugField(verbose_name='URL')),
                ('testimony', models.TextField(verbose_name='Показания')),
                ('contraindications', models.TextField(verbose_name='Противопоказания')),
                ('meta_title', models.CharField(blank=True, max_length=350, null=True, verbose_name='Мета заголовок')),
                ('meta_description', models.CharField(blank=True, max_length=500, null=True, verbose_name='Мета описание')),
                ('meta_keywords', models.CharField(blank=True, max_length=500, null=True, verbose_name='Ключевые слова')),
            ],
            options={
                'verbose_name': 'Услуга',
                'verbose_name_plural': 'Услуги',
            },
        ),
        migrations.CreateModel(
            name='Special',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=350, verbose_name='Название')),
                ('slug', models.SlugField(verbose_name='URL')),
                ('price', models.CharField(blank=True, max_length=200, null=True, verbose_name='Цена со скидкой')),
                ('sessions', models.CharField(max_length=150, null=True, verbose_name='Количество сеансов / процент скидки')),
                ('text', models.CharField(max_length=250, null=True, verbose_name='Текст под скидкой')),
                ('procent', models.BooleanField(default=False, null=True, verbose_name='Скидка в процентах')),
                ('meta_title', models.CharField(blank=True, max_length=350, null=True, verbose_name='Мета заголовок')),
                ('meta_description', models.CharField(blank=True, max_length=500, null=True, verbose_name='Мета описание')),
                ('meta_keywords', models.CharField(blank=True, max_length=500, null=True, verbose_name='Ключевые слова')),
                ('procedure', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='specials_procedure', to='estetico.procedures', verbose_name='Процедура')),
                ('services', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='specials', to='estetico.services', verbose_name='Услуга')),
            ],
            options={
                'verbose_name': 'Специальное предложение',
                'verbose_name_plural': 'Специальные предложения',
            },
        ),
        migrations.CreateModel(
            name='Specialist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=700, verbose_name='Заголовок')),
                ('text', models.TextField(verbose_name='Текст')),
                ('services', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='specialists', to='estetico.services', verbose_name='Услуга')),
            ],
            options={
                'verbose_name': 'Мнение специалиста',
                'verbose_name_plural': 'Мнение специалиста',
            },
        ),
        migrations.CreateModel(
            name='SpecialImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='images/special', verbose_name='Изображение')),
                ('special', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='estetico.special', verbose_name='Акция')),
            ],
            options={
                'verbose_name': 'Изображение',
                'verbose_name_plural': 'Изображения',
            },
        ),
        migrations.AddField(
            model_name='special',
            name='specialist',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='specials_specialist', to='estetico.specialist', verbose_name='Мнение специалиста'),
        ),
        migrations.CreateModel(
            name='ServicesImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='images/services', verbose_name='Изображение')),
                ('services', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='estetico.services', verbose_name='Услуга')),
            ],
            options={
                'verbose_name': 'Изображение',
                'verbose_name_plural': 'Изображения',
            },
        ),
        migrations.AddField(
            model_name='procedures',
            name='services',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='procedures', to='estetico.services', verbose_name='Услуга'),
        ),
        migrations.CreateModel(
            name='Departments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=350, verbose_name='Название')),
                ('time', models.CharField(max_length=300, verbose_name='Время работы')),
                ('address', models.CharField(max_length=300, verbose_name='Адрес')),
                ('metro', models.CharField(max_length=300, verbose_name='Метро рядом')),
                ('photo', models.ImageField(upload_to='images/departaments')),
                ('map', models.TextField(null=True, verbose_name='Код карты')),
                ('services', models.ManyToManyField(related_name='departaments', to='estetico.Services', verbose_name='Услуги')),
            ],
            options={
                'verbose_name': 'Филиал',
                'verbose_name_plural': 'Филиалы',
            },
        ),
    ]
