# Generated by Django 3.2.15 on 2022-10-03 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20221003_1316'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='language',
            field=models.ManyToManyField(blank=True, to='blog.Language'),
        ),
    ]
