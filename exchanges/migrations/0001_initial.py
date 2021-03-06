# Generated by Django 2.0.2 on 2018-02-20 00:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Exchange',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exchange_name', models.CharField(max_length=200)),
                ('api_key', models.CharField(max_length=200)),
                ('secret', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_coin', models.CharField(max_length=5)),
                ('order_coin_used', models.CharField(max_length=5)),
                ('order_date_created', models.DateField(verbose_name='order created')),
                ('order_date_executed', models.DateField(verbose_name='order executed')),
                ('exchange', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exchanges.Exchange')),
            ],
        ),
    ]
