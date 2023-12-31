# Generated by Django 4.2.2 on 2023-10-26 13:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Services', '0005_alter_service_created_by'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='date',
            field=models.DateField(blank=True, null=True, verbose_name='Fecha'),
        ),
        migrations.AlterField(
            model_name='service',
            name='status',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Services.servicestatus'),
        ),
    ]
