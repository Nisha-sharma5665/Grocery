# Generated by Django 4.2.4 on 2023-09-02 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='brand',
            name='id',
        ),
        migrations.RemoveField(
            model_name='product',
            name='id',
        ),
        migrations.AddField(
            model_name='brand',
            name='BrandId',
            field=models.AutoField(default=1, primary_key=True, serialize=False),
        ),
        migrations.AddField(
            model_name='product',
            name='ProductId',
            field=models.AutoField(default=1, primary_key=True, serialize=False),
        ),
    ]
