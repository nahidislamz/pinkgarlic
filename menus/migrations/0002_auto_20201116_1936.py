# Generated by Django 3.0.5 on 2020-11-16 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menus', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='description',
            field=models.CharField(max_length=1000, null=True),
        ),
    ]