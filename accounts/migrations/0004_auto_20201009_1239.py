# Generated by Django 3.1.2 on 2020-10-09 12:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_customer_lname'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='fname',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='lname',
        ),
    ]
