# Generated by Django 3.0.6 on 2020-05-19 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_auto_20200516_0904'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
