# Generated by Django 3.0.8 on 2021-07-24 05:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0003_auto_20210724_0050'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='published_date',
            field=models.CharField(default='', max_length=10, unique=True),
        ),
    ]
