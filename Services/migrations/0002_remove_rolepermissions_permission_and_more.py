# Generated by Django 4.2.2 on 2023-09-27 22:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Services', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rolepermissions',
            name='permission',
        ),
        migrations.RemoveField(
            model_name='rolepermissions',
            name='role',
        ),
        migrations.DeleteModel(
            name='SocialMediaIntegration',
        ),
        migrations.RemoveField(
            model_name='userroles',
            name='role',
        ),
        migrations.RemoveField(
            model_name='userroles',
            name='user',
        ),
        migrations.DeleteModel(
            name='Permission',
        ),
        migrations.DeleteModel(
            name='Role',
        ),
        migrations.DeleteModel(
            name='RolePermissions',
        ),
        migrations.DeleteModel(
            name='UserRoles',
        ),
    ]
