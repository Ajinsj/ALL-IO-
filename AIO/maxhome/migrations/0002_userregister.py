# Generated by Django 5.0.2 on 2024-02-22 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maxhome', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='userregister',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Username', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=100)),
                ('reenter', models.CharField(max_length=100)),
            ],
        ),
    ]
