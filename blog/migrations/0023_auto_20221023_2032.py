# Generated by Django 3.2.15 on 2022-10-23 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0022_alter_post_title_background'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='show_title_below_header',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='post',
            name='show_title_in_header',
            field=models.BooleanField(default=True),
        ),
    ]