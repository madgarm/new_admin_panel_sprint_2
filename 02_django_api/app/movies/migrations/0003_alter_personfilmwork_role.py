# Generated by Django 3.2 on 2022-07-05 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_alter_default_datetime_fileds'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personfilmwork',
            name='role',
            field=models.TextField(
                choices=[('actor', 'Актёр'), ('writer', 'Писатель'), ('director', 'Директор')], verbose_name='role'
            ),
        ),
    ]