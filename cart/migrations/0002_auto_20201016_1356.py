# Generated by Django 3.0.5 on 2020-10-16 13:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_auto_20201009_1629'),
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cart',
            old_name='timestamp',
            new_name='date_created',
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ordered', models.BooleanField(default=False)),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Out for delivery', 'Out for delivery'), ('Delivered', 'Delivered'), ('Canceled', 'Canceled')], default='Pending', max_length=200, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('customer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.Customer')),
                ('orderitems', models.ManyToManyField(to='cart.Cart')),
            ],
        ),
    ]
