# Generated by Django 5.0.1 on 2024-01-20 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mypost',
            name='title',
            field=models.CharField(max_length=20),
        ),
    ]