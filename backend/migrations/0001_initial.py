# Generated by Django 5.0.4 on 2024-05-16 20:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500, verbose_name='Заголовок')),
                ('content', models.TextField(verbose_name='Текст')),
                ('time_created', models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')),
            ],
            options={
                'verbose_name': 'Новость',
                'verbose_name_plural': 'Новости',
                'ordering': ['-time_created'],
                'indexes': [models.Index(fields=['-time_created'], name='backend_new_time_cr_e1f8a1_idx')],
            },
        ),
    ]
