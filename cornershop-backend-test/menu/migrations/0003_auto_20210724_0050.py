# Generated by Django 3.0.8 on 2021-07-24 00:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0002_auto_20210724_0042'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='published_date',
            field=models.CharField(default='', max_length=50, unique=True),
        ),
    ]