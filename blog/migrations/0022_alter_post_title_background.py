# Generated by Django 3.2.15 on 2022-10-23 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0021_auto_20221023_2025'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='title_background',
            field=models.CharField(choices=[('no', 'none'), ('gr', 'grey'), ('bl', 'black'), ('wh', 'white'), ('wt', 'white-transparent')], default='no', max_length=2),
        ),
    ]
