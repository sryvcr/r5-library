# Generated by Django 4.2.3 on 2024-01-03 03:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library_admin', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.ManyToManyField(related_name='authors', to='library_admin.author'),
        ),
        migrations.AlterField(
            model_name='book',
            name='category',
            field=models.ManyToManyField(related_name='categories', to='library_admin.category'),
        ),
    ]
