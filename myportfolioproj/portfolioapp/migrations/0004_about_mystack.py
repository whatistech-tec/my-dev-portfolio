# Generated by Django 5.1 on 2024-11-13 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolioapp', '0003_alter_mydetails_awards_alter_mydetails_clients_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profileimage', models.ImageField(null=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='MyStack',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stacklogo', models.ImageField(null=True, upload_to='')),
                ('stackname', models.CharField(max_length=250)),
            ],
        ),
    ]