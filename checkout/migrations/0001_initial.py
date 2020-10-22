# Generated by Django 3.0.5 on 2020-10-19 07:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0005_auto_20201009_1629'),
    ]

    operations = [
        migrations.CreateModel(
            name='BillingAddress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=100)),
                ('zipcode', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=30)),
                ('phone', models.CharField(max_length=20)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.Customer')),
            ],
            options={
                'verbose_name_plural': 'Delivery Addresses',
            },
        ),
    ]