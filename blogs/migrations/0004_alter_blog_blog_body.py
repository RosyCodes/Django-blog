# Generated by Django 4.2.13 on 2024-06-10 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0003_alter_blog_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='blog_body',
            field=models.TextField(max_length=3000),
        ),
    ]
