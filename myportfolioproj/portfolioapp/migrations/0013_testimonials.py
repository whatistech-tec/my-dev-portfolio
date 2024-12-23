# Generated by Django 5.1 on 2024-11-15 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolioapp', '0012_projects_creation_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Testimonials',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('creation_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('clientname', models.CharField(max_length=80)),
                ('clientposition', models.CharField(max_length=80)),
                ('clientcompany', models.CharField(max_length=80)),
                ('clientview', models.CharField(max_length=250)),
                ('clientimg', models.ImageField(upload_to='projects/')),
            ],
        ),
    ]
