# Generated by Django 3.2.15 on 2022-10-15 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_auto_20221014_1534'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='language',
        ),
        migrations.AddField(
            model_name='tag',
            name='type',
            field=models.CharField(choices=[('l', 'language tag'), ('o', 'other')], default='o', max_length=1),
        ),
        migrations.AlterField(
            model_name='post',
            name='tags',
            field=models.ManyToManyField(related_name='tags', to='blog.Tag'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='color',
            field=models.CharField(choices=[('lb', 'lightblue'), ('pb', 'pastelblue'), ('pp', 'pastelpurple'), ('sg', 'seagreen')], default='pb', max_length=2),
        ),
    ]
