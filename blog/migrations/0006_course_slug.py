# Generated by Django 3.2.9 on 2021-12-03 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='slug',
            field=models.SlugField(blank=True, null=True, unique=True),
        ),
    ]