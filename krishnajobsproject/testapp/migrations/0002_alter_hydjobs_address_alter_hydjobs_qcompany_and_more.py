# Generated by Django 5.0.4 on 2024-05-03 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hydjobs',
            name='address',
            field=models.CharField(max_length=64),
        ),
        migrations.AlterField(
            model_name='hydjobs',
            name='qcompany',
            field=models.CharField(max_length=64),
        ),
        migrations.AlterField(
            model_name='hydjobs',
            name='title',
            field=models.CharField(max_length=64),
        ),
    ]
