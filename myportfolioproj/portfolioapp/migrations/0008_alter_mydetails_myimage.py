# Generated by Django 5.1 on 2024-11-13 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolioapp', '0007_alter_about_stackname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mydetails',
            name='myimage',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
