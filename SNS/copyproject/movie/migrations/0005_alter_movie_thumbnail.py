# Generated by Django 4.2.7 on 2024-01-19 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0004_movie_thumbnail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='thumbnail',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
