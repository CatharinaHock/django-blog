# Generated by Django 3.2.15 on 2022-10-13 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_alter_post_language'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='language',
            field=models.ManyToManyField(blank=True, to='blog.Language'),
        ),
    ]
