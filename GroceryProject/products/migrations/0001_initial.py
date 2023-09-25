# Generated by Django 4.2.4 on 2023-09-02 10:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('BrandName', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ProductName', models.CharField(max_length=10)),
                ('Price', models.IntegerField()),
                ('Type', models.CharField(choices=[('Fruits', '1'), ('Vegetables', '2'), ('Dairy', '3'), ('Bread', '4'), ('Cleaners', '5'), ('Paper Goods', '6'), ('Personal Care', '7'), ('Other', '8')], default='1', max_length=20)),
                ('BrandName', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.brand')),
            ],
        ),
    ]
