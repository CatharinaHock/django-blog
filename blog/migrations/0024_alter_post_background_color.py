# Generated by Django 3.2.15 on 2022-10-24 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0023_auto_20221023_2032'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='background_color',
            field=models.CharField(choices=[('rbl', 'delve deeper rainbow  to bottom left'), ('rbr', 'delve deeper rainbow  to bottom right'), ('gl', 'golden'), ('wh', 'white'), ('bl', 'black'), ('lb', 'lightblue'), ('pb', 'pastelblue'), ('pp', 'pastelpurple'), ('pr', 'purple'), ('sg', 'seagreen')], default='rbl', max_length=3),
        ),
    ]
