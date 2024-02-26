# Generated by Django 5.0.2 on 2024-02-25 22:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0007_alter_project_project_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='project_progress',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Active', 'Active'), ('Completed', 'Completed')], default='P', max_length=100),
        ),
        migrations.AlterField(
            model_name='project',
            name='project_status',
            field=models.CharField(choices=[('Available', 'Available'), ('Not Available', 'Not Available')], default='A', max_length=100),
        ),
        migrations.AlterField(
            model_name='project',
            name='project_type',
            field=models.CharField(choices=[('Full Time', 'Full Time'), ('Part Time', 'Part Time'), ('Contract', 'Contract')], default='FT', max_length=200),
        ),
    ]
