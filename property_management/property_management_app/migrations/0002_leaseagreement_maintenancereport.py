# Generated by Django 5.1.1 on 2024-09-15 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property_management_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='LeaseAgreement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tenant_name', models.CharField(max_length=255)),
                ('property_address', models.TextField()),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('document', models.FileField(upload_to='documents/')),
            ],
        ),
        migrations.CreateModel(
            name='MaintenanceReport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tenant_name', models.CharField(max_length=255)),
                ('property_address', models.TextField()),
                ('issue_date', models.DateField()),
                ('description', models.TextField()),
                ('resolution', models.TextField()),
                ('document', models.FileField(upload_to='documents/')),
            ],
            options={
                'verbose_name_plural': 'Maintenance Reports',
            },
        ),
    ]