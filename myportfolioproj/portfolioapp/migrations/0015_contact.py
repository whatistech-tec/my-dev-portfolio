# Generated by Django 5.1 on 2024-11-16 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolioapp', '0014_alter_about_stackimage_alter_about_stackname'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=50)),
            ],
        ),
    ]
