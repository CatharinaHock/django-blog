# Generated by Django 3.2.15 on 2022-10-23 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0020_auto_20221021_2040'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='background_color',
            field=models.CharField(choices=[('rbl', 'delve deeper rainbow  to bottom left'), ('rbr', 'delve deeper rainbow  to bottom right'), ('gl', 'golden'), ('wh', 'white'), ('bl', 'black'), ('lb', 'lightblue'), ('pb', 'pastelblue'), ('pp', 'pastelpurple'), ('pr', 'purple'), ('sg', 'seagreen')], default='rb', max_length=3),
        ),
        migrations.AddField(
            model_name='post',
            name='show_whole_thumbnail',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='post',
            name='title_background',
            field=models.CharField(choices=[('no', 'none'), ('gr', 'grey'), ('bl', 'black'), ('wh', 'white'), ('wt', 'white transparent')], default='no', max_length=2),
        ),
        migrations.AlterField(
            model_name='post',
            name='title_color',
            field=models.CharField(choices=[('wh', 'white'), ('lb', 'lightblue'), ('pb', 'pastelblue'), ('pp', 'pastelpurple'), ('pr', 'purple'), ('sg', 'seagreen'), ('bl', 'inkblack')], default='bl', max_length=2),
        ),
    ]