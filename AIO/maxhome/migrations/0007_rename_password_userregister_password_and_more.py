# Generated by Django 5.0.2 on 2024-02-24 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maxhome', '0006_delete_customusermanager_alter_userregister_email'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userregister',
            old_name='password',
            new_name='Password',
        ),
        migrations.RemoveField(
            model_name='userregister',
            name='email',
        ),
        migrations.AddField(
            model_name='userregister',
            name='Email',
            field=models.EmailField(max_length=254, null=True, unique=True),
        ),
    ]
