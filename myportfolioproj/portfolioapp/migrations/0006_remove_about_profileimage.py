# Generated by Django 5.1 on 2024-11-13 12:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolioapp', '0005_delete_mystack_about_stacklogo_about_stackname'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='about',
            name='profileimage',
        ),
    ]
