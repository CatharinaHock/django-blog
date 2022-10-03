# Generated by Django 3.2.15 on 2022-10-03 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20220926_1958'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['published_date']},
        ),
        migrations.AddField(
            model_name='post',
            name='brief_description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='language',
            field=models.ManyToManyField(blank=True, null=True, to='blog.Language'),
        ),
    ]
