# Generated by Django 5.0.6 on 2025-01-11 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_table_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='posts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('des', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to='media')),
            ],
        ),
    ]
