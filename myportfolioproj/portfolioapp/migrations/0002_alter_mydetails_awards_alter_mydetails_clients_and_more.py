# Generated by Django 5.1 on 2024-11-13 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolioapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mydetails',
            name='awards',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='mydetails',
            name='clients',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='mydetails',
            name='completedprojects',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='mydetails',
            name='experience',
            field=models.FloatField(blank=True),
        ),
    ]
